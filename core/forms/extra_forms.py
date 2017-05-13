from django import forms


class ExtraForm(forms.Form):
    auth_image_use = forms.BooleanField(
        required=False,
        initial=True,
        label="Se autoriza el uso de la imagen del alumno/a",
        help_text="""
            Se autoriza que la imagen del alumno/a sea publicada en papel
            o por medios electrónicos con el fin de difundir o promocionar
            las enseñanzas o actividades realizadas por el centro durante
            el curso escolar.
        """
    )
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
