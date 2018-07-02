from django import forms
from .formfields import (NifField,
                         NieField,
                         NumericField,
                         BirthDateField,
                         SocialSecurityNumberField)


class StudentForm(forms.Form):
    GENDER_CHOICES = sorted((
        ("H", "Hombre"),
        ("M", "Mujer")),
        key=lambda x: x[1]
    )

    name = forms.CharField(
        label="Nombre",
        max_length=128,
    )
    surname = forms.CharField(
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
    birth_date = BirthDateField(
        label="Fecha de nacimiento",
        required=True,
        widget=forms.TextInput(attrs={"class": "datepicker"}),
        help_text="Formato de fecha: dd/mm/aaaa"
    )
    birth_country = forms.CharField(
        label="País de nacimiento",
        max_length=128,
        initial="España"
    )
    birth_province = forms.CharField(
        label="Provincia de nacimiento",
        max_length=128,
        required=False,
        initial="Santa Cruz de Tenerife"
    )
    birth_town = forms.CharField(
        label="Localidad de nacimiento",
        max_length=128,
        initial="Puerto de la Cruz"
    )
    nationality = forms.CharField(
        label="Nacionalidad",
        max_length=64,
        initial="Española"
    )
    social_security_number = SocialSecurityNumberField(
        label="Número de la seguridad social",
        max_length=32,
        required=False
    )
    address = forms.CharField(
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
    hometown = forms.CharField(
        label="Municipio",
        help_text="Domicilio durante el curso escolar",
        initial="Puerto de la Cruz"
    )
    lastyear_in_other_institution = forms.BooleanField(
        label="Marque esta casilla si estudió el curso pasado en otro centro",
        required=False,
        initial=False
    )
    lastyear_institution = forms.CharField(
        label="Centro de procedencia",
        max_length=256,
        help_text="Cumplimentar sólo si el curso anterior realizó estudios en "
                  "otro centro",
        required=False
    )
    lastyear_studies = forms.CharField(
        label="Estudios realizados el curso anterior",
        max_length=256,
        help_text="Cumplimentar sólo si el curso anterior realizó estudios en "
                  "otro centro",
        required=False
    )
    repeater = forms.BooleanField(
        label="Repetidor/a",
        required=False,
        help_text="Indique si repite curso"
    )

    def __init__(self, *args, **kwargs):
        edulevel = kwargs.pop("edulevel", None)
        super(StudentForm, self).__init__(*args, **kwargs)
        if edulevel and edulevel.is_first_course():
            self.fields["lastyear_in_other_institution"].initial = True

    def clean(self):
        cleaned_data = super(StudentForm, self).clean()
        nif = cleaned_data.get("nif")
        nie = cleaned_data.get("nie")
        passport = cleaned_data.get("passport")
        lastyear_studies = cleaned_data.get("lastyear_studies")
        lastyear_institution = cleaned_data.get("lastyear_institution")
        lastyear_in_other_institution = cleaned_data.get(
            "lastyear_in_other_institution"
        )

        if (not nif) and (not nie) and (not passport):
            msg = "Debe especificar NIF, NIE ó Pasaporte"
            self.add_error("nif", msg)
            self.add_error("nie", msg)
            self.add_error("passport", msg)

        if lastyear_in_other_institution and not lastyear_institution:
            msg = ("Indicó que estudió el curso pasado en otro centro. "
                   "Debe especificar centro de procedencia")
            self.add_error("lastyear_institution", msg)

        if lastyear_in_other_institution and not lastyear_studies:
            msg = ("Indicó que estudió el curso pasado en otro centro. "
                   "Debe especificar los estudios realizados")
            self.add_error("lastyear_studies", msg)

        if not lastyear_in_other_institution and lastyear_institution:
            msg = ("Indicó que NO estudió el curso pasado en otro centro. "
                   "Debe borrar centro de procedencia")
            self.add_error("lastyear_institution", msg)

        if not lastyear_in_other_institution and lastyear_studies:
            msg = ("Indicó que NO estudió el curso pasado en otro centro. "
                   "Debe borrar los estudios realizados")
            self.add_error("lastyear_studies", msg)
