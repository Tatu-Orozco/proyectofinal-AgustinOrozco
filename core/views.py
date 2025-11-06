from django.shortcuts import render
from django.views.decorators.http import require_GET

@require_GET  # Decorador en view común (consigna g)
def home(request):
    return render(request, 'core/home.html')

@require_GET
def about(request):
    return render(request, 'core/about.html')