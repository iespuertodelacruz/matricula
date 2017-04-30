from django import forms


class StudentForm(forms.Form):
    name = forms.CharField(label="Nombre", max_length=128)
    surname = forms.CharField(label="Apellidos", max_length=256)
