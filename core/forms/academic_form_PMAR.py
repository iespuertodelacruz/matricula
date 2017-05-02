from django import forms


class AcademicForm_1PMAR(forms.Form):
    SPECIFIC_SUBJECT_CHOICES = sorted((
        ("RLG", "Religión"),
        ("VAO", "Valores éticos")),
        key=lambda x: x[1]
    )

    specific_subject = forms.ChoiceField(
        choices=SPECIFIC_SUBJECT_CHOICES,
        label="MATERIA ESPECÍFICA",
    )


class AcademicForm_2PMAR(forms.Form):
    SPECIFIC_SUBJECT1_CHOICES = sorted((
        ("RLG", "Religión"),
        ("VAO", "Valores éticos")),
        key=lambda x: x[1]
    )
    SPECIFIC_SUBJECT2_CHOICES = sorted((
        ("EUP", "Educación plástica, visual y audiovisual"),
        ("MUS", "Música"),
        ("IVY", "Iniciación a la actividad emprendedora y empresarial")),
        key=lambda x: x[1]
    )

    specific_subject1 = forms.ChoiceField(
        choices=SPECIFIC_SUBJECT1_CHOICES,
        label="MATERIA ESPECÍFICA 1",
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

    def clean(self):
        cleaned_data = super(AcademicForm_2PMAR, self).clean()
        specific_subjects2 = []
        for i in range(1, 4):
            field = "specific_subject2_order{}".format(i)
            value = cleaned_data.get(field)
            if value in specific_subjects2:
                self.add_error(
                    field,
                    "Materia repetida. Por favor, seleccione otra"
                )
            else:
                specific_subjects2.append(value)


class AcademicForm_PostPMAR(forms.Form):
    SPECIFIC_SUBJECT1_CHOICES = sorted((
        ("RLG", "Religión"),
        ("VAO", "Valores éticos")),
        key=lambda x: x[1]
    )
    SPECIFIC_SUBJECT2_CHOICES = sorted((
        ("SGA", "Alemán"),
        ("AEZ", "Artes escénicas y danza"),
        ("CUF", "Cultura científica"),
        ("CUC", "Cultura clásica"),
        ("EPV", "Educación plástica, visual y audiovisual"),
        ("FIL", "Filosofía"),
        ("SGN", "Francés"),
        ("MUS", "Música"),
        ("TEE", "Tecnología"),
        ("TGD", "Informática")),
        key=lambda x: x[1]
    )
    CORE_SUBJECTS_CHOICES = (
        ("CIE+IVY", "Ciencias aplicadas a la actividad profesional + "
                    "Iniciación a la actividad emprendedora y empresarial"),
        ("CIE+TEE", "Ciencias aplicadas a la actividad profesional + "
                    "Tecnología"),
        ("IVY+TEE", "Iniciación a la actividad emprendedora y empresarial "
                    "Tecnología")
    )

    core_subjects = forms.ChoiceField(
        choices=CORE_SUBJECTS_CHOICES,
        label="TRONCALES DE OPCIÓN (Enseñanzas Aplicadas)"
    )
    specific_subject1 = forms.ChoiceField(
        choices=SPECIFIC_SUBJECT1_CHOICES,
        label="MATERIA ESPECÍFICA 1",
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
    specific_subject2_order5 = forms.ChoiceField(
        choices=SPECIFIC_SUBJECT2_CHOICES,
        label="MATERIA ESPECÍFICA 2 (Preferencia 5)",
        help_text="Seleccione la materia que quiera cursar en 5º lugar"
    )
    specific_subject2_order6 = forms.ChoiceField(
        choices=SPECIFIC_SUBJECT2_CHOICES,
        label="MATERIA ESPECÍFICA 2 (Preferencia 6)",
        help_text="Seleccione la materia que quiera cursar en 6º lugar"
    )
    specific_subject2_order7 = forms.ChoiceField(
        choices=SPECIFIC_SUBJECT2_CHOICES,
        label="MATERIA ESPECÍFICA 2 (Preferencia 7)",
        help_text="Seleccione la materia que quiera cursar en 7º lugar"
    )
    specific_subject2_order8 = forms.ChoiceField(
        choices=SPECIFIC_SUBJECT2_CHOICES,
        label="MATERIA ESPECÍFICA 2 (Preferencia 8)",
        help_text="Seleccione la materia que quiera cursar en 8º lugar"
    )
    specific_subject2_order9 = forms.ChoiceField(
        choices=SPECIFIC_SUBJECT2_CHOICES,
        label="MATERIA ESPECÍFICA 2 (Preferencia 9)",
        help_text="Seleccione la materia que quiera cursar en 9º lugar"
    )
    specific_subject2_order10 = forms.ChoiceField(
        choices=SPECIFIC_SUBJECT2_CHOICES,
        label="MATERIA ESPECÍFICA 2 (Preferencia 10)",
        help_text="Seleccione la materia que quiera cursar en 10º lugar"
    )

    def clean(self):
        cleaned_data = super(AcademicForm_PostPMAR, self).clean()
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
