from django.shortcuts import render
from .models import Proyect # Importamos el Model Proyect

# Create your views here.


def portafolio(request):
    """
    Vista que muestra elementos HTML.

    Args:
        request (_type_): La vista recibe 
        petpeticiones/metodos GET, POST, PUT, etc.

    Returns:
        HttpResponse: Variables que contienen
        elementos HTML.
    """
    # Query Devuelve todos los objetos que contenga el modelo de "Proyect".
    proyects = Proyect.objects.all()

    return render(request, 'portfolio/portafolio.html', {'proyects':proyects})


def portfolio_description(request, id):
    
    proyect = Proyect.objects.filter(id=id).first()

    return render(request, 'portfolio/portfolio_description.html', {'proyect':proyect})