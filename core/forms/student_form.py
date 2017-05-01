from django import forms
from .formfields import NifField, NieField, AlphaField, NumericField

GENDER_CHOICES = (
    ("H", "Hombre"),
    ("M", "Mujer")
)


class StudentForm(forms.Form):
    name = AlphaField(
        label="Nombre",
        max_length=128,
    )
    surname = AlphaField(
        label="Apellidos",
        max_length=256
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
    gender = forms.ChoiceField(
        label="Sexo",
        choices=GENDER_CHOICES
    )
    home_phone = NumericField(
        max_length=16,
        label="Teléfono de casa",
        required=False
    )
    mobile_phone = NumericField(
        max_length=16,
        label="Teléfono móvil",
        required=False
    )
    email = forms.EmailField(
        label="Correo electrónico",
        required=False
    )
    birth_date = forms.DateField(
        label="Fecha de nacimiento",
        required=True,
        widget=forms.TextInput(attrs={"class": "datepicker"})
    )
    birth_country = AlphaField(
        label="País de nacimiento",
        max_length=128,
        initial="España"
    )
    birth_province = AlphaField(
        label="Provincia de nacimiento",
        max_length=128,
        required=False,
        initial="Santa Cruz de Tenerife"
    )
    birth_town = AlphaField(
        label="Localidad de nacimiento",
        max_length=128,
        initial="Puerto de la Cruz"
    )
    nationality = AlphaField(
        label="Nacionalidad",
        max_length=64,
        initial="Española"
    )
    social_security_number = NumericField(
        label="Número de la seguridad social",
        max_length=32,
        required=False
    )
    address = AlphaField(
        label="Dirección",
        max_length=128,
        help_text="Domicilio durante el curso escolar"
    )
    zipcode = forms.CharField(
        label="Código postal",
        max_length=16,
        help_text="Domicilio durante el curso escolar",
        initial="38400"
    )
    hometown = AlphaField(
        label="Municipio",
        help_text="Domicilio durante el curso escolar",
        initial="Puerto de la Cruz"
    )
    lastyear_institution = AlphaField(
        label="Centro de procedencia",
        max_length=256,
        help_text="Cumplimentar sólo si el curso anterior realizó estudios en "
                  "otro centro",
        required=False
    )
    lastyear_studies = AlphaField(
        label="Estudios realizados el curso anterior",
        max_length=256,
        help_text="Cumplimentar sólo si el curso anterior realizó estudios en "
                  "otro centro",
        required=False
    )

    def clean(self):
        cleaned_data = super(StudentForm, self).clean()
        nif = cleaned_data.get("nif")
        nie = cleaned_data.get("nie")
        passport = cleaned_data.get("passport")

        if (not nif) and (not nie) and (not passport):
            msg = "Debe especificar NIF, NIE ó Pasaporte"
            self.add_error("nif", msg)
            self.add_error("nie", msg)
            self.add_error("passport", msg)
