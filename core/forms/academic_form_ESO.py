from django import forms


class AcademicForm_ESO(forms.Form):
    SPECIFIC_SUBJECT1_CHOICES = sorted((
        ("RLG", "Religión"),
        ("VAO", "Valores éticos")),
        key=lambda x: x[1]
    )
    SPECIFIC_SUBJECT2_CHOICES = sorted((
        ("SGA", "Alemán"),
        ("SGN", "Francés")),
        key=lambda x: x[1]
    )

    specific_subject1 = forms.ChoiceField(
        choices=SPECIFIC_SUBJECT1_CHOICES,
        label="MATERIA ESPECÍFICA 1",
    )
    specific_subject2 = forms.ChoiceField(
        choices=SPECIFIC_SUBJECT2_CHOICES,
        label="MATERIA ESPECÍFICA 2",
        help_text="Debe tener continuidad con la optativa elegida el curso "
                  "anterior"
    )
