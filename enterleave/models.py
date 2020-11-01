from django.db import models

# Create your models here.


class inout(models.Model):
    stud_id = models.IntegerField()
    IN = models.DateTimeField(null=True, blank=True)
    OUT = models.DateTimeField(null=True, blank=True)
