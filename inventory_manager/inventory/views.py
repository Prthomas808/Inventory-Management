from django.shortcuts import render, redirect
from .models import Inventory
from .forms import InventoryForm

# Create your views here.

# all inventory view
def all_inventory(request):
    items = Inventory.objects.all()
    return render(request, 'inventory_home.html', {'items' : items})

# add item to inventory view
def add_to_inventory(request):
    if request.method == "POST":
        form = InventoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory-home')
    else:
        form = InventoryForm()

    return render(request, 'add_to_inventory.html', {'form' : form})