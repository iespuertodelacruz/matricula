from django import forms
from django.core.exceptions import ValidationError
import re
import datetime


class NifField(forms.CharField):
    def validate(self, value):
        if value and not re.match("^(\d{8}[A-Za-z])$", value):
            raise ValidationError("{} no es un NIF válido".format(value))


class NieField(forms.CharField):
    def validate(self, value):
        if value and not re.match("^[A-Za-z]\d{7}[A-Za-z]$", value):
            raise ValidationError("{} no es un NIE válido".format(value))


class NumericField(forms.CharField):
    def validate(self, value):
        if value and not re.match("^\d+$", value):
            raise ValidationError(
                "{} no es un valor válido para este campo".format(value)
            )


class BirthDateField(forms.DateField):
    def validate(self, value):
        delta = (datetime.date.today() - value).days / 365
        if delta <= 10:
            raise ValidationError(
                "La fecha de nacimiento no parece correcta"
            )
