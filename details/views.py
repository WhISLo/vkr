from django.shortcuts import render, redirect, get_object_or_404
from .models import Part, PartOrderHistory
from .forms import PartOrderForm, PartOrderForm
from django.contrib.auth.decorators import login_required, user_passes_test

# Проверка роли менеджера
def is_manager(user):
    return user.groups.filter(name='Manager').exists() or user.is_superuser

def detail_info_view(request):
    return render(request, 'details/detail_info.html')

@login_required
def order_detail_view(request, order_id):
    order = get_object_or_404(PartOrderHistory, id=order_id, user=request.user)
    return render(request, 'details/order_detail.html', {'order': order})

def diagnostic_result_view(request):
    return render(request, 'details/diagnostic_result.html')

# Добавление новой запчасти только для менеджеров
@user_passes_test(is_manager)
def add_part_view(request):
    if request.method == 'POST':
        form = PartOrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('detail_info')
    else:
        form = PartOrderForm()
    return render(request, 'details/add_part.html', {'form': form})

@login_required
def user_orders_view(request):
    orders = PartOrderHistory.objects.filter(user=request.user).order_by('-order_date')
    return render(request, 'details/user_orders.html', {'orders': orders})

# Добавить запчасть в заказ пользователем
@login_required
def add_part_to_order_view(request, part_id):
    part = get_object_or_404(Part, id=part_id)
    if request.method == 'POST':
        form = PartOrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.part = part  # Привязываем запчасть здесь!
            order.save()
            return redirect('user_orders')
    else:
        form = PartOrderForm()
    return render(request, 'details/add_part_to_order.html', {'form': form, 'part': part})
@login_required
def parts_list_view(request):
    query = request.GET.get('q', '')  # Теперь если пусто — ''
    if query:
        parts = Part.objects.filter(name__icontains=query)  # icontains = нечувствительно к регистру
    else:
        parts = Part.objects.all()
    return render(request, 'details/parts_list.html', {'parts': parts, 'query': query})