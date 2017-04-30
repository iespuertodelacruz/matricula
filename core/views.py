from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import StudentForm


def index(request):
    return render(request, "index.html")


def student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("/thanks/")
    else:
        form = StudentForm()

    return render(request, "student.html", {"form": form})
