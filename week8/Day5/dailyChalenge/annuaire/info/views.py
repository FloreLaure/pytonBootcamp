from django.shortcuts import render
from django.http import HttpResponse
from .models import Persons
from .forms import ajouter,recherche
from django.shortcuts import redirect
from django.db.models import Q

def ajout(request):
    context = {
        'form' : ajouter(),
    }

    if request.method == 'POST':
        # POST, generate form with data from the request
        form = ajouter(request.POST)
        # check if we get data
        print("data", form.data)
        # check if it's valid:
        if form.is_valid():
            a = Persons()
            a.name = form.cleaned_data['name']
            a.email = form.cleaned_data['email']
            a.phonenumber = form.cleaned_data['phonenumber']
            a.address = form.cleaned_data['address']
            a.save()
            return redirect(f'/persons/{a.phonenumber}')

        else:
             # print the errors, just in case
            print("---ERRORS---", form.errors)
            context['form'] = form
            print(form)
            return render(request, 'info/ajout.html', context)
    return render(request, 'info/ajout.html', context)


def info(request, phonenumber=0):
    context = {'form' : recherche()}
    if request.method == 'POST':
        # POST, generate form with data from the request
        form = recherche(request.POST)
        # check if we get data
        print("data", form.data)
        # check if it's valid:
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phonenumber = form.cleaned_data['phonenumber']
            a = Persons.objects.filter(Q(name=name)|Q(email=email)|Q(phonenumber=phonenumber))
            print(a)
            context = {
		        'persons' : a,
	        }
        context['form']=recherche()

    else:
        a = Persons.objects.filter(phonenumber=phonenumber)
        context['persons'] = a
    return render(request, "info/index.html", context)


def infos(request, name=""):
    context = {'form' : recherche()}
    if request.method == 'POST':
        # POST, generate form with data from the request
        form = recherche(request.POST)
        # check if we get data
        print("data", form.data)
        # check if it's valid:
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phonenumber = form.cleaned_data['phonenumber']
            a = Persons.objects.filter(Q(name=name)|Q(email=email)|Q(phonenumber=phonenumber))
            print(a)
            context = {
		        'persons' : a,
	        }
        context['form']=recherche()

    else:
        a = Persons.objects.filter(name=name)
        context['persons'] = a
    return render(request, "info/index.html", context)


