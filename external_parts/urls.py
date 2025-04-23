from django.urls import path
from . import views

urlpatterns = [
    path('compare/', views.compare_parts_view, name='compare_parts'),
    path('links/', views.marketplace_links_view, name='marketplace_links'),
]
