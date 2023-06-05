from django.db import models
# from rest_framework import serializers



class Student(models.Model):
    name =models.CharField(max_length=20)
    roll =models.IntegerField()
    city = models.CharField(max_length=20)


# class Teacher(models.Model):
#     name =models.CharField(max_length=20)
#     subject =models.CharField(max_length=20)
#     salary =models.IntegerField()
#     city = models.CharField(max_length=20)

  
    