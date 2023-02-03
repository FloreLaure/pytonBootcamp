from django.shortcuts import render
from django.http import HttpResponse
from info.models import Persons
# from phonenumber_field.formfields import PhoneNumberField

def info(request, phonenumber):
	a = Persons.objects.filter(phonenumber=phonenumber)
	context = {
		'persons' : a,
	}
	return render(request, "info/index.html", context)

def infos(request, name):
	a = Persons.objects.filter(name=name)
	context = {
		'persons' : a,
	}
	return render(request, "info/index.html", context)
