from django import forms
from rent.models import Rental, Customer, Vehicle 


class AddRental(forms.ModelForm):
    class Meta:
        model = Rental
        fields = '__all__'
        
        
class CustomForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        
        
class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'
        