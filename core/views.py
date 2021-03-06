import json
import locale
import os
import uuid

from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from PyPDF2 import PdfFileMerger

from common import utils
from common.test_data import (ACADEMIC_DATA, AUTH_DATA, EXTRA_DATA,
                              RESPONSIBLE_DATA, STUDENT_DATA)
from core.forms.academic_form_FP import get_edulevel
from core.forms.auth_forms import ExitAuthForm, PickAuthForm
from core.forms.extra_forms import ExtraForm
from core.forms.router import get_formclass
from core.forms.student_form import StudentForm
from reporto.core import PdfReport

from .models import EduLevel, Config

SECTIONS = [
    "student",
    "academic",
    "itinerary",
    "responsible1",
    "responsible2",
    "auth_pick",
    "auth_exit",
    "extra",
]


def index(request):
    edu_levels = EduLevel.objects.all()
    config = Config.objects.first()

    for s in SECTIONS:
        request.session[s] = None

    request.session["breadcrumbs"] = "[]"

    return render(
        request,
        "index.html",
        {
            'config': config,
            "edu_levels": edu_levels,
        }
    )


def multi_enrollment(request, edulevel_code):
    edulevel = EduLevel.objects.get(code=edulevel_code)
    return render(
        request,
        "multi_enrollment.html",
        {
            "edulevel": edulevel,
        }
    )


def student(request, edulevel_code):
    valid_form = True
    edulevel = EduLevel.objects.get(code=edulevel_code)

    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            data = utils.expand_choices(form)
            data = utils.add_fields_to_student(data)
            request.session["student"] = json.dumps(
                data,
                default=utils.json_dump_handler
            )

            return HttpResponseRedirect(
                reverse("academic", args=[edulevel_code])
            )
        else:
            valid_form = False
    else:
        if request.session["student"]:
            form = StudentForm(json.loads(request.session["student"]))
        elif settings.DEBUG:
            form = StudentForm(STUDENT_DATA)
        else:
            form = StudentForm(edulevel=edulevel)

    breadcrumbs, request.session["breadcrumbs"] = utils.add_breadcrumb(
        "Alumno/a",
        reverse("student", args=[edulevel_code]),
        request.session["breadcrumbs"],
    )

    return render(
        request,
        "form.html",
        {
            "title": "Datos personales del alumno/a",
            "form": form,
            "edulevel": edulevel,
            "valid_form": valid_form,
            "breadcrumbs": breadcrumbs
        }
    )


def academic(request, edulevel_code):
    AcademicForm = get_formclass(edulevel_code)
    valid_form = True
    if request.method == "POST":
        form = AcademicForm(request.POST)
        if form.is_valid():
            training_itinerary = form.cleaned_data.get("training_itinerary")
            data = utils.expand_choices(form)
            request.session["academic"] = json.dumps(data)
            if training_itinerary:
                return HttpResponseRedirect(
                    reverse("itinerary", args=[
                        edulevel_code, training_itinerary
                    ])
                )
            elif json.loads(request.session["student"])["adult"]:
                return HttpResponseRedirect(
                    reverse("extra", args=[edulevel_code])
                )
            else:
                return HttpResponseRedirect(
                    reverse("family", args=[edulevel_code, 1])
                )
        else:
            valid_form = False
    else:
        if request.session["academic"]:
            form = AcademicForm(json.loads(request.session["academic"]))
        elif settings.DEBUG:
            form = AcademicForm(ACADEMIC_DATA[edulevel_code]["global"])
        else:
            form = AcademicForm()

    breadcrumbs, request.session["breadcrumbs"] = utils.add_breadcrumb(
        "Académico",
        reverse("academic", args=[edulevel_code]),
        request.session["breadcrumbs"]
    )

    edulevel = EduLevel.objects.get(code=edulevel_code)
    if edulevel.is_vocational_training():
        description = None
    else:
        description = """
            Queremos aclarar que las elecciones de materias no son
            definitivas, y por lo tanto, pueden cambiar, en función de
            la disponibilidad asignada por la Dirección General de Personal
            ó de las ratios del alumnado, entre otros factores.
        """

    return render(
        request,
        "form.html",
        {
            "title": "Información académica",
            "form": form,
            "edulevel": EduLevel.objects.get(code=edulevel_code),
            "valid_form": valid_form,
            "breadcrumbs": breadcrumbs,
            "description": description
        }
    )


