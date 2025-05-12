from django.core.mail import send_mail
from django.shortcuts import render
from diagnostics.models import DiagnosticReport
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from details.models import PartOrderHistory
from authorization.models import CustomUser
from django.shortcuts import render, redirect
from django.shortcuts import render
from diagnostics.models import DiagnosticReport
from details.models import Part

from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse


def manager_view(request):
    if request.user.role != 'manager':
        return redirect('profile')  # Перенаправление на страницу профиля, если пользователь не приёмщик

    # Логика для приёмщика, например, создание отчётов
    return render(request, 'pk/manager_dashboard.html')


def dashboard_view(request):
    return render(request, 'pk/dashboard.html')


@login_required
def profile_view(request):
    user = request.user  # Получаем текущего пользователя

    # Получаем последние 50 записей из истории запчастей
    part_order_history = PartOrderHistory.objects.filter(user=user).order_by('-order_date')[:50]

    # Получаем последние 50 диагностических отчетов
    diagnostics = DiagnosticReport.objects.filter(user=user).order_by('-created_at')[:50]



##ТУТ БАГ
    return render(request, 'pk/profile.html', {
        'part_order_history': part_order_history,
        'diagnostics': diagnostics,
    })

def home_view(request):
    return render(request, 'home.html')

@login_required
def manager_dashboard(request):
    if request.user.role != 'manager':
        raise Http404("Вы не имеете доступа к этой странице.")

    # Получаем все диагностические отчёты и запчасти
    reports = DiagnosticReport.objects.all()
    parts = Part.objects.all()

    return render(request, 'pk/manager_dashboard.html', {'reports': reports, 'parts': parts})

@login_required
def send_report(request, report_id):
    if request.user.role != 'manager':
        raise Http404("Вы не имеете доступа к этой странице.")

    report = DiagnosticReport.objects.get(id=report_id)

    # Получаем email пользователя, которому нужно отправить отчёт
    user_email = report.user.email

    # Отправляем email
    send_mail(
        'Диагностический отчёт',
        f'Отчёт: {report.description}\n\nРекомендации: {report.recommendations}',
        'from@example.com',
        [user_email],
        fail_silently=False,
    )

    return HttpResponse("Отчёт успешно отправлен!")


def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Отправка email (настройте в settings.py)
        send_mail(
            f'Сообщение от {name}',
            message,
            email,
            ['your@email.com'],  # Ваш email
            fail_silently=False,
        )
        messages.success(request, 'Ваше сообщение отправлено!')
        return redirect('home')

    return render(request, 'contact.html')