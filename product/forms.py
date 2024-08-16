from django import forms
from .models import Product, Category

class AddProductForm(forms.ModelForm):
    desc = forms.CharField(widget=forms.Textarea(attrs={"rows": 5, "cols": 20}))

    class Meta:
        model = Product
        fields = ['name', 'time', 'category', 'image', 'price', 'desc']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        self.fields['category'].queryset = Category.objects.filter(choose='sf')


class ViewProductForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.filter(choose="sf"), required=False)

    class Meta:
        model = Product
        fields = ['category']
        help_texts = {
            "category": None
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class SellerProductForm(forms.ModelForm):
    desc = forms.CharField(widget=forms.Textarea(attrs={"rows": 5, "cols": 20}))

    class Meta:
        model = Product
        fields = ['name', 'category', 'image', 'price', 'desc']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
