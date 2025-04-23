from django.shortcuts import render

def dashboard_view(request):
    return render(request, 'pk/dashboard.html')

def profile_view(request):
    return render(request, 'pk/profile.html')

def home_view(request):
    return render(request, 'home.html')