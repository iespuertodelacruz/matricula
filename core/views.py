from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import StudentForm
from .models import EduLevel
from common.test_data import STUDENT_DATA


def index(request):
    edu_levels = EduLevel.objects.all()
    return render(
        request,
        "index.html",
        {"edu_levels": edu_levels}
    )


def student(request, edulevel_code):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            request.session["student"] = form.cleaned_data
            return HttpResponseRedirect("/academic/")
    else:
        form = StudentForm(STUDENT_DATA)

    return render(
        request,
        "student.html",
        {
            "form": form,
            "edulevel": EduLevel.objects.get(code=edulevel_code),
            "prevent_exit": "false"
        }
    )
