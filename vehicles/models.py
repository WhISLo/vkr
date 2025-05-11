from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Vehicle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='vehicles')
    make = models.CharField(max_length=50, verbose_name="Марка")
    model = models.CharField(max_length=50, verbose_name="Модель")
    year = models.PositiveIntegerField(verbose_name="Год выпуска")
    license_plate = models.CharField(max_length=15, verbose_name="Госномер", unique=True)
    vin = models.CharField(max_length=17, verbose_name="VIN-код", unique=True)
    mileage = models.PositiveIntegerField(verbose_name="Пробег (км)")
    last_service = models.DateField(verbose_name="Последнее ТО")
    estimated_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Рыночная цена", null=True,
                                          blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    CATEGORY_CHOICES = [
        ('sedan', 'Седан'),
        ('suv', 'Внедорожник'),
        ('hatchback', 'Хэтчбек'),
        ('coupe', 'Купе'),
        ('minivan', 'Минивэн'),
    ]
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        verbose_name="Категория",
        blank=True,  # Разрешить пустое значение в формах
        null=True,  # Разрешить NULL в базе данных
        default='sedan'  # Значение по умолчанию
    )

    class Meta:
        verbose_name = "Автомобиль"
        verbose_name_plural = "Автомобили"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.make} {self.model} ({self.year}) - {self.license_plate}"