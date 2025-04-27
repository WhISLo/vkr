from django.contrib import admin
from .models import Part, PartOrderHistory

admin.site.register(Part)
admin.site.register(PartOrderHistory)
