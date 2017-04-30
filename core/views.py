from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import StudentForm
from .models import EduLevel


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
            return HttpResponseRedirect("/thanks/")
    else:
        form = StudentForm()

    return render(
        request,
        "student.html",
        {
            "form": form,
            "edulevel": EduLevel.objects.get(code=edulevel_code)
        }
    )
