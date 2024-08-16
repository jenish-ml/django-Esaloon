from django import forms
from .models import Location

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['latitude', 'longitude', 'route']
        widgets = {
            'route': forms.URLInput(attrs={'placeholder': 'Enter location URL'}),
        }
