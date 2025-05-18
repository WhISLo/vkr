from django.contrib import admin
from django.urls import path, include

import details
from pk.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('authorization/', include('authorization.urls')),
    path('pk/', include('pk.urls')),
    path('history/', include('history.urls')),
    path('details/', include('details.urls')),
    path('external/', include('external_parts.urls')),
    path('diagnostics/', include('diagnostics.urls')),  # Подключаем маршруты диагностических отчетов
    path('details/', include('details.urls', namespace='details')),
    path('parts/<int:pk>/', details.views.part_detail_view, name='part_detail'),
    path('garage/', include('vehicles.urls', namespace='vehicles')),
]