def itinerary(request, edulevel_code, itinerary_code):
    AcademicForm = get_formclass(edulevel_code)
    ItineraryForm = get_formclass("{}_{}".format(
        edulevel_code,
        itinerary_code
    ))
    valid_form = True
    if request.method == "POST":
        form = ItineraryForm(request.POST)
        if form.is_valid():
            data = utils.expand_choices(form)
            data["itinerary_code"] = itinerary_code
            request.session["itinerary"] = json.dumps(data)
            if json.loads(request.session["student"])["adult"]:
                return HttpResponseRedirect(
                    reverse("extra", args=[edulevel_code])
                )
            else:
                return HttpResponseRedirect(
                    reverse("family", args=[edulevel_code, 1])
                )
        else:
            valid_form = False
    else:
        if request.session["itinerary"]:
            form = ItineraryForm(json.loads(request.session["itinerary"]))
        elif settings.DEBUG:
            form = ItineraryForm(
                ACADEMIC_DATA[edulevel_code]["itinerary"][itinerary_code]
            )
        else:
            form = ItineraryForm()

    breadcrumbs, request.session["breadcrumbs"] = utils.add_breadcrumb(
        "Itinerario",
        reverse("itinerary", args=[edulevel_code, itinerary_code]),
        request.session["breadcrumbs"]
    )

    edulevel = EduLevel.objects.get(code=edulevel_code)
    if edulevel.is_vocational_training():
        description = None
    else:
        description = """
            Queremos aclarar que las elecciones de materias no son
            definitivas, y por lo tanto, pueden cambiar, en función de
            la disponibilidad asignada por la Dirección General de Personal
            ó de las ratios del alumnado, entre otros factores.
        """
    return render(
        request,
        "form.html",
        {
            "title": "Información académica - Itinerario",
            "form": form,
            "edulevel": EduLevel.objects.get(code=edulevel_code),
            "valid_form": valid_form,
            "itinerary": utils.field_verbose(
                AcademicForm.TRAINING_ITINERARY_CHOICES,
                itinerary_code
            ),
            "breadcrumbs": breadcrumbs,
            "description": description
        }
    )


def family(request, edulevel_code, responsible_id):
    valid_form = True
    key = "responsible{}".format(responsible_id)
    ResponsibleForm = get_formclass("R" + responsible_id)
    if request.method == "POST":
        form = ResponsibleForm(request.POST)
        if form.is_valid():
            if form.cleaned_data.get("ignore_info"):
                data = {"ignore_info": True}
            else:
                data = utils.expand_choices(form)
                data = utils.add_fields_to_responsible(data)
            data["id"] = responsible_id
            request.session[key] = json.dumps(
                data,
                default=utils.json_dump_handler
            )
            if responsible_id == "1":
                return HttpResponseRedirect(
                    reverse("family", args=[edulevel_code, 2])
                )
            elif responsible_id == "2":
                return HttpResponseRedirect(
                    reverse("auth_pick", args=[edulevel_code])
                )
        else:
            valid_form = False
    else:
        if request.session[key]:
            form = ResponsibleForm(json.loads(request.session[key]))
        elif settings.DEBUG:
            form = ResponsibleForm(RESPONSIBLE_DATA[responsible_id])
        else:
            form = ResponsibleForm()

    breadcrumbs, request.session["breadcrumbs"] = utils.add_breadcrumb(
        "Responsable " + responsible_id,
        reverse("family", args=[edulevel_code, responsible_id]),
        request.session["breadcrumbs"]
    )

    return render(
        request,
        "form.html",
        {
            "title": "Datos del responsable {}".format(responsible_id),
            "form": form,
            "edulevel": EduLevel.objects.get(code=edulevel_code),
            "valid_form": valid_form,
            "breadcrumbs": breadcrumbs
        }
    )


