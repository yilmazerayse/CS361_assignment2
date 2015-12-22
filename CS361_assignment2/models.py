__author__ = 'ayseyilmazer'

from django.db import models



class Course(models.Model):
     name = models.CharField(max_length=20)
     code = models.CharField(max_length=5)
     classroom = models.CharField(max_length=10)
     times = models.DateField()
     students = models.ManyToManyField(Student) #ManyToManyField accepts an extra set of arguments – all optional – that control how the relationship functions
     teachers = models.ForeignKey(Teacher) #ForeignKey many-to-one relationship. Requires a positional argument: the class to which the model is related.

class Teacher(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    office = models.CharField(max_length=30)
    phone = models.IntegerField()
    email = models.EmailField()

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()



