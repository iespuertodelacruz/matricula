from django import forms


class AcademicForm_FPB(forms.Form):
    TOPIC_CHOICES = (
        ("FPB", "Electricidad y Electrónica"),
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


class AcademicForm_Access_CFGM(forms.Form):
    # http://todofp.es/todofp/sobre-fp/informacion-general/
    # sistema-educativo-fp/como-accedo.html
    ACCESS_VIA_CHOICES = (
        ("ESO", "Educación Secundaria Obligatoria"),
        ("FPB", "Formación Profesional Básica"),
        ("TEC", "Técnico, Técnico Auxiliar o equivalente"),
        ("BUP", "Segundo curso de BUP"),
        ("PAC", "Prueba de acceso a grado medio"),
        ("U25", "Prueba de acceso a la Universidad (>25)")
    )

    access_via = forms.ChoiceField(
        choices=ACCESS_VIA_CHOICES,
        label="MÉTODO DE ACCESO"
    )


class AcademicForm_Access_CFGS(forms.Form):
    # http://todofp.es/todofp/sobre-fp/informacion-general/
    # sistema-educativo-fp/como-accedo.html
    ACCESS_VIA_CHOICES = (
        ("BAC", "Bachillerato"),
        ("EXP", "Segundo curso de bachillerato experimental"),
        ("CGM", "Formación Profesional de Grado Medio"),
        ("TEC", "Técnico Superior, Técnico Expecialista o equivalente"),
        ("COU", "COU"),
        ("UNI", "Titulación Universitaria"),
        ("PAC", "Prueba de acceso a grado superior"),
        ("U25", "Prueba de acceso a la Universidad (>25)")
    )

    access_via = forms.ChoiceField(
        choices=ACCESS_VIA_CHOICES,
        label="MÉTODO DE ACCESO"
    )


class AcademicForm_1CFGM(
    AcademicForm_CF,
    AcademicForm_Access_CFGM,
    AcademicForm_CFGM
):
    pass


class AcademicForm_2CFGM(AcademicForm_CF, AcademicForm_CFGM):
    pass


class AcademicForm_1CFGS(
    AcademicForm_CF,
    AcademicForm_Access_CFGS,
    AcademicForm_CFGS
):
    pass


class AcademicForm_2CFGS(AcademicForm_CF, AcademicForm_CFGS):
    pass


class AcademicForm_3CFGS(AcademicForm_CF, AcademicForm_CFD):
    pass


def get_edulevel(edulevel_code, academic):
    topic = academic.get("topic")
    if topic:
        return edulevel_code[0] + topic
    else:
        return None
