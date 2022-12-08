from django.db import models

# Create your models here.
from django.contrib.auth.models import User

from django.db.models.deletion import CASCADE


class EmployeeModel(models.Model):
    owner = models.ForeignKey(User,related_name="employee", null=True, on_delete=CASCADE)
    name = models.CharField(max_length=100,null=True)
    department = models.CharField(max_length=100,null=True)
    designation = models.CharField(max_length=100 ,null=True)
    phonenumber = models.CharField(max_length=10,null=True)

    def __str__(self):
         return self.name



