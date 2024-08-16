from django import forms
from .models import Registration

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['username', 'password', 'email', 'street_name', 'locality', 'landmark', 'phone_no']
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control bg-transparent name"}),
            "password": forms.PasswordInput(attrs={"class": "form-control bg-transparent pass"}),
            "email": forms.TextInput(attrs={"class": "form-control bg-transparent email"}),
            "street_name": forms.TextInput(attrs={"class": "form-control bg-transparent street"}),
            "locality": forms.TextInput(attrs={"class": "form-control bg-transparent loc"}),
            "landmark": forms.TextInput(attrs={"class": "form-control bg-transparent land"}),
            "phone_no": forms.TextInput(attrs={"class": "form-control bg-transparent phn"}),
        }
        help_texts = {
            "username": None
        }

class SaloonRegisterForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['username', 'password', 'email', 'street_name', 'locality', 'landmark', 'phone_no', 'owner', 'saloon_certificate', 'no_of_seats', 'open_time', 'close_time', 'holiday']
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control bg-transparent name"}),
            "password": forms.PasswordInput(attrs={"class": "form-control bg-transparent pass"}),
            "email": forms.TextInput(attrs={"class": "form-control bg-transparent email"}),
            "street_name": forms.TextInput(attrs={"class": "form-control bg-transparent street"}),
            "locality": forms.TextInput(attrs={"class": "form-control bg-transparent loc"}),
            "landmark": forms.TextInput(attrs={"class": "form-control bg-transparent land"}),
            "phone_no": forms.TextInput(attrs={"class": "form-control bg-transparent phn"}),
            "owner": forms.TextInput(attrs={"class": "form-control bg-transparent"}),
            "saloon_certificate": forms.FileInput(attrs={"class": "form-control bg-transparent"}),
            "no_of_seats": forms.NumberInput(attrs={"class": "form-control bg-transparent"}),
            "open_time": forms.TimeInput(attrs={"class": "form-control bg-transparent", "type": "time"}),
            "close_time": forms.TimeInput(attrs={"class": "form-control bg-transparent", "type": "time"}),
            "holiday": forms.Select(attrs={"class": "form-control bg-transparent"})
        }
        help_texts = {
            "username": None
        }

class FreelancerRegisterForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['username', 'password', 'email', 'street_name', 'locality', 'landmark', 'phone_no', 'experience_certificate']
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control bg-transparent"}),
            "password": forms.PasswordInput(attrs={"class": "form-control bg-transparent"}),
            "email": forms.TextInput(attrs={"class": "form-control bg-transparent email"}),
            "street_name": forms.TextInput(attrs={"class": "form-control bg-transparent"}),
            "locality": forms.TextInput(attrs={"class": "form-control bg-transparent"}),
            "landmark": forms.TextInput(attrs={"class": "form-control bg-transparent"}),
            "phone_no": forms.TextInput(attrs={"class": "form-control bg-transparent phn"}),
            "experience_certificate": forms.FileInput(attrs={"class": "form-control bg-transparent"}),
        }
        help_texts = {
            "username": None
        }

class ForgotForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['email']

class LoginForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['username', 'password']
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control bg-transparent"}),
            "password": forms.PasswordInput(attrs={"class": "form-control bg-transparent"}),
        }
