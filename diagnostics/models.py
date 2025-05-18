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
