from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Vehicle
from .forms import VehicleForm
import requests  # Для API оценки стоимости


@login_required
def garage_view(request):
    vehicles = request.user.vehicles.all()
    return render(request, 'vehicles/garage.html', {'vehicles': vehicles})


@login_required
def add_vehicle(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            vehicle = form.save(commit=False)
            vehicle.user = request.user
            vehicle.save()
            return redirect('vehicles:garage')
    else:
        form = VehicleForm()

    return render(request, 'vehicles/add_vehicle.html', {'form': form})


@login_required
def estimate_price(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk, user=request.user)

    # Получаем похожие автомобили
    similar_vehicles = Vehicle.objects.filter(
        make=vehicle.make,
        category=vehicle.category,
        year__gte=vehicle.year - 2,
        year__lte=vehicle.year + 2
    ).exclude(pk=pk).order_by('?')[:3]

    # Простая логика оценки (можно заменить на реальный API)
    if vehicle.year and vehicle.mileage:
        base_price = {
            'sedan': 500000,
            'suv': 800000,
            'hatchback': 400000,
            'coupe': 600000,
            'minivan': 700000,
        }.get(vehicle.category, 500000)

        age_factor = max(0, 1 - (2025 - vehicle.year) * 0.1)
        mileage_factor = max(0.3, 1 - (vehicle.mileage / 200000))
        estimated_price = int(base_price * age_factor * mileage_factor)
    else:
        estimated_price = None

    return render(request, 'vehicles/estimate.html', {
        'vehicle': vehicle,
        'estimated_price': estimated_price,
        'similar_vehicles': similar_vehicles
    })


@login_required
def service_history(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk, user=request.user)
    # Здесь можно добавить логику получения истории обслуживания
    return render(request, 'vehicles/history.html', {'vehicle': vehicle})


@login_required
def similar_vehicles(request, pk):
    user_vehicle = get_object_or_404(Vehicle, pk=pk, user=request.user)

    # Получаем похожие автомобили (той же категории и +/- 2 года)
    similar = Vehicle.objects.filter(
        category=user_vehicle.category,
        year__gte=user_vehicle.year - 2,
        year__lte=user_vehicle.year + 2
    ).exclude(pk=pk).order_by('?')[:6]  # 6 случайных похожих авто

    # Если мало результатов, расширяем критерии
    if similar.count() < 3:
        similar = Vehicle.objects.filter(
            category=user_vehicle.category
        ).exclude(pk=pk).order_by('?')[:6]

    return render(request, 'vehicles/similar.html', {
        'user_vehicle': user_vehicle,
        'similar_vehicles': similar
    })
