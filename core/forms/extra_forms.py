from django import forms


class ExtraForm(forms.Form):

    has_health_problem = forms.BooleanField(
        required=False,
        label="El alumno/a presenta problemas de salud",
        help_text="""
Marcar en caso de que el alumno/a sufra cualquier tipo de patología o problema
de salud reseñable, que deba ser informada al centro.
        """
    )
    health_problem = forms.CharField(
        required=False,
        label="Descripción de los problemas de salud del alumno/a",
        widget=forms.Textarea
    )
    auth_image_use = forms.BooleanField(
        required=False,
        initial=True,
        label="Autoriza el uso de la imagen del alumno/a",
        help_text="""
            Autoriza que la imagen del alumno/a sea publicada en papel
            o por medios electrónicos con el fin de difundir o promocionar
            las enseñanzas o actividades realizadas por el centro durante
            el curso escolar.
        """
    )
    non_simultaneous_studies = forms.BooleanField(
        required=True,
        initial=True,
        label="Declaración jurada de no simultanear estudios",
        help_text="""
            Juro/Declaro bajo mi responsabilidad que no voy a simultanear
            estudios, en régimen oficial y a tiempo completo, salvo que se
            trate de enseñanzas de música, danza, enseñanzas profesionales
            de artes plásticas y diseño, enseñanzas oficiales de idioma o
            enseñanzas deportivas. A estos efectos, los estudios universitarios
            a curso completo también se consideran enseñanzas postobligatorias.
        """
    )
    ampa = forms.BooleanField(
        required=False,
        label="Solicito la inscripción en el AMPA",
        help_text="""
        Solicito a la Asociación de Padres y Madres de Alumnos (AMPA) del
        IES Puerto de la Cruz - Telesforo Bravo mi inscripción commo socio para
        el presente curso escolar y beneficiarme así de los descuentos en las
        actividades extraescolares y demás actividades que organice el AMPA.
        Cuota anual 13€.
        """
    )
    books_loan = forms.BooleanField(
        required=False,
        label="Solicito participar en el proyecto de préstamo de libros "
              "del centro",
        help_text="""
            Sólo podrán presentar esta solicitud aquellas familias cuyos
            ingresos totales de la declaración del IRPF del ejercicio fiscal
            2015 no superan unas determinadas cantidades. <a target="blank"
            href="">Ver información sobre préstamo de libros</a>
        """
    )

    def clean(self):
        cleaned_data = super(ExtraForm, self).clean()
        has_health_problem = cleaned_data.get("has_health_problem")
        health_problem = cleaned_data.get("health_problem").strip()
        if has_health_problem and not health_problem:
            self.add_error(
                "health_problem",
                """Ha indicado que el alumno/a presenta algún problema de
                salud. Debe especificar los mismos en este apartado."""
            )
        if health_problem and not has_health_problem:
            self.add_error(
                "has_health_problem",
                """Ha especificado ciertos problemas de salud del alumno/a.
                Por lo tanto, debería marcar esta opción."""
            )
