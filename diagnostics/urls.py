# diagnostics/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_report_view, name='create_diagnostic_report'),
]
