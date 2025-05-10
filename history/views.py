from django.shortcuts import render

from details.models import PartOrderHistory
from diagnostics.models import DiagnosticReport

def service_history_view(request):
    # Получаем все заказы запчастей
    part_orders = PartOrderHistory.objects.filter(user=request.user)

    # Получаем все диагностические отчеты
    diagnostics = DiagnosticReport.objects.filter(user=request.user)

    return render(request, 'history/service_history.html', {
        'part_orders': part_orders,
        'diagnostics': diagnostics
    })

def parts_history_view(request):
    return render(request, 'history/parts_history.html')
