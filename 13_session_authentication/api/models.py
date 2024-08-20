from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)
    ship = models.CharField(max_length=100)
