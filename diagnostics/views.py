from django.shortcuts import render, redirect
from diagnostics.forms import DiagnosticReportForm  # не забудь создать форму
from diagnostics.models import DiagnosticReport  # и модель отчёта
from django.contrib.auth.decorators import login_required

@login_required
def create_report_view(request):
    if request.method == 'POST':
        form = DiagnosticReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.user = request.user  # связываем с текущим пользователем
            report.save()
            return redirect('profile')  # после сохранения — назад в профиль
    else:
        form = DiagnosticReportForm()
    return render(request, 'diagnostics/create_report.html', {'form': form})
