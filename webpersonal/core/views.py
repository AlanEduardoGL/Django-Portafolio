from django.shortcuts import (
    render,  # Permite renderizar plantillas Html.
    HttpResponse  # Nos permite responser una petición, devolviendo un código.
)


def home(request):
    """
    Vista que muestra elementos HTML.

    Args:
        request (_type_): La vista recibe 
        petpeticiones/metodos GET, POST, PUT, etc.

    Returns:
        HttpResponse: Variables que contienen
        elementos HTML.
    """
    contenido_html = "Contenido Principal."

    return render(request, 'core/home.html', {'contenido_html': contenido_html})


def about(request):
    """
    Vista que muestra elementos HTML.

    Args:
        request (_type_): La vista recibe 
        petpeticiones/metodos GET, POST, PUT, etc.

    Returns:
        HttpResponse: Variables que contienen
        elementos HTML.
    """
    contenido_html = 'Soy un programador.'

    return render(request, 'core/about.html', {'contenido_html': contenido_html})


def contact(request):
    """
    Vista que muestra elementos HTML.

    Args:
        request (_type_): La vista recibe 
        petpeticiones/metodos GET, POST, PUT, etc.

    Returns:
        HttpResponse: Variables que contienen
        elementos HTML.
    """
    contenido_html = 'Vista de Contacto.'

    return render(request, 'core/contact.html', {'contenido_html': contenido_html})
