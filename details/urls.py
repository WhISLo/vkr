from django.urls import path
from . import views

urlpatterns = [
    path('info/', views.detail_info_view, name='detail_info'),
    path('order/<int:order_id>/', views.order_detail_view, name='order_detail'),
    path('diagnostic/', views.diagnostic_result_view, name='diagnostic_result'),
    path('add_part/', views.add_part_view, name='add_part'),  # Только для менеджеров
    path('my_orders/', views.user_orders_view, name='user_orders'),
    path('order/add/<int:part_id>/', views.add_part_to_order_view, name='add_part_to_order'),
    path('parts/', views.parts_list_view, name='parts_list')
]
