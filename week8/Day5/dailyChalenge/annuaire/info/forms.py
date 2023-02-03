from django import forms
from .models import Persons
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberInternationalFallbackWidget

class ajouter(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.CharField(max_length=50)
    phonenumber = PhoneNumberField(
        widget=PhoneNumberInternationalFallbackWidget()
    )
    address = forms.CharField(max_length=40)

class recherche(forms.Form):
    name = forms.CharField(max_length=30,required=False)
    email = forms.CharField(max_length=50,required=False)
    phonenumber = PhoneNumberField(
        widget=PhoneNumberInternationalFallbackWidget()
    )


