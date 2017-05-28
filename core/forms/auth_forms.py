from django import forms
from .formfields import NifField


class PickAuthForm(forms.Form):
    nif1 = NifField(
        label="NIF (Persona 1)",
        max_length=32,
        help_text="El NIF es el DNI incluyendo la letra final",
        required=False
    )
    long_name1 = forms.CharField(
        label="NOMBRE Y APELLIDOS (Persona 1)",
        required=False
    )
    nif2 = NifField(
        label="NIF (Persona 2)",
        max_length=32,
        help_text="El NIF es el DNI incluyendo la letra final",
        required=False
    )
    long_name2 = forms.CharField(
        label="NOMBRE Y APELLIDOS (Persona 2)",
        required=False
    )
    nif3 = NifField(
        label="NIF (Persona 3)",
        max_length=32,
        help_text="El NIF es el DNI incluyendo la letra final",
        required=False
    )
    long_name3 = forms.CharField(
        label="NOMBRE Y APELLIDOS (Persona 3)",
        required=False
    )
    nif4 = NifField(
        label="NIF (Persona 4)",
        max_length=32,
        help_text="El NIF es el DNI incluyendo la letra final",
        required=False
    )
    long_name4 = forms.CharField(
        label="NOMBRE Y APELLIDOS (Persona 4)",
        required=False
    )

    def clean(self):
        cleaned_data = super(PickAuthForm, self).clean()
        for i in range(5):
            nif_field = "nif{}".format(i)
            nif = cleaned_data.get(nif_field)
            long_name_field = "long_name{}".format(i)
            long_name = cleaned_data.get(long_name_field)
            if nif and not long_name:
                self.add_error(
                    long_name_field,
                    "Debe especificar nombre y apellidos"
                )
            if not nif and long_name:
                self.add_error(
                    nif_field,
                    "Debe especificar el NIF"
                )


class ExitAuthForm(forms.Form):
    exit_auth_last_lesson = forms.BooleanField(
        required=False,
        initial=True,
        label="""
            Autorizo la salida de mi hijo/hija/tutorizado a última hora sólo
            en el caso de que falte profesorado y no tengan ninguna otra
            actividad pendiente.
        """
    )
    exit_auth_on_env = forms.BooleanField(
        required=False,
        initial=True,
        label="""
            Autorizo la salida de mi hijo/hija/tutorizado a asistir a las
            actividades que se realicen en el entorno del centro y dentro del
            horario lectivo.
        """
    )

    def __init__(self, mandatory, *args, **kwargs):
        super(forms.Form, self).__init__(*args, **kwargs)
        if mandatory:
            self.fields.pop("exit_auth_last_lesson")
