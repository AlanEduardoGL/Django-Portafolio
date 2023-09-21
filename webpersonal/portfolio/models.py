from django.db import models

# Create your models here.


class Proyect(models.Model):
    title = models.CharField(max_length=50, verbose_name="Titulo")
    description = models.TextField(verbose_name="Descripcion")
    image = models.ImageField(verbose_name="Imagen", upload_to="proyect")
    link = models.URLField(null=True, blank=True, verbose_name="Link del proyecto")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualizacion")

    # Agregamos meta datos extendidos.
    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["-created"] # Campo de ordenamiento par nuestros registros. Del mas nuevo al antiguo.

    # Devolvemos el nombre del proyecto.
    def __str__(self):
        return self.title
