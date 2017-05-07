from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from core.forms.student_form import StudentForm
from .models import EduLevel
from common.test_data import STUDENT_DATA, RESPONSIBLE1_DATA, RESPONSIBLE2_DATA
from common.test_data import ACADEMIC_DATA
from django.urls import reverse
import json
from common.utils import age, json_dump_handler, field_verbose, expand_choices
from common.utils import calculate_schoolyear
from core.forms.router import get_formclass
from django.conf import settings
from core.forms.extra_forms import ExtraForm
from reporto.core import PdfReport
from core.forms.academic_form_FP import get_edulevel

SECTIONS = [
    "student",
    "academic",
    "itinerary",
    "responsible1",
    "responsible2",
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
            data = expand_choices(form)
            data["age"] = age(data["birth_date"])
            data["adult"] = data["age"] >= 18
            request.session["student"] = json.dumps(
                data,
                default=json_dump_handler
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
            data = expand_choices(form)
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
            data = expand_choices(form)
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
            "itinerary": field_verbose(
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
            if not form.cleaned_data.get("ignore_info"):
                key = "responsible{}".format(responsible_id)
                data = expand_choices(form)
                request.session[key] = json.dumps(
                    data,
                    default=json_dump_handler
                )
            if responsible_id == "1":
                return HttpResponseRedirect(
                    reverse("family", args=[edulevel_code, 2])
                )
            elif responsible_id == "2":
                return HttpResponseRedirect(
                    reverse("extra", args=[edulevel_code])
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


def extra(request, edulevel_code):
    valid_form = True
    if request.method == "POST":
        form = ExtraForm(request.POST)
        if form.is_valid():
            data = expand_choices(form)
            request.session["extra"] = json.dumps(data)
            return HttpResponseRedirect(
                reverse("form", args=[edulevel_code])
            )
        else:
            valid_form = False
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


def form(request, edulevel_code):
    report = PdfReport("form.html", HttpResponse)

    params = {}
    for s in SECTIONS:
        if request.session.get(s):
            v = json.loads(request.session[s])
        else:
            v = None
        params[s] = v
    edulevel = EduLevel.objects.get(code=edulevel_code)
    # vocational training
    vt_edulevel = get_edulevel(edulevel_code, params["academic"])

    report.render(
        **params,
        edulevel=edulevel,
        vt_edulevel=vt_edulevel,
        school_year=calculate_schoolyear()
    )
    return report.http_response()
