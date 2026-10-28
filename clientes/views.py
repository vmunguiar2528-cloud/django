# clientes/views.py
"""Vistas de la app clientes — W02 (placeholder)."""
from django.shortcuts import render

from .models import Cliente


def index(request):
    """Muestra la cartera de clientes."""
    context = {
        'titulo': 'Clientes',
        'descripcion': 'Gestión de cartera de clientes.',
        'clientes': Cliente.objects.all(),
    }
    return render(request, 'clientes/index.html', context)