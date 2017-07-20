from django import forms


class AcademicForm_1CIE(forms.Form):
    TRAINING_ITINERARY_CHOICES = sorted((
        ("CCS", "Ciencias de la Salud"),
        ("TEC", "Científico-Tecnológico")),
        key=lambda x: x[1]
    )
    SPECIFIC_SUBJECT1_CHOICES = sorted((
        ("RLG", "Religión"),
        ("TFY", "Tecnologías de la información y la comunicación")),
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


class AcademicForm_1CIE_CCS(forms.Form):
    SPECIFIC_SUBJECT2_CHOICES = sorted((
        ("CUF", "Cultura científica"),
        ("SGG", "Francés"),
        ("SGT", "Alemán"),
        ("TNI", "Tecnología Industrial I")),
        key=lambda x: x[1]
    )

    specific_subject2_order1 = forms.ChoiceField(
        choices=SPECIFIC_SUBJECT2_CHOICES,
        label="MATERIA ESPECÍFICA 2 (Preferencia 1)",
        help_text="Seleccione la materia que quiera cursar en 1er lugar"
    )
    specific_subject2_order2 = forms.ChoiceField(
        choices=SPECIFIC_SUBJECT2_CHOICES,
        label="MATERIA ESPECÍFICA 2 (Preferencia 2)",
        help_text="Seleccione la materia que quiera cursar en 2do lugar"
    )
    specific_subject2_order3 = forms.ChoiceField(
        choices=SPECIFIC_SUBJECT2_CHOICES,
        label="MATERIA ESPECÍFICA 2 (Preferencia 3)",
        help_text="Seleccione la materia que quiera cursar en 3er lugar"
    )
    specific_subject2_order4 = forms.ChoiceField(
        choices=SPECIFIC_SUBJECT2_CHOICES,
        label="MATERIA ESPECÍFICA 2 (Preferencia 4)",
        help_text="Seleccione la materia que quiera cursar en 4º lugar"
    )

    def clean(self):
        cleaned_data = super(AcademicForm_1CIE_CCS, self).clean()
        specific_subjects2 = []
        for i in range(1, 5):
            field = "specific_subject2_order{}".format(i)
            value = cleaned_data.get(field)
            if value in specific_subjects2:
                self.add_error(
                    field,
                    "Materia repetida. Por favor, seleccione otra"
                )
            else:
                specific_subjects2.append(value)


class AcademicForm_1CIE_TEC(forms.Form):
    SPECIFIC_SUBJECT2_CHOICES = sorted((
        ("CUF", "Cultura científica"),
        ("SGG", "Francés"),
        ("SGT", "Alemán"),
        ("TNI", "Tecnología Industrial I")),
        key=lambda x: x[1]
    )

    specific_subject2_order1 = forms.ChoiceField(
        choices=SPECIFIC_SUBJECT2_CHOICES,
        label="MATERIA ESPECÍFICA 2 (Preferencia 1)",
        help_text="Seleccione la materia que quiera cursar en 1er lugar"
    )
    specific_subject2_order2 = forms.ChoiceField(
        choices=SPECIFIC_SUBJECT2_CHOICES,
        label="MATERIA ESPECÍFICA 2 (Preferencia 2)",
        help_text="Seleccione la materia que quiera cursar en 2do lugar"
    )
    specific_subject2_order3 = forms.ChoiceField(
        choices=SPECIFIC_SUBJECT2_CHOICES,
        label="MATERIA ESPECÍFICA 2 (Preferencia 3)",
        help_text="Seleccione la materia que quiera cursar en 3er lugar"
    )
    specific_subject2_order4 = forms.ChoiceField(
        choices=SPECIFIC_SUBJECT2_CHOICES,
        label="MATERIA ESPECÍFICA 2 (Preferencia 4)",
        help_text="Seleccione la materia que quiera cursar en 4º lugar"
    )

    def clean(self):
        cleaned_data = super(AcademicForm_1CIE_TEC, self).clean()
        specific_subjects2 = []
        for i in range(1, 5):
            field = "specific_subject2_order{}".format(i)
            value = cleaned_data.get(field)
            if value in specific_subjects2:
                self.add_error(
                    field,
                    "Materia repetida. Por favor, seleccione otra"
                )
            else:
                specific_subjects2.append(value)
