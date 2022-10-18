from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# exerciceXp

def animal(request):
    context = {
        "animals": [
        {
            "id" :1,
            "name": "Dog",
            "legs": 4,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 2
        },
        {
            "id": 2,
            "name": "Domestic Cat",
            "legs": 2,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 1
        },
        {
            "id": 3,
            "name": "Panther",
            "legs": 2,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 1 
        }
    ]
    }

    return HttpResponse(context["animals"])

def family(request):
	context= {
	 	"families": [
	        {
	            "id": 1,
	            "name": "Felidae"
	        },
	        {
	            "id": 2,
	            "name": "Caninae"
	        },
	        {
	            "id": 3,
	            "name": "insecte"
	        },
	        {
	            "id": 4,
	            "name": "mammifère"
	        },
	        {
	            "id": 5,
	            "name": "reptile"
	        }
    ]
	}
	return HttpResponse(context["families"])


# exerciceXpGold

def animaux(request):
    context = {
        "animals": [
        {
            "id" :1,
            "name": "Dog",
            "legs": 4,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 2
        },
        {
            "id": 2,
            "name": "Domestic Cat",
            "legs": 2,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 1
        },
        {
            "id": 3,
            "name": "Panther",
            "legs": 2,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 1 
        }
    ]
    }
    return HttpResponse(context["animals"][0]["name"])
	
