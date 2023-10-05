from django.db import models

# Create your models here.
class Student(models.Model):
    sname =models.CharField(max_length=20)
    sage = models.IntegerField()
    email = models.EmailField()
    def __str__(self):
        return self.sname