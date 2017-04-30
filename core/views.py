from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import StudentForm
from .models import EduLevel
import json


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
            print(json.dumps(form.cleaned_data))
            return HttpResponseRedirect("/academic/")
    else:
        data = {
            "name": "John",
            "surname": "Test1 Test2",
            "nif": "12345678Y",
            "nie": "",
            "passport": "",
            "gender": "M",
            "home_phone": "",
            "mobile_phone": "555555555",
            "email": "test@test.com",
            "birth_date": "1/6/1975",
            "birth_country": "Spain",
            "birth_province": "Testing",
            "birth_town": "Hometown",
            "nationality": "Spanish",
            "social_security_number": "",
            "address": "Street Chrome, 10",
            "zipcode": "54321",
            "hometown": "Hometown",
            "lastyear_institution": "Google",
            "lastyear_studies": "Computing"
        }
        form = StudentForm(data)

    return render(
        request,
        "student.html",
        {
            "form": form,
            "edulevel": EduLevel.objects.get(code=edulevel_code),
            "prevent_exit": "true"
        }
    )
