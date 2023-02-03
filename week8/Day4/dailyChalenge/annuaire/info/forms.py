from django import forms
from .models import Persons
from phonenumber_field.formfields import PhoneNumberField


class ajouter(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.CharField(max_length=50)
    phonenumber = PhoneNumberField()
    address = forms.CharField(max_length=40)

