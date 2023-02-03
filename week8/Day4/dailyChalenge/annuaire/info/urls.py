from django.urls import path
from . import views


urlpatterns = [
  path('', views.ajout, name='ajout'),
  path('persons/<str:phonenumber>/', views.info, name='info'),
  path('person/<str:name>/', views.infos, name='infos'),
]