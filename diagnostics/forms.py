from django import forms
from .models import DiagnosticReport

class DiagnosticReportForm(forms.ModelForm):
    class Meta:
        model = DiagnosticReport
        fields = ['description', 'recommendations', 'required_parts']
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'recommendations': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'required_parts': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }
