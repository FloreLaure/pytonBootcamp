from django.shortcuts import render
from django.http import HttpResponse

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
        },
        {
            "id": 4,
            "name": "Serpent",
            "legs": 0,
            "weight": 1.67,
            "height":1.5,
            "speed": 15,
            "family": 3 
        },
        {
            "id": 5,
            "name": "Mouche",
            "legs": 6,
            "weight": 0.10,
            "height":0.06,
            "speed": 34,
            "family": 4 
        }
    ],
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
            "name": "reptile"
        },
        {
            "id": 4,
            "name": "insect"
        }
    ]
}

def famille(request, X):
    context.update({'X' : X})
    return render(request, "info/famille.html", context)

def animal(request, X):
    context.update({'X' : X})
    return render(request, "info/animal.html", context)