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
