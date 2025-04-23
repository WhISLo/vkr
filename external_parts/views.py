from django.shortcuts import render

def compare_parts_view(request):
    return render(request, 'external_parts/compare_parts.html')

def marketplace_links_view(request):
    return render(request, 'external_parts/marketplace_links.html')
