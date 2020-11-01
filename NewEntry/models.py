from django.db import models


# Create your models here.


class Student(models.Model):
    stud_id = models.IntegerField()
    name = models.CharField(max_length=100)
    year = models.CharField(max_length=10)
    contact = models.BigIntegerField()
    email = models.EmailField(max_length=50)
    room = models.PositiveSmallIntegerField()
    parents_name = models.CharField(max_length=100)
    parents_contact = models.BigIntegerField()
    parents_email = models.EmailField(max_length=50)


