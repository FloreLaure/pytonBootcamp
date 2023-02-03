from django.db import models
from datetime import datetime, date
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phonenumber = PhoneNumberField(null=True)
    address1 = models.CharField(max_length=30)
    address2 = models.CharField(max_length=30)
    country = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.first_name}{self.last_name}'


class Vehicle_Type(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name}'


class Vehicle_Size(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name}'

class Vehicle(models.Model):
    vehicle_type = models.ForeignKey(Vehicle_Type,null=True, blank=True,on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)
    real_cost = models.FloatField()
    size = models.ForeignKey(Vehicle_Size, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.vehicle_type}---{self.size}'


class Rental(models.Model):
    rental = models.CharField(max_length=30)
    retour = models.DateField()
    customer = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.rental}'


class Rental_Rate(models.Model):
    daily_rate = models.CharField(max_length=30)
    vehicle_type = models.ForeignKey(Vehicle_Type, null=True, blank=True, on_delete=models.CASCADE)
    vehicle_size = models.ForeignKey(Vehicle_Size, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.daily_rate}'

