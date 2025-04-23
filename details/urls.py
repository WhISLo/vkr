from django.urls import path
from . import views

urlpatterns = [
    path('info/', views.detail_info_view, name='detail_info'),
    path('order/', views.order_detail_view, name='order_detail'),
    path('diagnostic/', views.diagnostic_result_view, name='diagnostic_result'),
]
