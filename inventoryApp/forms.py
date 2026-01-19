from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        label = {
            'product_name' : 'Name',
            'product_sku' : 'SKU',
            'product_price' : 'Price',
            'product_quantity' : 'Quantity',
        }
     