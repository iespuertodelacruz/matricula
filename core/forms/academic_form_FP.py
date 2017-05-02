from django import forms


class AcademicForm_FPB(forms.Form):
    TOPIC_CHOICES = (
        ("ELE", "Electricidad y Electrónica"),
    )

    topic = forms.ChoiceField(
        choices=TOPIC_CHOICES,
        label="ESPECIALIDAD",
    )


class AcademicForm_1FPB(AcademicForm_FPB):
    pass


class AcademicForm_2FPB(AcademicForm_FPB):
    pass


class AcademicForm_CF(forms.Form):
    repeating_subjects = forms.CharField(
        label="MÓDULOS A CURSAR NUEVAMENTE",
        help_text="Sólo en el caso de alumnado repetidor",
        widget=forms.Textarea,
        required=False
    )


class AcademicForm_1CF(forms.Form):
    ACCESS_VIA_CHOICES = (
        ("PAC", "Prueba de acceso"),
        ("FPB", "Formación Profesional Básica"),
        ("ESO", "Educación Secundaria Obligatoria"),
        ("OTR", "Otros"),
    )

    access_via = forms.ChoiceField(
        choices=ACCESS_VIA_CHOICES,
        label="MÉTODO DE ACCESO"
    )


class AcademicForm_CFGM(forms.Form):
    TOPIC_CHOICES = sorted((
        ("CAR", "Carrocería"),
        ("ELE", "Instalaciones eléctricas y automáticas"),
        ("TEL", "Instalaciones de telecomunicaciones")),
        key=lambda x: x[1]
    )

    topic = forms.ChoiceField(
        choices=TOPIC_CHOICES,
        label="ESPECIALIDAD",
    )


class AcademicForm_CFGS(forms.Form):
    TOPIC_CHOICES = sorted((
        ("ASR", "Administración de sistemas informáticos en red"),
        ("DAW", "Desarrollo de aplicaciones Web"),
        ("GIT", "Guía, información y asistencia turísticas"),
        ("ALO", "Gestión de alojamientos turísticos"),
        ("DAM", "Desarrollo de aplicaciones multiplataforma"),
        ("ARI", "Automatización y robótica industrial")),
        key=lambda x: x[1]
    )

    topic = forms.ChoiceField(
        choices=TOPIC_CHOICES,
        label="ESPECIALIDAD",
    )


class AcademicForm_CFD(forms.Form):
    TOPIC_CHOICES = (
        ("DAM", "Desarrollo de aplicaciones multiplataforma"),
    )

    topic = forms.ChoiceField(
        choices=TOPIC_CHOICES,
        label="ESPECIALIDAD",
    )


class AcademicForm_1CFGM(AcademicForm_CF, AcademicForm_1CF, AcademicForm_CFGM):
    pass


class AcademicForm_2CFGM(AcademicForm_CF, AcademicForm_CFGM):
    pass


class AcademicForm_1CFGS(AcademicForm_CF, AcademicForm_1CF, AcademicForm_CFGS):
    pass


class AcademicForm_2CFGS(AcademicForm_CF, AcademicForm_CFGS):
    pass


class AcademicForm_3CFGS(AcademicForm_CF, AcademicForm_CFD):
    pass
