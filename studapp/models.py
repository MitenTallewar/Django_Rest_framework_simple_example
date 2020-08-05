from django.db import models
from django.core.validators import EmailValidator
# Create your models here.
class Student(models.Model):
    name = models.CharField('Stud_name',max_length=50)
    age = models.IntegerField('Age')
    contact_no = models.BigIntegerField('mobile')
    email = models.EmailField('Email Id')
