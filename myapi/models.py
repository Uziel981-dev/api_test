from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone

# Create your models here.
class Almacen(models.Model):
    active = 1
    archived = 0
    draft = 2

    CHOICES_3STATE = (
        (active, 'Activo'),
        (archived, 'Archivado'),
        (draft, 'Borrador')
    )

    name = models.CharField(max_length=40)
    sku = models.CharField(max_length=10, unique=True)
    imagen = models.TextField(max_length=3000)
    tags = models.CharField(max_length=100)
    cost = models.IntegerField(validators=[MinValueValidator(0)])
    status = models.PositiveIntegerField(choices=CHOICES_3STATE, 
        null = True, blank=True, validators=[MinValueValidator(0)])
    talla = models.CharField(max_length=100)
    fecha = models.DateField(default=timezone.now)
    fecha_actualizada = models.DateField(default=timezone.now)





    def __str__(self):
        return self.name