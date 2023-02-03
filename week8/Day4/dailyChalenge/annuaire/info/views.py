from django.shortcuts import render
from django.http import HttpResponse
from .models import Persons
from .forms import ajouter
from django.shortcuts import redirect

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


def info(request, phonenumber):
    a = Persons.objects.filter(phonenumber=phonenumber)
    if not(a) :
        pass
    else :
        a=a[0]
    context = {
		'persons' : a,
	}
    return render(request, "info/index.html", context)

def infos(request, name):
    a = Persons.objects.filter(name=name)
    if not(a) :
        pass
    else :    
        a=a[0]
    context = {
		'persons' : a,
	}
    return render(request, "info/index.html", context)
