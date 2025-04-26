from django.db import models
from authorization.models import CustomUser

class Part(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(blank=True, verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    in_stock = models.BooleanField(default=True, verbose_name="В наличии")

    def __str__(self):
        return self.name

class PartOrderHistory(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='part_order_history')
    part = models.ForeignKey(Part, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=[('ordered', 'Ordered'), ('received', 'Received')], default='ordered')

    def __str__(self):
        return f"Запчасть: {self.part.name}, Статус: {self.status}, Дата заказа: {self.order_date.strftime('%d.%m.%Y')}"