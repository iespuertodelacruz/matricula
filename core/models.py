from django.db import models


class EducationLevel(models.Model):
    code = models.CharField(max_length=32)
    law = models.CharField(max_length=32)
    description = models.CharField(max_length=256)
    enrollment_date = models.DateField()

    def __str__(self):
        return self.code
