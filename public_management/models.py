from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Choices for gender and weekday
GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
]

WEEKDAY_CHOICES = [
    (0, 'Sunday'),
    (1, 'Monday'),
    (2, 'Tuesday'),
    (3, 'Wednesday'),
    (4, 'Thursday'),
    (5, 'Friday'),
    (6, 'Saturday'),
]

class Registration(AbstractUser):
    email = models.EmailField(max_length=100, unique=True)
    contact = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    street_name = models.CharField(max_length=50, blank=True, null=True)
    locality = models.CharField(max_length=50, blank=True, null=True)
    landmark = models.CharField(max_length=50, blank=True, null=True)
    usertype = models.CharField(max_length=50, blank=True, null=True)
    phone_no = models.CharField(max_length=15, blank=True, null=True)
    owner = models.CharField(max_length=50, blank=True, null=True)
    saloon_certificate = models.FileField(upload_to='certificates/', blank=True, null=True)
    firm_license = models.FileField(upload_to='licenses/', blank=True, null=True)
    experience_certificate = models.FileField(upload_to='experience_certificates/', blank=True, null=True)
    no_of_seats = models.IntegerField(
        default=1,
        null=True,
        validators=[MaxValueValidator(100), MinValueValidator(1)]
    )
    status = models.CharField(max_length=50, blank=True, null=True)
    open_time = models.TimeField(default='07:00:00')
    close_time = models.TimeField(default='22:00:00')
    holiday = models.IntegerField(choices=WEEKDAY_CHOICES, default=2)
    
    groups = models.ManyToManyField(
        Group,
        related_name='registration_set',
        blank=True,
        help_text='The groups this user belongs to.'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='registration_set',
        blank=True,
        help_text='Specific permissions for this user.'
    )

    def __str__(self) -> str:
        return self.username
