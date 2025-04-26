'''

from django.db import models
from django.conf import settings

class DiagnosticReport(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='diagnostic_reports',
        verbose_name='Пользователь'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    description = models.TextField(verbose_name='Описание неисправностей')
    recommendations = models.TextField(verbose_name='Рекомендуемые работы')
    required_parts = models.ManyToManyField(
        'details.Part',
        blank=True,
        related_name='diagnostic_reports',
        verbose_name='Необходимые запчасти'
    )

    class Meta:
        verbose_name = 'Отчёт о диагностике'
        verbose_name_plural = 'Отчёты о диагностике'
        ordering = ['-created_at']

    def __str__(self):
        return f"Отчёт от {self.created_at.strftime('%d.%m.%Y')} для {self.user.email}"
'''
# diagnostics/models.py
from django.db import models
from authorization.models import CustomUser
from details.models import Part  # не забудь импорт

class DiagnosticReport(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='diagnostics')
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    recommendations = models.TextField()
    required_parts = models.ManyToManyField(Part, blank=True)

    def __str__(self):
        return f"Диагностика от {self.created_at.strftime('%d.%m.%Y')} для {self.user.email}"
