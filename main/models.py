from django.db import models

class Hospital(models.Model):
    class Meta:
        verbose_name_plural = 'Hospitals'
        verbose_name = 'Hospital'
        ordering = ['name']

    name = models.CharField(max_length=100)
    