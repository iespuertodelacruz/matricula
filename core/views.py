from django.shortcuts import render
from django.http import HttpResponseRedirect
from core.forms.student_form import StudentForm
from .models import EduLevel
from common.test_data import STUDENT_DATA, RESPONSIBLE1_DATA, RESPONSIBLE2_DATA
from django.urls import reverse
import json
from common.utils import age, json_dump_handler, field_verbose
from core.forms.router import get_formclass
from django.conf import settings


def index(request):
    edu_levels = EduLevel.objects.all()
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
            form.cleaned_data["age"] = age(
                form.cleaned_data["birth_date"]
            )
            form.cleaned_data["adult"] = form.cleaned_data["age"] >= 18
            request.session["student"] = json.dumps(
                form.cleaned_data,
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
            request.session["academic"] = form.cleaned_data
            training_itinerary = form.cleaned_data.get("training_itinerary")
            if training_itinerary:
                return HttpResponseRedirect(
                    reverse("itinerary", args=[
                        edulevel_code, training_itinerary
                    ])
                )
            elif json.loads(request.session["student"])["adult"]:
                return HttpResponseRedirect("next")
            else:
                return HttpResponseRedirect(
                    reverse("family", args=[edulevel_code, 1])
                )
        else:
            valid_form = False
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
            request.session["itinerary"] = form.cleaned_data
            if request.session["student"].adult:
                return HttpResponseRedirect("next")
            else:
                return HttpResponseRedirect(
                    reverse("family", args=[edulevel_code, 1])
                )
        else:
            valid_form = False
    else:
        form = ItineraryForm()

    return render(
        request,
        "form.html",
        {
            "title": "Información académica (Itinerario)",
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
                request.session[key] = json.dumps(
                    form.cleaned_data,
                    default=json_dump_handler
                )
            if responsible_id == "1":
                return HttpResponseRedirect(
                    reverse("family", args=[edulevel_code, 2])
                )
            elif responsible_id == "2":
                return HttpResponseRedirect("/next")
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
