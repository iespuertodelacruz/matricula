import datetime

from django.db import models


class EduLevel(models.Model):
    code = models.CharField(max_length=32)
    law = models.CharField(max_length=32)
    description = models.CharField(max_length=256)
    enrollment_date = models.DateField(blank=True, null=True)
    order = models.SmallIntegerField()
    cost = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = "Nivel educativo"
        verbose_name_plural = "Niveles educativos"
        ordering = ["order", "code"]

    def enrollment_payment_doc(self):
        return f"enrollment_payment_{self.cost}.pdf"

    def is_vocational_training(self):
        return self.code[1:] in ["CFGM", "CFGS"]

    def is_ESO(self):
        return self.code[1:] == "ESO" or self.code[-4::] == "PMAR"

    def is_mandatory(self):
        return self.is_ESO()

    def is_bachillerato(self):
        return self.code[1:] in ["CIE", "SOC"]

    def allow_multi_enrollment(self):
        return self.is_ESO() or self.code in ["1CIE", "1SOC"]

    @staticmethod
    def empty_all_enrollment_dates():
        return len(EduLevel.objects.filter(enrollment_date__isnull=False)) == 0

    def is_first_course(self):
        return self.code[0] == "1"

    def is_FPB(self):
        return self.code[1:] == "FPB"


class Config(models.Model):
    regular_enroll_start_date = models.DateField(
        verbose_name='Fecha de comienzo de matrícula ordinaria')
    regular_enroll_end_date = models.DateField(
        verbose_name='Fecha de finalización de matrícula ordinaria')
    exist_ampa = models.BooleanField(verbose_name='¿Existe AMPA?')

    def __str__(self):
        return 'Configuración general de la aplicación'

    def is_regular_enroll_period(self):
        today = datetime.date.today()
        return self.regular_enroll_start_date <= \
            today <= \
            self.regular_enroll_end_date

    def get_schoolyear(self):
        today = datetime.date.today()
        if today >= self.regular_enroll_start_date:
            ref_year = today.year
        else:
            ref_year = today.year - 1
        return "{}/{}".format(ref_year, ref_year+1)
