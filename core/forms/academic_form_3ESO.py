from django import forms


class AcademicForm_3ESO(forms.Form):
    core_subject = forms.ChoiceField(
        choices=(
            ("SAA", "Matemáticas orientadas a las enseñanzas académicas"),
            ("MMZ", "Matemáticas orientadas a las enseñanzas aplicadas"),
        ),
        label="Materia troncal",
        help_text="Debe tener continuidad con la optativa elegida el curso "
                  "anterior"
    )
    specific_subject1 = forms.ChoiceField(
        choices=(
            ("RLG", "Religión"),
            ("VAO", "Valores éticos"),
        ),
        label="Materia específica 1",
        help_text="Debe tener continuidad con la optativa elegida el curso "
                  "anterior"
    )
    specific_subject2 = forms.ChoiceField(
        choices=(
            ("SGA", "Segunda Lengua Alemán"),
            ("SGN", "Segunda Lengua Francés"),
        ),
        label="Materia específica 2",
        help_text="Debe tener continuidad con la optativa elegida el curso "
                  "anterior"
    )
    specific_subject3_order1 = forms.ChoiceField(
        choices=(
            ("CUC", "Cultura Clásica"),
            ("MUS", "Música"),
            ("TEE", "Tecnología"),
            ("EUP", "Educación Plástica, Visual y Audiovisual"),
            ("IVY", "Iniciación a la actividad emprendedora y empresarial"),
        ),
        label="Materia específica 3 (PREFERENCIA 1)",
        help_text="Cursará 2 materias de 'Materia específica 3'. Seleccione "
                  " las materias según su preferencia.",
    )
    specific_subject3_order2 = forms.ChoiceField(
        choices=(
            ("CUC", "Cultura Clásica"),
            ("MUS", "Música"),
            ("TEE", "Tecnología"),
            ("EUP", "Educación Plástica, Visual y Audiovisual"),
            ("IVY", "Iniciación a la actividad emprendedora y empresarial"),
        ),
        label="Materia específica 3 (PREFERENCIA 2)",
        help_text="Cursará 2 materias de 'Materia específica 3'. Seleccione "
                  " las materias según su preferencia."
    )
    specific_subject3_order3 = forms.ChoiceField(
        choices=(
            ("CUC", "Cultura Clásica"),
            ("MUS", "Música"),
            ("TEE", "Tecnología"),
            ("EUP", "Educación Plástica, Visual y Audiovisual"),
            ("IVY", "Iniciación a la actividad emprendedora y empresarial"),
        ),
        label="Materia específica 3 (PREFERENCIA 3)",
        help_text="Cursará 2 materias de 'Materia específica 3'. Seleccione "
                  " las materias según su preferencia."
    )
    specific_subject3_order4 = forms.ChoiceField(
        choices=(
            ("CUC", "Cultura Clásica"),
            ("MUS", "Música"),
            ("TEE", "Tecnología"),
            ("EUP", "Educación Plástica, Visual y Audiovisual"),
            ("IVY", "Iniciación a la actividad emprendedora y empresarial"),
        ),
        label="Materia específica 3 (PREFERENCIA 4)",
        help_text="Cursará 2 materias de 'Materia específica 3'. Seleccione "
                  " las materias según su preferencia."
    )
    specific_subject3_order5 = forms.ChoiceField(
        choices=(
            ("CUC", "Cultura Clásica"),
            ("MUS", "Música"),
            ("TEE", "Tecnología"),
            ("EUP", "Educación Plástica, Visual y Audiovisual"),
            ("IVY", "Iniciación a la actividad emprendedora y empresarial"),
        ),
        label="Materia específica 3 (PREFERENCIA 5)",
        help_text="Cursará 2 materias de 'Materia específica 3'. Seleccione "
                  " las materias según su preferencia."
    )

    def clean(self):
        cleaned_data = super(AcademicForm_3ESO, self).clean()
        specific_subject3_order1 = cleaned_data.get("specific_subject3_order1")
        specific_subject3_order2 = cleaned_data.get("specific_subject3_order2")
        specific_subject3_order3 = cleaned_data.get("specific_subject3_order3")
        specific_subject3_order4 = cleaned_data.get("specific_subject3_order4")
        specific_subject3_order5 = cleaned_data.get("specific_subject3_order5")

        specific_subjects = set()
        specific_subjects.add(specific_subject3_order1)
        specific_subjects.add(specific_subject3_order2)
        specific_subjects.add(specific_subject3_order3)
        specific_subjects.add(specific_subject3_order4)
        specific_subjects.add(specific_subject3_order5)
        if len(specific_subjects) < 5:
            raise forms.ValidationError(
                "Las elecciones de la materia específica 3 no son correctas. "
                "Puede que haya repetido alguna materia"
            )
