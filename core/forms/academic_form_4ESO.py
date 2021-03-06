from django import forms


class AcademicForm_4ESO(forms.Form):
    TRAINING_ITINERARY_CHOICES = sorted((
        ("EAC", "Enseñanzas ACADÉMICAS para la iniciación al "
                "Bachillerato"),
        ("EAP", "Enseñanzas APLICADAS para la iniciación a la Formación "
                "Profesional")),
        key=lambda x: x[1]
    )
    SPECIFIC_SUBJECT1_CHOICES = sorted((
        ("RLG", "Religión"),
        ("VAO", "Valores éticos")),
        key=lambda x: x[1]
    )
    SPECIFIC_SUBJECT2_CHOICES = sorted((
        ("SGA", "Alemán"),
        ("AEZ", "Artes escénicas y danza"),
        ("CUF", "Cultura científica"),
        ("CUC", "Cultura clásica"),
        ("EPV", "Educación plástica, visual y audiovisual"),
        ("FIL", "Filosofía"),
        ("SGN", "Francés"),
        ("MUS", "Música"),
        ("TEE", "Tecnología"),
        ("TGD", "Informática")),
        key=lambda x: x[1]
    )

    training_itinerary = forms.ChoiceField(
        choices=TRAINING_ITINERARY_CHOICES,
        label="ITINERARIO",
    )
    specific_subject1 = forms.ChoiceField(
        choices=SPECIFIC_SUBJECT1_CHOICES,
        label="MATERIA ESPECÍFICA 1",
    )
    specific_subject2_order1 = forms.ChoiceField(
        choices=SPECIFIC_SUBJECT2_CHOICES,
        label="MATERIA ESPECÍFICA 2 (Preferencia 1)",
        help_text="Seleccione la materia que quiera cursar en 1er lugar.<br>"
                  "Cusará dos materias de las que se le asignen."
    )
    specific_subject2_order2 = forms.ChoiceField(
        choices=SPECIFIC_SUBJECT2_CHOICES,
        label="MATERIA ESPECÍFICA 2 (Preferencia 2)",
        help_text="Seleccione la materia que quiera cursar en 2do lugar.<br>"
                  "Cusará dos materias de las que se le asignen."
    )
    specific_subject2_order3 = forms.ChoiceField(
        choices=SPECIFIC_SUBJECT2_CHOICES,
        label="MATERIA ESPECÍFICA 2 (Preferencia 3)",
        help_text="Seleccione la materia que quiera cursar en 3er lugar.<br>"
                  "Cusará dos materias de las que se le asignen."
    )
    specific_subject2_order4 = forms.ChoiceField(
        choices=SPECIFIC_SUBJECT2_CHOICES,
        label="MATERIA ESPECÍFICA 2 (Preferencia 4)",
        help_text="Seleccione la materia que quiera cursar en 4º lugar.<br>"
                  "Cusará dos materias de las que se le asignen."
    )
    specific_subject2_order5 = forms.ChoiceField(
        choices=SPECIFIC_SUBJECT2_CHOICES,
        label="MATERIA ESPECÍFICA 2 (Preferencia 5)",
        help_text="Seleccione la materia que quiera cursar en 5º lugar.<br>"
                  "Cusará dos materias de las que se le asignen."
    )
    specific_subject2_order6 = forms.ChoiceField(
        choices=SPECIFIC_SUBJECT2_CHOICES,
        label="MATERIA ESPECÍFICA 2 (Preferencia 6)",
        help_text="Seleccione la materia que quiera cursar en 6º lugar.<br>"
                  "Cusará dos materias de las que se le asignen."
    )
    specific_subject2_order7 = forms.ChoiceField(
        choices=SPECIFIC_SUBJECT2_CHOICES,
        label="MATERIA ESPECÍFICA 2 (Preferencia 7)",
        help_text="Seleccione la materia que quiera cursar en 7º lugar.<br>"
                  "Cusará dos materias de las que se le asignen."
    )
    specific_subject2_order8 = forms.ChoiceField(
        choices=SPECIFIC_SUBJECT2_CHOICES,
        label="MATERIA ESPECÍFICA 2 (Preferencia 8)",
        help_text="Seleccione la materia que quiera cursar en 8º lugar.<br>"
                  "Cusará dos materias de las que se le asignen."
    )
    specific_subject2_order9 = forms.ChoiceField(
        choices=SPECIFIC_SUBJECT2_CHOICES,
        label="MATERIA ESPECÍFICA 2 (Preferencia 9)",
        help_text="Seleccione la materia que quiera cursar en 9º lugar.<br>"
                  "Cusará dos materias de las que se le asignen."
    )
    specific_subject2_order10 = forms.ChoiceField(
        choices=SPECIFIC_SUBJECT2_CHOICES,
        label="MATERIA ESPECÍFICA 2 (Preferencia 10)",
        help_text="Seleccione la materia que quiera cursar en 10º lugar.<br>"
                  "Cusará dos materias de las que se le asignen."
    )

    def clean(self):
        cleaned_data = super(AcademicForm_4ESO, self).clean()
        specific_subjects2 = []
        for i in range(1, 11):
            field = "specific_subject2_order{}".format(i)
            value = cleaned_data.get(field)
            if value in specific_subjects2:
                self.add_error(
                    field,
                    "Materia repetida. Por favor, seleccione otra"
                )
            else:
                specific_subjects2.append(value)


class AcademicForm_4ESO_EAC(forms.Form):
    CORE_SUBJECTS_CHOICES = sorted((
        ("BIG+FYQ", "Biología y Geología + Física y Química"),
        ("ECO+LAT", "Economía + Latín")),
        key=lambda x: x[1]
    )

    core_subjects = forms.ChoiceField(
        choices=CORE_SUBJECTS_CHOICES,
        label="TRONCALES DE OPCIÓN"
    )


class AcademicForm_4ESO_EAP(forms.Form):
    CORE_SUBJECTS_CHOICES = sorted((
        ("CIE+IVY", "Ciencias aplicadas a la actividad profesional + "
                    "Iniciación a la actividad emprendedora y empresarial"),
        ("CIE+TEE", "Ciencias aplicadas a la actividad profesional + "
                    "Tecnología"),
        ("IVY+TEE", "Iniciación a la actividad emprendedora y empresarial "
                    "Tecnología")),
        key=lambda x: x[1]
    )

    core_subjects = forms.ChoiceField(
        choices=CORE_SUBJECTS_CHOICES,
        label="TRONCALES DE OPCIÓN"
    )
