from django import forms


class PickAuthForm(forms.Form):
    id1 = forms.CharField(
        label="NIF/NIE/Pasaporte (Persona 1)",
        max_length=32,
        required=False
    )
    long_name1 = forms.CharField(
        label="NOMBRE Y APELLIDOS (Persona 1)",
        required=False
    )
    id2 = forms.CharField(
        label="NIF/NIE/Pasaporte (Persona 2)",
        max_length=32,
        required=False
    )
    long_name2 = forms.CharField(
        label="NOMBRE Y APELLIDOS (Persona 2)",
        required=False
    )
    id3 = forms.CharField(
        label="NIF/NIE/Pasaporte (Persona 3)",
        max_length=32,
        required=False
    )
    long_name3 = forms.CharField(
        label="NOMBRE Y APELLIDOS (Persona 3)",
        required=False
    )
    id4 = forms.CharField(
        label="NIF/NIE/Pasaporte (Persona 4)",
        max_length=32,
        required=False
    )
    long_name4 = forms.CharField(
        label="NOMBRE Y APELLIDOS (Persona 4)",
        required=False
    )

    def __init__(self, responsibles_ids, *args, **kwargs):
        self.responsibles_ids = responsibles_ids
        super(forms.Form, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(PickAuthForm, self).clean()
        for i in range(5):
            id_field = "id{}".format(i)
            id_value = cleaned_data.get(id_field)
            long_name_field = "long_name{}".format(i)
            long_name = cleaned_data.get(long_name_field)
            if id_value and not long_name:
                self.add_error(
                    long_name_field,
                    "Debe especificar nombre y apellidos"
                )
            if not id_value and long_name:
                self.add_error(
                    id_field,
                    "Debe especificar el NIF"
                )
            if id_value in self.responsibles_ids:
                self.add_error(
                    id_field,
                    ("No puede poner a los responsables como personas "
                     "autorizadas")
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
