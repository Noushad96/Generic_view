from django.db import models

# Create your models here.

class Student(models.Model):
    objects = None
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=18)
    father_name = models.CharField(max_length=200)

    def __str__(self):
        return self.name