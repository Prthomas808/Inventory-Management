from django import forms
from .models import Inventory

class InventoryForm:
    class Meta:
        model = Inventory
        fields = ['name', 'description', 'quantity', 'price']