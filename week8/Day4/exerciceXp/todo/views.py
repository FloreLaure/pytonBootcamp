from django.shortcuts import render
from .models import Category, Todo
from .forms import TodoForm

# Create your views here.

def affiche(request):
    context = {
        'category' : Category.objects.all(),
    }
    return render(request, 'todo/affiche.html', context)

def ajout(request):
	context = {
	'forms' : TodoForm(),
	}
	return render(request, 'todo/ajout.html', context)

