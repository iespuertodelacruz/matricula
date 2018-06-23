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
    remarks = forms.CharField(
        label="OBSERVACIONES / MÓDULOS A REPETIR",
        help_text="Indique aspectos específicos a tener en cuenta en su "
                  "matrícula. También explique los detalles en caso de haber "
                  "marcado 'Otras situaciones' en el método de acceso.",
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
        ("ESO", "Graduado en ESO o equivalente"),
        ("PCP", "Con los módulos obligatorios de PCPI superados"),
        ("PAC", "Prueba de acceso a ciclo formativo de grado medio"),
        ("EXT", "Convalidación/Homologación de estudios extranjeros"),
        ("BAC", "Bachillerato"),
        ("FPB", "Formación Profesional Básica"),
        ("UNI", "Con titulación universitaria"),
        ("OTR", "Otras situaciones")
    )

    access_via = forms.ChoiceField(
        choices=ACCESS_VIA_CHOICES,
        label="MÉTODO DE ACCESO"
    )


class AcademicForm_Access_CFGS(forms.Form):
    # http://todofp.es/todofp/sobre-fp/informacion-general/
    # sistema-educativo-fp/como-accedo.html
    ACCESS_VIA_CHOICES = (
        ("BAC", "Bachillerato o equivalente"),
        ("PAC", "Prueba de acceso a ciclo formativo de grado superior"),
        ("EXT", "Convalidación/Homologación de estudios extranjeros"),
        ("UNI", "Con titulación universitaria"),
        ("TFP", "Con título de Técnico de Formación Profesional"),
        ("OTR", "Otras situaciones")
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
