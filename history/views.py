from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from details.models import PartOrderHistory
from diagnostics.models import DiagnosticReport

@login_required
def service_history_view(request):
    return render(request, 'history/service_history.html', {
        'part_orders': PartOrderHistory.objects.filter(user=request.user)
                           .select_related('part')
                           .order_by('-order_date'),
        'diagnostics': DiagnosticReport.objects.filter(user=request.user)
                            .prefetch_related('required_parts')
                            .order_by('-created_at')
    })

def parts_history_view(request):
    return render(request, 'history/parts_history.html')


