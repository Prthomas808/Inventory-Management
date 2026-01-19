from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=65)
    product_sku = models.CharField(max_length=65, unique=True)
    product_price = models.FloatField()
    product_quantity = models.IntegerField()

    def __str__(self):
        return self.product_name