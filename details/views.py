from django.shortcuts import render

def detail_info_view(request):
    return render(request, 'details/detail_info.html')

def order_detail_view(request):
    return render(request, 'details/order_detail.html')

def diagnostic_result_view(request):
    return render(request, 'details/diagnostic_result.html')
