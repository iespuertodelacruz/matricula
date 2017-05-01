from django.shortcuts import render
from django.http import HttpResponseRedirect
from core.forms.student_form import StudentForm
from .models import EduLevel
from common.test_data import STUDENT_DATA
from django.urls import reverse
import json
from common.utils import age, json_dump_handler
from core.forms.academic_index import get_formclass


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
        form = StudentForm(STUDENT_DATA)

    return render(
        request,
        "student.html",
        {
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
            return HttpResponseRedirect("/next/")
        else:
            valid_form = False
    else:
        form = AcademicForm()

    return render(
        request,
        "academic.html",
        {
            "form": form,
            "edulevel": EduLevel.objects.get(code=edulevel_code),
            "valid_form": valid_form,
            "prevent_exit": "false"
        }
    )
