from django import forms
from .models import Part, PartOrderHistory

class PartForm(forms.ModelForm):
    class Meta:
        model = Part
        fields = ['name', 'description', 'price']

class PartOrderForm(forms.ModelForm):
    class Meta:
        model = PartOrderHistory
        fields = ['part', 'quantity']
