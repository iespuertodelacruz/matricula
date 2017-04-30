from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import StudentForm
from .models import EducationLevel


def index(request):
    education_levels = EducationLevel.objects.all()
    return render(
        request,
        "index.html",
        {"education_levels": education_levels}
    )


def student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("/thanks/")
    else:
        form = StudentForm()

    return render(request, "student.html", {"form": form})
