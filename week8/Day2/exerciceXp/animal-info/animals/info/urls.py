from django.urls import path
from . import views

urlpatterns = [
  path('family/<int:x>', views.family, name='family'),
  path('animal/<int:x>/', views.animal, name='animal'),
  path('animals/', views.animals, name='animals')
]