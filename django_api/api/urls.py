from django.urls import path
from . import views

urlpatterns = [
    path('buses/', views.getData_buses),
    path('buses-user/', views.getData_buses_user),
    path('user/', views.getData_user),
    path('addBuses/', views.addItem_buses),
    path('addBuses-user/', views.addItem_buses_user),
    path('addUser/', views.addItem_user)
]