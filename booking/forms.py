from django import forms
from .models import UserBook
from datetime import date, timedelta

class PaymentForm(forms.ModelForm):
    class Meta:
        model = UserBook
        fields = ['card_no', 'cvv', 'valid_date', 'booking_date', 'booking_time']
        widgets = {
            'card_no': forms.TextInput(attrs={
                'class': 'form-control bg-transparent number',
                'maxlength': '16'  # Changed min_length to maxlength for card number
            }),
            'cvv': forms.PasswordInput(attrs={
                'class': 'form-control bg-transparent cvv'
            }),
            'valid_date': forms.DateInput(attrs={
                'class': 'form-control bg-transparent d',
                'type': 'date'
            }),
            'booking_date': forms.DateInput(attrs={
                'class': 'form-control bg-transparent bd',
                'type': 'date',
                'min': date.today().strftime('%Y-%m-%d'),
                'max': (date.today() + timedelta(days=4)).strftime('%Y-%m-%d')
            }),
            'booking_time': forms.TimeInput(attrs={
                'class': 'form-control bg-transparent',
                'type': 'time'
            })
        }

class CosPaymentForm(forms.ModelForm):
    class Meta:
        model = UserBook
        fields = ['card_no', 'cvv', 'valid_date', 'no_of_products']
        widgets = {
            'card_no': forms.TextInput(attrs={
                'class': 'form-control bg-transparent number',
                'maxlength': '16'  # Changed min_length to maxlength for card number
            }),
            'cvv': forms.PasswordInput(attrs={
                'class': 'form-control bg-transparent cvv'
            }),
            'valid_date': forms.DateInput(attrs={
                'class': 'form-control bg-transparent d',
                'type': 'date'
            }),
            'no_of_products': forms.NumberInput(attrs={  # Changed TextInput to NumberInput
                'class': 'form-control bg-transparent'
            })
        }

class ReplyForm(forms.ModelForm):
    class Meta:
        model = UserBook
        fields = ['messages']
        widgets = {
            'messages': forms.Textarea(attrs={
                'class': 'form-control bg-transparent',
                'rows': 4  # Added rows attribute for better text area size
            })
        }
