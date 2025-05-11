from django.urls import path
from . import views

app_name = 'vehicles'

urlpatterns = [
    path('add/', views.add_vehicle, name='add_vehicle'),
    path('<int:pk>/estimate/', views.estimate_price, name='estimate_price'),
    path('<int:pk>/history/', views.service_history, name='service_history'),
    path('', views.garage_view, name='garage'),
    path('<int:pk>/similar/', views.similar_vehicles, name='similar_vehicles'),
]