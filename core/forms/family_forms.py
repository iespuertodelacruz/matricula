from django import forms
from .formfields import NifField, NieField, NumericField


class ResponsibleForm(forms.Form):
    GENDER_CHOICES = sorted((
        ("H", "Hombre"),
        ("M", "Mujer")),
        key=lambda x: x[1]
    )
    LINK_CHOICES = sorted((
        ("PAD", "Padre"),
        ("MAD", "Madre"),
        ("TUO", "Tutor"),
        ("TUA", "Tutora")),
        key=lambda x: x[1]
    )

    gender = forms.ChoiceField(
        label="Sexo",
        choices=GENDER_CHOICES
    )
    name = forms.CharField(
        label="Nombre",
        max_length=128,
    )
    surname = forms.CharField(
        label="Apellidos",
        max_length=256
    )
    link = forms.ChoiceField(
        choices=LINK_CHOICES,
        label="Vínculo con el alumno/a"
    )
    nif = NifField(
        label="NIF",
        max_length=32,
        required=False,
        help_text="El NIF es el DNI incluyendo la letra final",
    )
    nie = NieField(
        label="NIE",
        max_length=32,
        required=False,
        help_text="El NIE es el número de identidad de extranjeros"
    )
    passport = forms.CharField(
        label="Pasaporte",
        max_length=32,
        required=False,
        help_text="Cumplimentar sólo en el caso de que no se tenga DNI/NIE"
    )
    mobile_phone = NumericField(
        max_length=16,
        label="Teléfono móvil",
        required=False
    )
    email = forms.EmailField(
        label="Correo electrónico",
        required=False,
        help_text="Muy importante para las comunicaciones con el centro"
    )
    birth_date = forms.DateField(
        label="Fecha de nacimiento",
        required=True,
        widget=forms.TextInput(attrs={"class": "datepicker"})
    )
    job = forms.CharField(
        label="Profesión",
        required=False
    )
    separated = forms.BooleanField(
        label="Padres separados/divorciados",
        required=False,
        initial=False
    )
    parental_auth = forms.BooleanField(
        label="Patria potestad",
        required=False,
        initial=True,
        help_text="Indicar sólo en el caso de padres separados/divorciados"
    )
    children_custody = forms.BooleanField(
        label="Guarda custodia",
        required=False,
        initial=True,
        help_text="Indicar sólo en el caso de padres separados/divorciados"
    )

    def clean(self):
        cleaned_data = super(ResponsibleForm, self).clean()
        nif = cleaned_data.get("nif")
        nie = cleaned_data.get("nie")
        passport = cleaned_data.get("passport")

        if (not nif) and (not nie) and (not passport):
            msg = "Debe especificar NIF, NIE ó Pasaporte"
            self.add_error("nif", msg)
            self.add_error("nie", msg)
            self.add_error("passport", msg)

        return cleaned_data


class UnknownResponsibleForm(forms.Form):

    ignore_info = forms.BooleanField(
        label="Se desconocen los datos de este responsable",
        help_text="""
Marque esta opción si se trata de una familia monoparental. En este caso, no es
necesario que rellene este formulario. Los datos que introduzca se ignorarán.
Sólo debe pulsar el botón de 'Continuar' que está al pie de esta página
""",
        required=False
    )


class Responsible1Form(ResponsibleForm):
    pass


class Responsible2Form(ResponsibleForm, UnknownResponsibleForm):
    def __init__(self, *args, **kwargs):
        super(Responsible2Form, self).__init__(*args, **kwargs)
        self.fields["gender"].required = False
        self.fields["name"].required = False
        self.fields["surname"].required = False
        self.fields["birth_date"].required = False

    def clean(self):
        cleaned_data = super(Responsible2Form, self).clean()
        ignore_info = cleaned_data.get("ignore_info")
        print(ignore_info)
        if not ignore_info:
            if not cleaned_data.get("gender"):
                self.add_error("gender", "Este campo es obligatorio")
            if not cleaned_data.get("name"):
                self.add_error("name", "Este campo es obligatorio")
            if not cleaned_data.get("surname"):
                self.add_error("surname", "Este campo es obligatorio")
            if not cleaned_data.get("birth_date"):
                self.add_error("birth_date", "Este campo es obligatorio")
