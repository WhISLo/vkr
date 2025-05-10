from django.urls import path
from . import views

app_name = 'history'

urlpatterns = [
    path('service/', views.service_history_view, name='service_history'),
    path('parts/', views.parts_history_view, name='parts_history'),
]

