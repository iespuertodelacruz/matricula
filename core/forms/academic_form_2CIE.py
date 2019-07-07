from django import forms

from .bachillerato_subjects import SUBJECTS


class AcademicForm_2CIE(forms.Form):
    TRAINING_ITINERARY_CHOICES = sorted((
        ("CCS", "Ciencias de la Salud"),
        ("TEC", "Científico-Tecnológico")),
        key=lambda x: x[1]
    )
    SPECIFIC_SUBJECT1_CHOICES = sorted(
        SUBJECTS['2BACH']['Libre configuración autonómica'],
        key=lambda x: x[1]
    )

    training_itinerary = forms.ChoiceField(
        choices=TRAINING_ITINERARY_CHOICES,
        label="ITINERARIO",
        help_text="Sería deseable continuar con el itinerario de primer curso"
    )
    specific_subject1_order1 = forms.ChoiceField(
        choices=SPECIFIC_SUBJECT1_CHOICES,
        label="MATERIA ESPECÍFICA 1 (Preferencia 1)",
        help_text="Seleccione la materia que quiera cursar en 1er lugar"
    )
    specific_subject1_order2 = forms.ChoiceField(
        choices=SPECIFIC_SUBJECT1_CHOICES,
        label="MATERIA ESPECÍFICA 1 (Preferencia 2)",
        help_text="Seleccione la materia que quiera cursar en 2do lugar"
    )
    specific_subject1_order3 = forms.ChoiceField(
        choices=SPECIFIC_SUBJECT1_CHOICES,
        label="MATERIA ESPECÍFICA 1 (Preferencia 3)",
        help_text="Seleccione la materia que quiera cursar en 3er lugar"
    )
    specific_subject1_order4 = forms.ChoiceField(
        choices=SPECIFIC_SUBJECT1_CHOICES,
        label="MATERIA ESPECÍFICA 1 (Preferencia 4)",
        help_text="Seleccione la materia que quiera cursar en 4º lugar"
    )
    specific_subject1_order5 = forms.ChoiceField(
        choices=SPECIFIC_SUBJECT1_CHOICES,
        label="MATERIA ESPECÍFICA 1 (Preferencia 5)",
        help_text="Seleccione la materia que quiera cursar en 5º lugar"
    )
    specific_subject1_order6 = forms.ChoiceField(
        choices=SPECIFIC_SUBJECT1_CHOICES,
        label="MATERIA ESPECÍFICA 1 (Preferencia 6)",
        help_text="Seleccione la materia que quiera cursar en 6º lugar"
    )
    specific_subject1_order7 = forms.ChoiceField(
        choices=SPECIFIC_SUBJECT1_CHOICES,
        label="MATERIA ESPECÍFICA 1 (Preferencia 7)",
        help_text="Seleccione la materia que quiera cursar en 7º lugar"
    )
    specific_subject1_order8 = forms.ChoiceField(
        choices=SPECIFIC_SUBJECT1_CHOICES,
        label="MATERIA ESPECÍFICA 1 (Preferencia 8)",
        help_text="Seleccione la materia que quiera cursar en 8º lugar"
    )
    specific_subject1_order9 = forms.ChoiceField(
        choices=SPECIFIC_SUBJECT1_CHOICES,
        label="MATERIA ESPECÍFICA 1 (Preferencia 9)",
        help_text="Seleccione la materia que quiera cursar en 9º lugar"
    )
    specific_subject1_order10 = forms.ChoiceField(
        choices=SPECIFIC_SUBJECT1_CHOICES,
        label="MATERIA ESPECÍFICA 1 (Preferencia 10)",
        help_text="Seleccione la materia que quiera cursar en 10º lugar"
    )

    def clean(self):
        cleaned_data = super(AcademicForm_2CIE, self).clean()
        specific_subjects1 = []
        for i in range(1, 11):
            field = "specific_subject1_order{}".format(i)
            value = cleaned_data.get(field)
            if value in specific_subjects1:
                self.add_error(
                    field,
                    "Materia repetida. Por favor, seleccione otra"
                )
            else:
                specific_subjects1.append(value)


class AcademicForm_2CIE_CCS(forms.Form):
    CORE_SUBJECT_CHOICES = sorted((
        ("GEO", "Geología"),
        ("QUI", "Química")),
        key=lambda x: x[1]
    )
    SPECIFIC_SUBJECT2_CHOICES = sorted(
        SUBJECTS['2CIE']['Materia específica'],
        key=lambda x: x[1]
    )

    core_subject_order1 = forms.ChoiceField(
        choices=CORE_SUBJECT_CHOICES,
        label="MATERIA TRONCAL DE OPCIÓN (Preferencia 1)",
        help_text="Seleccione la materia que quiera cursar en 1er lugar"
    )
    core_subject_order2 = forms.ChoiceField(
        choices=CORE_SUBJECT_CHOICES,
        label="MATERIA TRONCAL DE OPCIÓN (Preferencia 2)",
        help_text="Seleccione la materia que quiera cursar en 2do lugar"
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

    def clean(self):
        cleaned_data = super(AcademicForm_2CIE_CCS, self).clean()

        core_subjects = []
        for i in range(1, 3):
            field = "core_subject_order{}".format(i)
            value = cleaned_data.get(field)
            if value in core_subjects:
                self.add_error(
                    field,
                    "Materia repetida. Por favor, seleccione otra"
                )
            else:
                core_subjects.append(value)

        specific_subjects2 = []
        for i in range(1, 9):
            field = "specific_subject2_order{}".format(i)
            value = cleaned_data.get(field)
            if value in specific_subjects2:
                self.add_error(
                    field,
                    "Materia repetida. Por favor, seleccione otra"
                )
            else:
                specific_subjects2.append(value)


class AcademicForm_2CIE_TEC(forms.Form):
    CORE_SUBJECT_CHOICES = sorted((
        ("DBC", "Dibujo Técnico II"),
        ("QUI", "Química")),
        key=lambda x: x[1]
    )
    SPECIFIC_SUBJECT2_CHOICES = sorted(
        SUBJECTS['2CIE']['Materia específica'],
        key=lambda x: x[1]
    )

    core_subject_order1 = forms.ChoiceField(
        choices=CORE_SUBJECT_CHOICES,
        label="MATERIA TRONCAL DE OPCIÓN (Preferencia 1)",
        help_text="Seleccione la materia que quiera cursar en 1er lugar"
    )
    core_subject_order2 = forms.ChoiceField(
        choices=CORE_SUBJECT_CHOICES,
        label="MATERIA TRONCAL DE OPCIÓN (Preferencia 2)",
        help_text="Seleccione la materia que quiera cursar en 2do lugar"
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

    def clean(self):
        cleaned_data = super(AcademicForm_2CIE_TEC, self).clean()

        core_subjects = []
        for i in range(1, 3):
            field = "core_subject_order{}".format(i)
            value = cleaned_data.get(field)
            if value in core_subjects:
                self.add_error(
                    field,
                    "Materia repetida. Por favor, seleccione otra"
                )
            else:
                core_subjects.append(value)

        specific_subjects2 = []
        for i in range(1, 9):
            field = "specific_subject2_order{}".format(i)
            value = cleaned_data.get(field)
            if value in specific_subjects2:
                self.add_error(
                    field,
                    "Materia repetida. Por favor, seleccione otra"
                )
            else:
                specific_subjects2.append(value)
