from django import forms
from django.core.exceptions import ValidationError
import re


class AlphaField(forms.CharField):
    def to_python(self, value):
        return value.upper()


class NifField(forms.CharField):
    def to_python(self, value):
        return value.strip().upper()

    def validate(self, value):
        if value and not re.match("^(\d{8}[A-Z])$", value):
            raise ValidationError("{} no es un NIF válido".format(value))


class NieField(forms.CharField):
    def to_python(self, value):
        return value.strip().upper()

    def validate(self, value):
        if value and not re.match("^[A-Z]\d{7}[A-Z]$", value):
            raise ValidationError("{} no es un NIE válido".format(value))


class NumericField(forms.CharField):
    def to_python(self, value):
        return value.strip()

    def validate(self, value):
        if value and not re.match("^\d+$", value):
            raise ValidationError(
                "{} no es un valor válido para este campo".format(value)
            )
