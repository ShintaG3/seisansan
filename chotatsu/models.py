from django.db import models

class Chotatsu(models.Model):
    project_name        = models.CharField(max_length=128, null=True, blank=True)
    first_category      = models.CharField(max_length=128, null=True, blank=True)
    second_category     = models.CharField(max_length=128, null=True, blank=True)
    comment             = models.CharField(max_length=1000, null=True, blank=True)
    def __str__(self):
        return f"{self.project_name} {self.first_category}"
