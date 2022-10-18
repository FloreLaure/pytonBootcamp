from django.urls import path #path function
from . import views # . is shorthand for the current directory

# one urlpattern per line
urlpatterns = [
    path('', views.animal, name='animal'),
    path('family/', views.family, name='family'),
    path('animaux/', views.animaux, name='animaux'),

]