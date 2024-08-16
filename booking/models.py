from django.db import models
from public_management.models import Registration
from product.models import Product
from feedback.models import Feedbacks
from cosmatics.models import Cosmetics

class UserBook(models.Model):
    user = models.ForeignKey(Registration, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    card_no = models.CharField(max_length=20, null=True)  # Changed IntegerField to CharField for card numbers
    cvv = models.CharField(max_length=10, blank=True, null=True)
    valid_date = models.CharField(max_length=6, null=True)  # Consider using DateField or DateTimeField if you need more specific date information
    booking_date = models.DateField(null=True)
    end_time = models.TimeField(null=True)
    booking_time = models.TimeField(null=True)
    messages = models.TextField(blank=True)  # Changed CharField to TextField for longer messages
    payment = models.CharField(max_length=50, default='null')  # Default value should be meaningful; consider 'pending' or similar
    status = models.CharField(max_length=50, default='not given', null=True)
    cosmetic_product = models.ForeignKey(Cosmetics, on_delete=models.CASCADE, null=True)
    feedback = models.ForeignKey(Feedbacks, on_delete=models.CASCADE, null=True)  # Renamed f_id to feedback for clarity
    no_of_products = models.PositiveIntegerField(default=1)  # Changed CharField to PositiveIntegerField for numeric values

class Cart(models.Model):
    user = models.ForeignKey(Registration, on_delete=models.CASCADE, null=True)  # Renamed uid to user for clarity
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)  # Renamed sid to product for clarity
    cosmetic = models.ForeignKey(Cosmetics, on_delete=models.CASCADE, null=True)  # Renamed cid to cosmetic for clarity
    no_of_products = models.PositiveIntegerField(default=0)  # Changed CharField to PositiveIntegerField for numeric values
