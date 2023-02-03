from django.shortcuts import render
from .models import Family, Animal

def family(request,x):
	animal = Animal.objects.filter(family__pk = x)
	context = {
		'animals':animal
	}
	return render(request, 'info/famille.html',context)

def animal(request,x):
	animal = Animal.objects.filter(pk = x)
	context = {
		'animals':animal
	}
	return render(request, 'info/animal.html',context)

def animals(request):
	animal = Animal.objects.all()
	context = {
		'animals':animal
	}
	return render(request, 'info/animal.html',context)
	