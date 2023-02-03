from django.urls import path #path function
from . import views # . is shorthand for the current directory

urlpatterns = [
    path('', views.home, name='home'),
    path('rent/rental', views.rental, name='rental'),
    path('rent/rental/<int:id>', views.rental_detail, name='rental_detail'),
    path('rent/rental/add', views.add_rental, name='add_rental'),
    path('rent/customer', views.customer, name='customer'),
    path('rent/customer/<int:id>', views.customer_detail, name='customer_detail'), 
    path('rent/customer/add', views.add_customer, name='add_customer'),
    path('rent/vehicle', views.vehicle, name='vehicle'),
    path('rent/vehicle/<int:id>', views.vehicle_detail, name='vehicle_detail'),
    path('rent/vehicle/add', views.add_vehicle, name='add_vehicle'),
]