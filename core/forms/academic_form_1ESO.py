from django import forms


class AcademicForm_1ESO(forms.Form):
    SPECIFIC_SUBJECT1_CHOICES = (
        ("RLG", "Religión"),
        ("VAO", "Valores éticos"),
    )
    SPECIFIC_SUBJECT2_CHOICES = (
        ("SGA", "Segunda Lengua Alemán"),
        ("SGN", "Segunda Lengua Francés"),
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
