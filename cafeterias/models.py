from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Cafeteria(models.Model):
    """Modelo para registrar y calificar cafeterías."""

    nombre = models.CharField(
        max_length=120,
        unique=True,
        help_text="Nombre de la cafetería",
    )

    imagen = models.URLField(
        blank=True,
        null=True,
        help_text="Imagen de referencia",
    )

    # ⭐ Calificación Personal (0-5 con un decimal)
    estrellas_puntuacion = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        help_text="Puntuación personal (0 − 5)",
    )

    # ⭐ Valoraciones propias (1-5)
    rating_comida = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name="Calidad de la comida",
    )
    rating_atencion = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name="Atención del personal",
    )
    rating_precio = models.PositiveSmallIntegerField(
        default= 0,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name="Precio",
    )
    rating_ubicacion = models.URLField(
    verbose_name="Ubicación",
    help_text="Enlace a la ubicación (ej. Google Maps)"
)


    descripcion = models.TextField(
        blank=True,
        help_text="Breve reseña o comentario",
    )

    fecha_creacion = models.DateTimeField(auto_now_add=True)