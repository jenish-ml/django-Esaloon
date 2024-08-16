from django import forms
from .models import Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'choose']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 216px'})
        }
