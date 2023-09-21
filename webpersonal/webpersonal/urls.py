"""
URL configuration for webpersonal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views as core_views  # Importamos funciones views.py de "core".
from portfolio import views as portfolio_views # Importamos funciones views.py de "portfolio".
from django.conf import settings

urlpatterns = [
    path('', core_views.home, name='home'),  # Importamos la función/vista "home".
    # Importamos la función/vista "about".
    path('about/', core_views.about, name='about'),
    # Importamos la funcion/vista "portafolio"
    path('portafolio/', portfolio_views.portafolio, name='portafolio'),
    # Importamos la funcion/vista "contact"
    path('contact/', core_views.contact, name='contact'),
    path('admin/', admin.site.urls),
]

# Configuracion para que pueda abrir los ficheros de "media".
# Solo funcinoa con el DEBUG activo.
if settings.DEBUG:
    from django.conf.urls.static import static
    
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
