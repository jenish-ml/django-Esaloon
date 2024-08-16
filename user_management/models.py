from django.db import models
from public_management.models import Registration

class Location(models.Model):
    user = models.ForeignKey(Registration, on_delete=models.CASCADE, null=True)
    longitude = models.FloatField()
    latitude = models.FloatField()
    route = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"Location for user {self.user.id} - {self.route or 'No route'}"
