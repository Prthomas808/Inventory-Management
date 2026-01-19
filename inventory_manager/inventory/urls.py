from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_inventory, name='inventory-home'),
    path('add/', views.add_to_inventory, name='add_to_inventory')
]