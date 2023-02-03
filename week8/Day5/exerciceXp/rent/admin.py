from django.contrib import admin
from .models import Customer, Vehicle_Type, Vehicle, Vehicle_Size, Rental, Rental_Rate

# Register your models here.
admin.site.register(Customer)
admin.site.register(Vehicle_Type)
admin.site.register(Vehicle)
admin.site.register(Vehicle_Size)
admin.site.register(Rental)
admin.site.register(Rental_Rate)