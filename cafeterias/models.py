from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Cafeteria(models.Model):
    """Modelo para registrar y calificar cafeterías."""

    nombre = models.CharField(
        max_length=120,
        unique=True,
        help_text="Nombre comercial de la cafetería",
    )

    imagen = models.ImageField(
        upload_to="cafeterias/",
        blank=True,
        null=True,
        help_text="Foto de la fachada, logo o ambiente",
    )

    # ⭐ Calificación pública de Google (0-5 con un decimal)
    estrellas_google = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        help_text="Puntuación pública de Google (0 − 5)",
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
    rating_ubicacion = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name="Ubicación / Accesibilidad",
    )

    descripcion = models.TextField(
        blank=True,
        help_text="Breve reseña o comentario",
    )

    fecha_creacion = models.DateTimeField(auto_now_add=True)