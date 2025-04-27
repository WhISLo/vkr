# details/forms.py
from django import forms
from .models import PartOrderHistory

class PartOrderForm(forms.ModelForm):
    class Meta:
        model = PartOrderHistory
        fields = ['quantity']  # Убираем поле 'part'
