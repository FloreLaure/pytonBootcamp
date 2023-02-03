from django.shortcuts import render
from .models import Gif, Category
from django.shortcuts import render
from .forms import GifForm, CategoryForm

# Create your views here.

def affiche(request):
    context = {
        'gifs' : Gif.objects.all(),
        'category' : Category.objects.all(),
    }
    return render(request, 'gifs/affiche.html', context)

def ajoutgif(request):
    context = {
        'form' : GifForm(),
    }
    return render(request, 'gifs/ajoutgif.html', context)

def ajoutcategorie(request):
    context = {
        'form' : CategoryForm(),
    }
    return render(request, 'gifs/ajoutcategorie.html', context)

