from django import forms
from .academic_form_ESO import AcademicForm_ESO


class AcademicForm_3ESO(AcademicForm_ESO):
    CORE_SUBJECT_CHOICES = sorted((
        ("SAA", "Matemáticas orientadas a las enseñanzas académicas"),
        ("MMZ", "Matemáticas orientadas a las enseñanzas aplicadas")),
        key=lambda x: x[1]
    )
    SPECIFIC_SUBJECT3_CHOICES = sorted((
        ("CUC", "Cultura Clásica"),
        ("MUS", "Música"),
        ("TEE", "Tecnología"),
        ("EUP", "Educación Plástica, Visual y Audiovisual"),
        ("IVY", "Iniciación a la actividad emprendedora y empresarial")),
        key=lambda x: x[1]
    )

    core_subject = forms.ChoiceField(
        choices=CORE_SUBJECT_CHOICES,
        label="MATERIA TRONCAL",
    )
    specific_subject3_order1 = forms.ChoiceField(
        choices=SPECIFIC_SUBJECT3_CHOICES,
        label="MATERIA ESPECÍFICA 3 (Preferencia 1)",
        help_text="Seleccione la materia que quiera cursar en 1er lugar"
    )
    specific_subject3_order2 = forms.ChoiceField(
        choices=SPECIFIC_SUBJECT3_CHOICES,
        label="MATERIA ESPECÍFICA 3 (Preferencia 2)",
        help_text="Seleccione la materia que quiera cursar en 2do lugar"
    )
    specific_subject3_order3 = forms.ChoiceField(
        choices=SPECIFIC_SUBJECT3_CHOICES,
        label="MATERIA ESPECÍFICA 3 (Preferencia 3)",
        help_text="Seleccione la materia que quiera cursar en 3er lugar"
    )
    specific_subject3_order4 = forms.ChoiceField(
        choices=SPECIFIC_SUBJECT3_CHOICES,
        label="MATERIA ESPECÍFICA 3 (Preferencia 4)",
        help_text="Seleccione la materia que quiera cursar en 4º lugar"
    )
    specific_subject3_order5 = forms.ChoiceField(
        choices=SPECIFIC_SUBJECT3_CHOICES,
        label="MATERIA ESPECÍFICA 3 (Preferencia 5)",
        help_text="Seleccione la materia que quiera cursar en 5º lugar"
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
