from django import forms
from .models import Complaints, Feedbacks

class ComplaintsForm(forms.ModelForm):
    class Meta:
        model = Complaints
        fields = ['subject', 'message']
        widgets = {
            'subject': forms.TextInput(attrs={
                'class': 'form-control bg-transparent',
                'type': 'text',
                'style': 'color:white'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control bg-transparent',
                'style': 'color:white;'
            })
        }

class FeedbacksForm(forms.ModelForm):
    class Meta:
        model = Feedbacks
        fields = ['subject', 'message', 'saloon_name', 'service_id', 'product_id', 'rating']
        widgets = {
            'subject': forms.TextInput(attrs={
                'class': 'form-control bg-transparent',
                'type': 'text',
                'style': 'color:white'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control bg-transparent',
                'style': 'color:white;'
            }),
            'rating': forms.NumberInput(attrs={
                'class': 'form-control bg-transparent',
                'style': 'color:white'
            })
        }
