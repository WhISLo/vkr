from django.urls import path
from . import views
from authorization.views import logout_view

urlpatterns = [
    # Главная страница
    path('', views.home_view, name='home'),

    # Страница профиля для пользователя
    path('profile/', views.profile_view, name='profile'),

    # Логин/выход
    path('logout/', logout_view, name='logout'),

    # Страница для приёмщика (менеджера)
    path('manager/', views.manager_view, name='manager_dashboard'),

    # Отправка отчёта
    path('send_report/<int:report_id>/', views.send_report, name='send_report'),

    # Страница профиля приёмщика (менеджера)
    path('manager/profile/', views.manager_dashboard, name='manager_profile'),
    # изменил на 'manager_profile' для различия

]
