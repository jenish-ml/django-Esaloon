from django.db import models
from public_management.models import Registration
from product.models import Product
from cosmatics.models import Cosmetics

class Complaints(models.Model):
    subject = models.CharField(max_length=50, default='')
    message = models.TextField(default='')
    response = models.TextField(default='')
    status = models.IntegerField(default=0, null=True)
    rid = models.ForeignKey(Registration, on_delete=models.CASCADE, null=True, related_name='complaints')

class Feedbacks(models.Model):
    subject = models.CharField(max_length=50, default='')
    message = models.TextField(default='')
    rid = models.ForeignKey(Registration, on_delete=models.CASCADE, null=True, related_name='feedbacks')
    saloon_name = models.ForeignKey(Registration, on_delete=models.CASCADE, null=True, related_name='saloon_feedbacks')
    service_id = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, related_name='feedbacks')
    product_id = models.ForeignKey(Cosmetics, on_delete=models.CASCADE, null=True, related_name='feedbacks')
    rating = models.IntegerField(default=0)
