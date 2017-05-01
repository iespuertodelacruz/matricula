from django import forms


class AcademicForm_4ESO(forms.Form):
    TRAINING_ITINERARY_CHOICES = (
        ("EAC", "Enseñanzas ACADÉMICAS para la iniciación al "
                "Bachillerato"),
        ("EAP", "Enseñanzas APLICADAS para la iniciación a la Formación "
                "Profesional")
    )
    SPECIFIC_SUBJECT1_CHOICES = (
        ("RLG", "Religión"),
        ("VAO", "Valores éticos")
    )
    SPECIFIC_SUBJECT2_CHOICES = (
        ("SGA", "Alemán"),
        ("AEZ", "Artes escénicas y danza"),
        ("CUF", "Cultura científica"),
        ("CUC", "Cultura clásica"),
        ("EPV", "Educación plástica, visual y audiovisual"),
        ("FIL", "Filosofía"),
        ("SGN", "Francés"),
        ("MUS", "Música"),
        ("TEE", "Tecnología"),
        ("TGD", "Informática")
    )
    ACADEMIC_CORE_SUBJECTS_CHOICES = (
        ("", "---"),
        ("BIG+FYQ", "Biología y Geología + Física y Química"),
        ("ECO+LAT", "Economía + Latín")
    )
    APPLIED_CORE_SUBJECTS_CHOICES = (
        ("", "---"),
        ("CIE+IVY", "Ciencias aplicadas a la actividad profesional + "
                    "Iniciación a la actividad emprendedora y empresarial"),
        ("CIE+TEE", "Ciencias aplicadas a la actividad profesional + "
                    "Tecnología"),
        ("IVY+TEE", "Iniciación a la actividad emprendedora y empresarial "
                    "Tecnología")
    )

    training_itinerary = forms.ChoiceField(
        choices=TRAINING_ITINERARY_CHOICES,
        label="Opción de enseñanzas",
    )
    academic_core_subjects = forms.ChoiceField(
        choices=ACADEMIC_CORE_SUBJECTS_CHOICES,
        label="Troncales de opción (para Enseñanzas Académicas)",
        help_text="Cumplimentar sólo en el caso de haber elegido "
                  "'Enseñanzas Académicas'",
        required=False
    )
    applied_core_subjects = forms.ChoiceField(
        choices=APPLIED_CORE_SUBJECTS_CHOICES,
        label="Troncales de opción (para Enseñanzas Aplicadas)",
        help_text="Cumplimentar sólo en el caso de haber elegido "
                  "'Enseñanzas Aplicadas'",
        required=False
    )
    specific_subject1 = forms.ChoiceField(
        choices=SPECIFIC_SUBJECT1_CHOICES,
        label="Materia específica 1",
        help_text="Debe tener continuidad con la optativa elegida el curso "
                  "anterior"
    )
    specific_subject2_order1 = forms.ChoiceField(
        choices=SPECIFIC_SUBJECT2_CHOICES,
        label="Materia específica 2 (PREFERENCIA 1)",
        help_text="Cursará 2 materias de 'Materia específica 3'. Seleccione "
                  " las materias según su preferencia.",
    )
    specific_subject2_order2 = forms.ChoiceField(
        choices=SPECIFIC_SUBJECT2_CHOICES,
        label="Materia específica 2 (PREFERENCIA 2)",
        help_text="Cursará 2 materias de 'Materia específica 3'. Seleccione "
                  " las materias según su preferencia.",
    )
    specific_subject2_order3 = forms.ChoiceField(
        choices=SPECIFIC_SUBJECT2_CHOICES,
        label="Materia específica 2 (PREFERENCIA 3)",
        help_text="Cursará 2 materias de 'Materia específica 3'. Seleccione "
                  " las materias según su preferencia.",
    )
    specific_subject2_order4 = forms.ChoiceField(
        choices=SPECIFIC_SUBJECT2_CHOICES,
        label="Materia específica 2 (PREFERENCIA 4)",
        help_text="Cursará 2 materias de 'Materia específica 3'. Seleccione "
                  " las materias según su preferencia.",
    )
    specific_subject2_order5 = forms.ChoiceField(
        choices=SPECIFIC_SUBJECT2_CHOICES,
        label="Materia específica 2 (PREFERENCIA 5)",
        help_text="Cursará 2 materias de 'Materia específica 3'. Seleccione "
                  " las materias según su preferencia.",
    )
    specific_subject2_order6 = forms.ChoiceField(
        choices=SPECIFIC_SUBJECT2_CHOICES,
        label="Materia específica 2 (PREFERENCIA 6)",
        help_text="Cursará 2 materias de 'Materia específica 3'. Seleccione "
                  " las materias según su preferencia.",
    )
    specific_subject2_order7 = forms.ChoiceField(
        choices=SPECIFIC_SUBJECT2_CHOICES,
        label="Materia específica 2 (PREFERENCIA 7)",
        help_text="Cursará 2 materias de 'Materia específica 3'. Seleccione "
                  " las materias según su preferencia.",
    )
    specific_subject2_order8 = forms.ChoiceField(
        choices=SPECIFIC_SUBJECT2_CHOICES,
        label="Materia específica 2 (PREFERENCIA 8)",
        help_text="Cursará 2 materias de 'Materia específica 3'. Seleccione "
                  " las materias según su preferencia.",
    )
    specific_subject2_order9 = forms.ChoiceField(
        choices=SPECIFIC_SUBJECT2_CHOICES,
        label="Materia específica 2 (PREFERENCIA 9)",
        help_text="Cursará 2 materias de 'Materia específica 3'. Seleccione "
                  " las materias según su preferencia.",
    )
    specific_subject2_order10 = forms.ChoiceField(
        choices=SPECIFIC_SUBJECT2_CHOICES,
        label="Materia específica 2 (PREFERENCIA 10)",
        help_text="Cursará 2 materias de 'Materia específica 3'. Seleccione "
                  " las materias según su preferencia.",
    )

    def clean(self):
        cleaned_data = super(AcademicForm_4ESO, self).clean()
        training_itinerary = cleaned_data.get("training_itinerary")
        academic_core_subjects = cleaned_data.get("academic_core_subjects")
        applied_core_subjects = cleaned_data.get("applied_core_subjects")

        if training_itinerary == "EAC" and not academic_core_subjects:
            self.add_error(
                "academic_core_subjects",
                "Debe seleccionar las troncales de opción"
            )

        if training_itinerary == "EAP" and not applied_core_subjects:
            self.add_error(
                "applied_core_subjects",
                "Debe seleccionar las troncales de opción"
            )

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
