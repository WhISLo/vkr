from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20, blank=True)
    car_model = models.CharField(max_length=100, blank=True)

    ROLE_CHOICES = [
        ('client', 'Клиент'),
        ('manager', 'Приемщик'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='client')

    def __str__(self):
        return self.username
