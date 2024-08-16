from django.db import models
from public_management.models import Registration  # Adjust import based on actual module structure

class Job(models.Model):
    user = models.ForeignKey(Registration, on_delete=models.CASCADE, null=True, blank=True)
    job_title = models.CharField(max_length=200)
    job_description = models.TextField()  # Changed to TextField for longer descriptions
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Changed to DecimalField for monetary values

    def __str__(self):
        return self.job_title
