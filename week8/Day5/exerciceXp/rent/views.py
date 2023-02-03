from django.shortcuts import render, redirect
from .forms import AddRental, VehicleForm, CustomForm
from .models import Rental, Customer, Vehicle


def home(request):
    return render(request, 'rent/home.html')


def rental(request):
    context ={"all":Rental.objects.all()}
    return render(request, 'rent/rental.html', context)


def rental_detail(request, id):
    context ={"all":Rental.objects.filter(pk = id)}
    return render(request, 'rent/rental_detail.html', context)


def add_rental(request):
    if request.method=="POST":
        form = AddRental(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'rent/home.html')
        else:
            form = AddRental()
            return render(request, 'rent/add.html', {"form":form})
    else:
        form = AddRental()
        return render(request, 'rent/add.html', {"form":form})
    
    
def customer(request):
    context ={"all": Customer.objects.all()}
    return render(request, 'rent/aff.html', context)


def customer_detail(request, id):
    context ={"all": Customer.objects.filter(pk = id)}
    return render(request, 'rent/customer_detail.html', context)

  
def add_customer(request):
    if request.method=="POST":
        form = CustomForm(request.POST)    
        if form.is_valid():
            form.save()
            return render(request, 'rent/home.html')
        else:
            return render(request, 'rent/aff.html', {"form":form})
    else:
        form = CustomForm()
        return render(request, 'rent/add.html', {"form":form})
    


def vehicle(request):
    context ={"all": Vehicle.objects.all()}
    return render(request, 'rent/vehicle.html', context)


def vehicle_detail(request, id):
    context ={"all": Vehicle.objects.filter(pk = id)}
    return render(request, 'rent/vehicle_detail.html', context)


def add_vehicle(request):
    if request.method=="POST":
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'rent/home.html')
        else:
            return render(request, 'rent/add_vehi.html', {"form":form})
    else:
        form = VehicleForm()
        return render(request, 'rent/add.html', {"form":form})
    


