from django.shortcuts import render, redirect
from .forms import ReportForm  # не забудь создать форму
from .models import Report  # и модель отчёта
from django.contrib.auth.decorators import login_required

@login_required
def create_report_view(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.user = request.user  # связываем с текущим пользователем
            report.save()
            return redirect('profile')  # после сохранения — назад в профиль
    else:
        form = ReportForm()
    return render(request, 'diagnostics/create_report.html', {'form': form})
