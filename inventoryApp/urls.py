from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('create/', views.create_product, name='create-product'),
    path('list/', views.list_product, name='list-product'),
    path('update/<int:id>/', views.update_product, name='update-product'),
    path('delete/<int:id>/', views.delete_product, name='delete-product'),
]