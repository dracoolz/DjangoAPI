from django.urls import path
from . import views

urlpatterns = [
    #GET
    path('get/buses/', views.getData_buses),
    path('get/buses-user/', views.getData_buses_user),
    path('get/user/', views.getData_user),
    #POST
    path('post/buses/', views.addItem_buses),
    path('post/buses-user/', views.addItem_buses_user),
    path('post/user/', views.addItem_user),
    #DELETE
    # path('deleteBuses/', views.addItem_buses),
    path('delete/buses-user/', views.Delete_buses_user),
    # path('deleteUser/', views.addItem_user)
]