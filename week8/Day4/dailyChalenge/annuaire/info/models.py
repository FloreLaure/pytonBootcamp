from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Persons(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=50, unique=True)
    phonenumber = PhoneNumberField(null=True)
    address = models.CharField(max_length=40)

    def __str__(self):
        return f'{self.name}'

    
   