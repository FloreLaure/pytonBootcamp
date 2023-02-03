from django.urls import path
from . import views

urlpatterns = [
    path('family/<int:X>/', views.famille, name='famille'),
    path('animal/<int:X>/', views.animal, name='animal'),
]
