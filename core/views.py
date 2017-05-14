from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from core.forms.student_form import StudentForm
from .models import EduLevel
from common.test_data import STUDENT_DATA, RESPONSIBLE1_DATA, RESPONSIBLE2_DATA
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
    "extra"
]


def index(request):
    edu_levels = EduLevel.objects.all()

    for s in SECTIONS:
        request.session[s] = None

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
        if settings.DEBUG:
            form = StudentForm(STUDENT_DATA)
        else:
            form = StudentForm()

    return render(
        request,
        "form.html",
        {
            "title": "Datos personales del alumno/a",
            "form": form,
            "edulevel": EduLevel.objects.get(code=edulevel_code),
            "valid_form": valid_form,
            "prevent_exit": "false"
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
        if settings.DEBUG:
            form = AcademicForm(ACADEMIC_DATA[edulevel_code]["global"])
        else:
            form = AcademicForm()

    return render(
        request,
        "form.html",
        {
            "title": "Información académica",
            "form": form,
            "edulevel": EduLevel.objects.get(code=edulevel_code),
            "valid_form": valid_form,
            "prevent_exit": "false"
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
        if settings.DEBUG:
            form = ItineraryForm(
                ACADEMIC_DATA[edulevel_code]["itinerary"][itinerary_code]
            )
        else:
            form = ItineraryForm()

    return render(
        request,
        "form.html",
        {
            "title": "Información académica - Itinerario",
            "form": form,
            "edulevel": EduLevel.objects.get(code=edulevel_code),
            "valid_form": valid_form,
            "prevent_exit": "false",
            "itinerary": utils.field_verbose(
                AcademicForm.TRAINING_ITINERARY_CHOICES,
                itinerary_code
            )
        }
    )


def family(request, edulevel_code, responsible_id):
    valid_form = True
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
            key = "responsible{}".format(responsible_id)
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
        if settings.DEBUG:
            if responsible_id == "1":
                form = ResponsibleForm(RESPONSIBLE1_DATA)
            elif responsible_id == "2":
                form = ResponsibleForm(RESPONSIBLE2_DATA)
        else:
            form = ResponsibleForm()

    return render(
        request,
        "form.html",
        {
            "title": "Datos del responsable {}".format(responsible_id),
            "form": form,
            "edulevel": EduLevel.objects.get(code=edulevel_code),
            "valid_form": valid_form,
            "prevent_exit": "false"
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
        if settings.DEBUG:
            form = PickAuthForm(AUTH_DATA["pick"])
        else:
            form = PickAuthForm()

    return render(
        request,
        "form.html",
        {
            "title": "Personas autorizadas a recoger al alumno/a",
            "description": """
El alumnado menor de edad no puede salir del centro durante el período lectivo.
En caso de que hubiera necesidad de recogerlo por algún motivo, sólo lo podrían
hacer padre/madre/tutores legales, ó bien aquellas personas que fueran
autorizadas en el siguiente formulario. Máximo de 4 personas.
            """,
            "form": form,
            "edulevel": EduLevel.objects.get(code=edulevel_code),
            "valid_form": valid_form,
            "prevent_exit": "false"
        }
    )


def auth_exit(request, edulevel_code):
    valid_form = True
    if request.method == "POST":
        form = ExitAuthForm(request.POST)
        if form.is_valid():
            data = utils.expand_choices(form)
            request.session["auth_exit"] = json.dumps(data)
            return HttpResponseRedirect(
                reverse("extra", args=[edulevel_code])
            )
        else:
            valid_form = False
    else:
        form = ExitAuthForm()

    return render(
        request,
        "form.html",
        {
            "title": "Autorizaciones de salida",
            "form": form,
            "edulevel": EduLevel.objects.get(code=edulevel_code),
            "valid_form": valid_form,
            "prevent_exit": "false"
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
        if settings.DEBUG:
            form = ExtraForm(EXTRA_DATA)
        else:
            form = ExtraForm()

    return render(
        request,
        "form.html",
        {
            "title": "Otra información de interés",
            "form": form,
            "edulevel": EduLevel.objects.get(code=edulevel_code),
            "valid_form": valid_form,
            "prevent_exit": "false"
        }
    )


def summary(request, edulevel_code):
    data = utils.load_session_data(request.session, SECTIONS)
    return render(
        request,
        "summary.html",
        {
            "edulevel": EduLevel.objects.get(code=edulevel_code),
            "prevent_exit": "false",
            "data": data
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
    return report.http_response()
