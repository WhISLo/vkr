from django import forms
from .models import Vehicle

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['make', 'model', 'year', 'license_plate', 'vin', 'mileage', 'last_service', 'category']
        widgets = {
            'last_service': forms.DateInput(attrs={'type': 'date'}),
            'year': forms.NumberInput(attrs={'min': 1990, 'max': 2025}),
        }
        labels = {
            'make': 'Марка',
            'model': 'Модель',
            'year': 'Год выпуска',
            'license_plate': 'Госномер',
            'vin': 'VIN-код',
            'mileage': 'Пробег (км)',
            'last_service': 'Дата последнего ТО',
            'category': 'Тип кузова'
        }