def auth_pick(request, edulevel_code):
    valid_form = True
    responsibles_ids = utils.get_responsibles_ids(request.session)
    if request.method == "POST":
        form = PickAuthForm(responsibles_ids, request.POST)
        if form.is_valid():
            data = utils.expand_choices(form)
            request.session["auth_pick"] = json.dumps(data)
            return HttpResponseRedirect(
                reverse("auth_exit", args=[edulevel_code])
            )
        else:
            valid_form = False
    else:
        if request.session["auth_pick"]:
            form = PickAuthForm(
                responsibles_ids,
                json.loads(request.session["auth_pick"])
            )
        elif settings.DEBUG:
            form = PickAuthForm(
                responsibles_ids,
                AUTH_DATA["pick"]
            )
        else:
            form = PickAuthForm(responsibles_ids)

    breadcrumbs, request.session["breadcrumbs"] = utils.add_breadcrumb(
        "Recogida",
        reverse("auth_pick", args=[edulevel_code]),
        request.session["breadcrumbs"]
    )

    return render(
        request,
        "form.html",
        {
            "title": "Personas autorizadas a recoger al alumno/a",
            "description": """
El alumnado menor de edad no puede salir del centro durante el período lectivo.
En caso de que hubiera necesidad de recogerlo por algún motivo, sólo lo podrían
hacer padre/madre/tutores legales, ó bien aquellas personas mayores de edad que
fueran autorizadas en el siguiente formulario. Máximo de 4 personas.
(No incluir aquí a los responsables).
            """,
            "form": form,
            "edulevel": EduLevel.objects.get(code=edulevel_code),
            "valid_form": valid_form,
            "breadcrumbs": breadcrumbs
        }
    )


def auth_exit(request, edulevel_code):
    valid_form = True
    edulevel = EduLevel.objects.get(code=edulevel_code)
    if request.method == "POST":
        form = ExitAuthForm(edulevel.is_mandatory(), request.POST)
        if form.is_valid():
            data = utils.expand_choices(form)
            request.session["auth_exit"] = json.dumps(data)
            return HttpResponseRedirect(
                reverse("extra", args=[edulevel_code])
            )
        else:
            valid_form = False
    else:
        if request.session["auth_exit"]:
            form = ExitAuthForm(
                edulevel.is_mandatory(),
                json.loads(request.session["auth_exit"])
            )
        else:
            form = ExitAuthForm(edulevel.is_mandatory())

    breadcrumbs, request.session["breadcrumbs"] = utils.add_breadcrumb(
        "Salida",
        reverse("auth_exit", args=[edulevel_code]),
        request.session["breadcrumbs"]
    )

    return render(
        request,
        "form.html",
        {
            "title": "Autorizaciones de salida",
            "form": form,
            "edulevel": edulevel,
            "valid_form": valid_form,
            "breadcrumbs": breadcrumbs
        }
    )


def extra(request, edulevel_code):
    valid_form = True
    if request.method == "POST":
        form = ExtraForm(request.POST)
        if form.is_valid():
            data = utils.expand_choices(form)
            request.session["extra"] = json.dumps(data)
            return HttpResponseRedirect(
                reverse("summary", args=[edulevel_code])
            )
        else:
            valid_form = False
    else:
        if request.session["extra"]:
            form = ExtraForm(json.loads(request.session["extra"]))
        elif settings.DEBUG:
            form = ExtraForm(EXTRA_DATA)
        else:
            form = ExtraForm()

    breadcrumbs, request.session["breadcrumbs"] = utils.add_breadcrumb(
        "Extra",
        reverse("extra", args=[edulevel_code]),
        request.session["breadcrumbs"]
    )

    return render(
        request,
        "form.html",
        {
            "title": "Otra información de interés",
            "form": form,
            "edulevel": EduLevel.objects.get(code=edulevel_code),
            "valid_form": valid_form,
            "breadcrumbs": breadcrumbs
        }
    )


