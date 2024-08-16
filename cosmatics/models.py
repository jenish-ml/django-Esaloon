from django.db import models
from category.models import Category
from public_management.models import Registration

# Create your models here.
class Cosmetics(models.Model):
    product_name = models.CharField(max_length=200, default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    price = models.FloatField(default=0.0)
    description = models.CharField(max_length=200, default='')
    user = models.ForeignKey(Registration, on_delete=models.CASCADE)
    number_of_products = models.IntegerField(default=0)
    booking_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.product_name
