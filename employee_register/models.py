from django.db import models

# Create your models here.

## For any model there will be a primary key which is automatically created by the django ORM. Its self it will be id ##

class Position(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=4)
    mobile = models.CharField(max_length=15)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    def __str__(self):
        return self.fullname

## on_delete=models.CASCADE means when we delete Position model data, also delete from Employee model ##