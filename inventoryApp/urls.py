from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('create/', views.create_product, name='create_product'),
    path('list/', views.list_product, name='product_list'),
    path('update/<int:id>/', views.update_product, name='update_product'),
    path('delete/<int:id>/', views.delete_product, name='delete_product'),
]