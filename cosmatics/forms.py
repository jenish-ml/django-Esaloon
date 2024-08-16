from django import forms
from .models import Cosmetics, Category

class AddCosmeticsForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={"rows": 5, "cols": 20}), label='Description')

    class Meta:
        model = Cosmetics
        fields = ['product_name', 'category', 'image', 'price', 'description', 'number_of_products', 'booking_date']
        widgets = {
            'booking_date': forms.DateInput(attrs={'type': 'date'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class ViewProductForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.filter(choose="cs"), 
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Category
        fields = ['category']
        help_texts = {
            'category': 'Select a category from the list.',
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
