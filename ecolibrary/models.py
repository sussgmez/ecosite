from django.db import models
from tinymce import models as tinymce_models
from django.utils.translation import gettext_lazy as _ 

STATES = [
    (0, 'Amazonas'),
    (1, 'Anzoátegui'),
    (2, 'Apure'),
    (3, 'Aragua'),
    (4, 'Barinas'),
    (5, 'Bolívar'),
    (6, 'Carabobo'),
    (7, 'Cojedes'),
    (8, 'Delta Amacuro'),
    (9, 'Distrito Capital'),
    (10, 'Falcón'),
    (11, 'Guárico'),
    (12, 'Lara'),
    (13, 'Mérida'),
    (14, 'Miranda'),
    (15, 'Monagas'),
    (16, 'Nueva Esparta'),
    (17, 'Portuguesa'),
    (18, 'Sucre'),
    (19, 'Táchira'),
    (20, 'Trujillo'),
    (21, 'Vargas'),
    (22, 'Yaracuy'),
    (23, 'Zulia'),
]


class Site(models.Model):
    name = models.CharField(_("Nombre"), max_length=300)
    content = tinymce_models.HTMLField("Contenido", blank=True, null=True)
    image = models.ImageField(_("Imagen"), upload_to='sites/')
    state = models.IntegerField(_("Estado"), choices=STATES)
    established = models.DateField(_("Fecha Establecido"), blank=True, null=True)
    
    def __str__(self):
        return self.name

class NationalPark(Site):

    def get_cname(self):
        class_name = 'national_park'
        return class_name

class NaturalMonument(Site):

    def get_cname(self):
        class_name = 'natural_monument'
        return class_name

