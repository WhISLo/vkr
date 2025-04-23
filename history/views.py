from django.shortcuts import render

def service_history_view(request):
    return render(request, 'history/service_history.html')

def parts_history_view(request):
    return render(request, 'history/parts_history.html')
