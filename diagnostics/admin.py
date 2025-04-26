# diagnostics/admin.py
from django.contrib import admin
from .models import DiagnosticReport

class DiagnosticReportAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'description', 'recommendations')
    search_fields = ('user__username', 'description', 'recommendations')
    list_filter = ('created_at', 'user')

admin.site.register(DiagnosticReport, DiagnosticReportAdmin)
