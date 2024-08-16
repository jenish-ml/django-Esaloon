from django import forms
from .models import Job

class AddJobForm(forms.ModelForm):
    job_description = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 5, "cols": 20}),
        required=True
    )

    class Meta:
        model = Job
        fields = ['job_title', 'job_description', 'salary']
        widgets = {
            'salary': forms.NumberInput(attrs={'placeholder': 'Enter salary'})
        }
