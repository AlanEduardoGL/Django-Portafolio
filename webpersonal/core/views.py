from django.shortcuts import (
    render,
    HttpResponse  # Nos permite responser una petición, devolviendo un código.
)


base_html = """
    <h1>Mi Web Personal</h1>
    <ul>
        <li><a href="/">Inicio</a></li>
        <li><a href="/about/">Acerca de</a></li>
    </ul>
"""


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
    contenido_html = "<h2>Contenido Inicial</h2>"

    return HttpResponse(base_html + contenido_html)


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
    acerca_de_html = "<h1>Acerca de mi</h1>"
    contenido_html = "<p>Soy un programador.</p>"

    contenido_html = acerca_de_html + contenido_html

    return HttpResponse(base_html + contenido_html)
