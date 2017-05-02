from django import forms


class AcademicForm_1SOC(forms.Form):
    TRAINING_ITINERARY_CHOICES = (
        ("HUM", "Humanidades"),
        ("SOC", "Sociales")
    )
    SPECIFIC_SUBJECT1_CHOICES = (
        ("RLG", "Religión"),
        ("TFY", "Tecnologías de la información y la comunicación")
    )

    training_itinerary = forms.ChoiceField(
        choices=TRAINING_ITINERARY_CHOICES,
        label="Itinerario",
    )
    specific_subject1 = forms.ChoiceField(
        choices=SPECIFIC_SUBJECT1_CHOICES,
        label="Materia específica 1",
    )


class AcademicForm_1SOC_HUM(forms.Form):
    CORE_SUBJECT_CHOICES = (
        ("GRI", "Griego I"),
        ("LIE", "Literatura Universal")
    )
    SPECIFIC_SUBJECT2_CHOICES = (
        ("CUF", "Cultura científica"),
        ("SGG", "Francés"),
        ("SGA", "Alemán"),
        ("ECO", "Economía"),
        ("DAI", "Dibujo Artístico I")
    )

    core_subject = forms.ChoiceField(
        choices=CORE_SUBJECT_CHOICES,
        label="Troncal de opción",
    )
    specific_subject2_order1 = forms.ChoiceField(
        choices=SPECIFIC_SUBJECT2_CHOICES,
        label="Materia específica 2 (PREFERENCIA 1)",
        help_text="Seleccione la materia que quiera cursar en 1er lugar"
    )
    specific_subject2_order2 = forms.ChoiceField(
        choices=SPECIFIC_SUBJECT2_CHOICES,
        label="Materia específica 2 (PREFERENCIA 2)",
        help_text="Seleccione la materia que quiera cursar en 2do lugar"
    )
    specific_subject2_order3 = forms.ChoiceField(
        choices=SPECIFIC_SUBJECT2_CHOICES,
        label="Materia específica 2 (PREFERENCIA 3)",
        help_text="Seleccione la materia que quiera cursar en 3er lugar"
    )
    specific_subject2_order4 = forms.ChoiceField(
        choices=SPECIFIC_SUBJECT2_CHOICES,
        label="Materia específica 2 (PREFERENCIA 4)",
        help_text="Seleccione la materia que quiera cursar en 4º lugar"
    )
    specific_subject2_order5 = forms.ChoiceField(
        choices=SPECIFIC_SUBJECT2_CHOICES,
        label="Materia específica 2 (PREFERENCIA 5)",
        help_text="Seleccione la materia que quiera cursar en 5º lugar"
    )

    def clean(self):
        cleaned_data = super(AcademicForm_1SOC_HUM, self).clean()
        specific_subjects2 = []
        for i in range(1, 6):
            field = "specific_subject2_order{}".format(i)
            value = cleaned_data.get(field)
            if value in specific_subjects2:
                self.add_error(
                    field,
                    "Materia repetida. Por favor, seleccione otra"
                )
            else:
                specific_subjects2.append(value)


class AcademicForm_1SOC_SOC(forms.Form):
    SPECIFIC_SUBJECT2_CHOICES = (
        ("CUF", "Cultura científica"),
        ("SGG", "Francés"),
        ("SGA", "Alemán"),
        ("ECO", "Economía"),
        ("GRI", "Griego I"),
        ("LIE", "Literatura Universal")
    )

    specific_subject2_order1 = forms.ChoiceField(
        choices=SPECIFIC_SUBJECT2_CHOICES,
        label="Materia específica 2 (PREFERENCIA 1)",
        help_text="Seleccione la materia que quiera cursar en 1er lugar"
    )
    specific_subject2_order2 = forms.ChoiceField(
        choices=SPECIFIC_SUBJECT2_CHOICES,
        label="Materia específica 2 (PREFERENCIA 2)",
        help_text="Seleccione la materia que quiera cursar en 2do lugar"
    )
    specific_subject2_order3 = forms.ChoiceField(
        choices=SPECIFIC_SUBJECT2_CHOICES,
        label="Materia específica 2 (PREFERENCIA 3)",
        help_text="Seleccione la materia que quiera cursar en 3er lugar"
    )
    specific_subject2_order4 = forms.ChoiceField(
        choices=SPECIFIC_SUBJECT2_CHOICES,
        label="Materia específica 2 (PREFERENCIA 4)",
        help_text="Seleccione la materia que quiera cursar en 4º lugar"
    )
    specific_subject2_order5 = forms.ChoiceField(
        choices=SPECIFIC_SUBJECT2_CHOICES,
        label="Materia específica 2 (PREFERENCIA 5)",
        help_text="Seleccione la materia que quiera cursar en 5º lugar"
    )
    specific_subject2_order6 = forms.ChoiceField(
        choices=SPECIFIC_SUBJECT2_CHOICES,
        label="Materia específica 2 (PREFERENCIA 6)",
        help_text="Seleccione la materia que quiera cursar en 6º lugar"
    )

    def clean(self):
        cleaned_data = super(AcademicForm_1SOC_SOC, self).clean()
        specific_subjects2 = []
        for i in range(1, 7):
            field = "specific_subject2_order{}".format(i)
            value = cleaned_data.get(field)
            if value in specific_subjects2:
                self.add_error(
                    field,
                    "Materia repetida. Por favor, seleccione otra"
                )
            else:
                specific_subjects2.append(value)
