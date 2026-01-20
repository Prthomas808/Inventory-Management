from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm

# Create your views here.

# Home View
def index(request):
    return render(request, 'index.html')

# Create Product
def create_product(request):
    form = ProductForm
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()

    return render(request, 'product_form.html', {'form' : form})

# Product List
def list_product(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products' : products})

# Update Product
def update_product(request, id):
    product = Product.objects.get(id=id)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()

    return render(request, 'product_form', {'form' : form})

# Delete Product
def delete_product(request, id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    
    return render(request, 'product_delete.html', {'product' : product})