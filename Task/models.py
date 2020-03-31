from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    mark_one = models.CharField(max_length=50)
    mark_two = models.CharField(max_length=50)
    mark_three = models.CharField(max_length=50)
    rank = models.CharField(max_length=50)
    total = models.IntegerField()

    def __str__(self):
        return self.name

