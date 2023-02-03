from django.urls import path #path function
from . import views # . is shorthand for the current directory

# one urlpattern per line
urlpatterns = [
    path('', views.affiche, name='affiche'),
    path('ajoutgif', views.ajoutgif, name='ajoutgif'),
    path('ajoutcategorie', views.ajoutcategorie, name='ajoutcategorie'),
]