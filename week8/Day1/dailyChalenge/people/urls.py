from django.urls import path
from . import views

urlpatterns = [
    path('', views.people, name='people'),
    path('info/<int:id>/', views.info, name='info'),
]
