from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pk.urls')),
    path('authorization/', include('authorization.urls')),
    path('history/', include('history.urls')),
    path('details/', include('details.urls', namespace='details')),
    path('external/', include('external_parts.urls', namespace='external_parts')),
    path('diagnostics/', include('diagnostics.urls', namespace='diagnostics')),
]