def summary(request, edulevel_code):
    config = Config.objects.first()
    data = utils.load_session_data(request.session, SECTIONS)

    breadcrumbs, request.session["breadcrumbs"] = utils.add_breadcrumb(
        "Resumen",
        reverse("summary", args=[edulevel_code]),
        request.session["breadcrumbs"]
    )

    return render(
        request,
        "summary.html",
        {
            "edulevel": EduLevel.objects.get(code=edulevel_code),
            "data": data,
            "breadcrumbs": breadcrumbs,
            "edulevels": EduLevel.objects.all(),
            "cancel_btn_msg": "Comenzar nueva matrícula",
            'config': config
        }
    )


def conditions(request):
    return render(
        request,
        "conditions.html"
    )


def form(request, edulevel_code):
    config = Config.objects.first()
    params = utils.load_session_data(request.session, SECTIONS)
    edulevel = EduLevel.objects.get(code=edulevel_code)
    # vocational training
    vt_edulevel = get_edulevel(edulevel_code, params["academic"])

    school_copy = PdfReport("form.html")
    # signature date (with locale)
    locale.setlocale(locale.LC_TIME, "es_ES.UTF-8")
    signature_date = school_copy.generation_time.strftime("%d de %B de %Y")
    school_copy.render(
        **params,
        edulevel=edulevel,
        vt_edulevel=vt_edulevel,
        config=config,
        signature_date=signature_date,
        copy_target="centro"
    )

    applicant_copy = PdfReport("form.html")
    # signature date (with locale)
    locale.setlocale(locale.LC_TIME, "es_ES.UTF-8")
    signature_date = applicant_copy.generation_time.strftime("%d de %B de %Y")
    applicant_copy.render(
        **params,
        edulevel=edulevel,
        vt_edulevel=vt_edulevel,
        config=config,
        signature_date=signature_date,
        copy_target="interesado"
    )

    payment_doc = os.path.join(
        os.path.dirname(__file__),
        "docs",
        edulevel.enrollment_payment_doc()
    )

    documentation = PdfReport("documentation.html")
    documentation.render(
        **params,
        edulevel=edulevel
    )

    merger = PdfFileMerger()
    merger.append(school_copy.output_filename)
    merger.append(applicant_copy.output_filename)
    merger.append(payment_doc)
    merger.append(documentation.output_filename)

    report_name = "Matrícula-{}-{}".format(edulevel_code,
                                           params["student"]["name"])
    report_filename = "/tmp/" + str(uuid.uuid4()) + ".pdf"
    merger.write(report_filename)
    response = HttpResponse(open(report_filename, "rb"))
    os.remove(school_copy.output_filename)
    os.remove(applicant_copy.output_filename)
    os.remove(documentation.output_filename)
    os.remove(report_filename)
    response["Content-Type"] = "application/pdf"
    response["Content-Disposition"] = \
        "attachment; filename={}.pdf".format(report_name)
    return response


def change_edulevel(request, edulevel_code):
    target_edulevel_id = request.POST["target_edulevel_id"]
    target_edulevel = EduLevel.objects.get(pk=target_edulevel_id)
    request.session["academic"] = None
    request.session["itinerary"] = None
    request.session["breadcrumbs"] = utils.update_breadcrumbs(
        edulevel_code,
        target_edulevel.code,
        request.session["breadcrumbs"]
    )
    return HttpResponseRedirect(
        reverse("academic", args=[target_edulevel.code])
    )
