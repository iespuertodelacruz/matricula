from django import forms


class AcademicForm_3ESO(forms.Form):
    CORE_SUBJECT_CHOICES = (
        ("SAA", "Matemáticas orientadas a las enseñanzas académicas"),
        ("MMZ", "Matemáticas orientadas a las enseñanzas aplicadas"),
    )
    SPECIFIC_SUBJECT1_CHOICES = (
        ("RLG", "Religión"),
        ("VAO", "Valores éticos"),
    )
    SPECIFIC_SUBJECT2_CHOICES = (
        ("SGA", "Segunda Lengua Alemán"),
        ("SGN", "Segunda Lengua Francés"),
    )
    SPECIFIC_SUBJECT3_CHOICES = (
        ("CUC", "Cultura Clásica"),
        ("MUS", "Música"),
        ("TEE", "Tecnología"),
        ("EUP", "Educación Plástica, Visual y Audiovisual"),
        ("IVY", "Iniciación a la actividad emprendedora y empresarial"),
    )

    core_subject = forms.ChoiceField(
        choices=CORE_SUBJECT_CHOICES,
        label="Materia troncal",
        help_text="Debe tener continuidad con la optativa elegida el curso "
                  "anterior"
    )
    specific_subject1 = forms.ChoiceField(
        choices=SPECIFIC_SUBJECT1_CHOICES,
        label="Materia específica 1",
        help_text="Debe tener continuidad con la optativa elegida el curso "
                  "anterior"
    )
    specific_subject2 = forms.ChoiceField(
        choices=SPECIFIC_SUBJECT2_CHOICES,
        label="Materia específica 2",
        help_text="Debe tener continuidad con la optativa elegida el curso "
                  "anterior"
    )
    specific_subject3_order1 = forms.ChoiceField(
        choices=SPECIFIC_SUBJECT3_CHOICES,
        label="Materia específica 3 (PREFERENCIA 1)",
        help_text="Cursará 2 materias de 'Materia específica 3'. Seleccione "
                  " las materias según su preferencia.",
    )
    specific_subject3_order2 = forms.ChoiceField(
        choices=SPECIFIC_SUBJECT3_CHOICES,
        label="Materia específica 3 (PREFERENCIA 2)",
        help_text="Cursará 2 materias de 'Materia específica 3'. Seleccione "
                  " las materias según su preferencia."
    )
    specific_subject3_order3 = forms.ChoiceField(
        choices=SPECIFIC_SUBJECT3_CHOICES,
        label="Materia específica 3 (PREFERENCIA 3)",
        help_text="Cursará 2 materias de 'Materia específica 3'. Seleccione "
                  " las materias según su preferencia."
    )
    specific_subject3_order4 = forms.ChoiceField(
        choices=SPECIFIC_SUBJECT3_CHOICES,
        label="Materia específica 3 (PREFERENCIA 4)",
        help_text="Cursará 2 materias de 'Materia específica 3'. Seleccione "
                  " las materias según su preferencia."
    )
    specific_subject3_order5 = forms.ChoiceField(
        choices=SPECIFIC_SUBJECT3_CHOICES,
        label="Materia específica 3 (PREFERENCIA 5)",
        help_text="Cursará 2 materias de 'Materia específica 3'. Seleccione "
                  " las materias según su preferencia."
    )

    def clean(self):
        cleaned_data = super(AcademicForm_3ESO, self).clean()

        specific_subjects3 = []
        for i in range(1, 6):
            field = "specific_subject3_order{}".format(i)
            value = cleaned_data.get(field)
            if value in specific_subjects3:
                self.add_error(
                    field,
                    "Materia repetida. Por favor, seleccione otra"
                )
            else:
                specific_subjects3.append(value)
