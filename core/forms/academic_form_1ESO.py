from django import forms


class AcademicForm_1ESO(forms.Form):
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
