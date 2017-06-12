from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from core.forms.student_form import StudentForm
from .models import EduLevel
from common.test_data import STUDENT_DATA, RESPONSIBLE_DATA
from common.test_data import ACADEMIC_DATA, AUTH_DATA, EXTRA_DATA
from django.urls import reverse
import json
from common import utils
from core.forms.router import get_formclass
from django.conf import settings
from core.forms.auth_forms import PickAuthForm, ExitAuthForm
from core.forms.extra_forms import ExtraForm
from reporto.core import PdfReport
from core.forms.academic_form_FP import get_edulevel
import locale

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

    for s in SECTIONS:
        request.session[s] = None

    request.session["breadcrumbs"] = "[]"

    return render(
        request,
        "index.html",
        {"edu_levels": edu_levels}
    )


def student(request, edulevel_code):
    valid_form = True
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            data = utils.expand_choices(form)
            data["age"] = utils.age(data["birth_date"])
            data["adult"] = data["age"] >= 18
            data["full_name"] = data["name"] + " " + data["surname"]
            lyi = data["lastyear_institution"].upper()
            data["attached_ceip"] = \
                (lyi.find("SAN ANTONIO") != -1) or \
                (lyi.find("TOMÁS DE IRIARTE") != -1) or \
                (lyi.find("TOMAS DE IRIARTE") != -1)
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
            form = StudentForm()

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
            "edulevel": EduLevel.objects.get(code=edulevel_code),
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

    return render(
        request,
        "form.html",
        {
            "title": "Información académica",
            "form": form,
            "edulevel": EduLevel.objects.get(code=edulevel_code),
            "valid_form": valid_form,
            "breadcrumbs": breadcrumbs
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
            "breadcrumbs": breadcrumbs
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
                data["age"] = utils.age(data["birth_date"])
                data["full_name"] = data["name"] + " " + data["surname"]
                data["is_tutor"] = data["link"] in ["TUO", "TUA"]
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
    if request.method == "POST":
        form = PickAuthForm(request.POST)
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
            form = PickAuthForm(json.loads(request.session["auth_pick"]))
        elif settings.DEBUG:
            form = PickAuthForm(AUTH_DATA["pick"])
        else:
            form = PickAuthForm()

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
hacer padre/madre/tutores legales, ó bien aquellas personas que fueran
autorizadas en el siguiente formulario. Máximo de 4 personas. (No incluir aquí
a los responsables).
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
            form = ExitAuthForm(json.loads(request.session["auth_exit"]))
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
            "cancel_btn_msg": "Comenzar nueva matrícula"
        }
    )


def conditions(request):
    return render(
        request,
        "conditions.html"
    )


def form(request, edulevel_code):
    report = PdfReport("form.html", HttpResponse)

    params = utils.load_session_data(request.session, SECTIONS)
    edulevel = EduLevel.objects.get(code=edulevel_code)
    # vocational training
    vt_edulevel = get_edulevel(edulevel_code, params["academic"])

    # signature date (with locale)
    locale.setlocale(locale.LC_TIME, "es_ES.UTF-8")
    signature_date = report.generation_time.strftime("%d de %B de %Y")

    report.render(
        **params,
        edulevel=edulevel,
        vt_edulevel=vt_edulevel,
        school_year=utils.calculate_schoolyear(),
        signature_date=signature_date
    )
    report_name = "Matrícula-{}-{}".format(edulevel_code,
                                           params["student"]["name"])
    return report.http_response(report_name)


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
