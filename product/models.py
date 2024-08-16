from django.db import models
from category.models import Category
from public_management.models import Registration

class Product(models.Model):
    name = models.CharField(max_length=200, default='')
    product_name = models.CharField(max_length=200, default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    price = models.FloatField(default=0)
    description = models.TextField(default='')
    user = models.ForeignKey(Registration, on_delete=models.CASCADE)
    usertype = models.CharField(max_length=200, default='')
    time = models.IntegerField(default=0)
    no_of_products = models.IntegerField(default=0)

    def __str__(self):
        return self.product_name
