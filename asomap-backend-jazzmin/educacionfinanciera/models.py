from django.db import models
from django_prose_editor.fields import ProseEditorField


class SavingTip(models.Model):
    """Modelo para consejos de ahorro y educación financiera"""
    title = models.CharField(
        max_length=200,
        verbose_name="Título",
        help_text="Título del consejo de ahorro"
    )
    description = models.TextField(
        verbose_name="Descripción",
        help_text="Descripción breve del consejo"
    )
    content = ProseEditorField(
        extensions={
            "Bold": True,
            "Italic": True,
            "Underline": True,
            "Strike": True,
            "Heading": True,
            "BulletList": True,
            "OrderedList": True,
            "Link": True,
            "Blockquote": True,
            "Code": True,
            "CodeBlock": True,
        },
        sanitize=True,  # Server side sanitization is strongly recommended
        verbose_name="Contenido completo",
        help_text="Contenido detallado del consejo"
    )
    link = models.URLField(
        verbose_name="Enlace",
        help_text="Enlace relacionado con el consejo"
    )
    order = models.PositiveIntegerField(
        default=0,
        verbose_name="Orden",
        help_text="Orden de aparición del consejo"
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="Activo",
        help_text="Indica si el consejo está activo"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Consejo de Ahorro"
        verbose_name_plural = "Consejos de Ahorro"
        ordering = ['order', 'id']

    def __str__(self):
        return f"{self.title} - Orden {self.order}"


class SliderSlide(models.Model):
    """Modelo para slides del slider de educación financiera"""
    image = models.ImageField(
        upload_to='financial-guidance/slider/',
        verbose_name="Imagen",
        help_text="Imagen del slide"
    )
    title = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name="Título",
        help_text="Título del slide (opcional)"
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name="Descripción",
        help_text="Descripción del slide (opcional)"
    )
    order = models.PositiveIntegerField(
        default=0,
        verbose_name="Orden",
        help_text="Orden de aparición del slide"
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="Activo",
        help_text="Indica si el slide está activo"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Slide del Slider"
        verbose_name_plural = "Slides del Slider"
        ordering = ['order', 'id']

    def __str__(self):
        title = self.title or f"Slide {self.id}"
        return f"{title} - Orden {self.order}"

    @property
    def image_url(self):
        """
        Retorna la URL de la imagen para el frontend
        """
        if self.image:
            return self.image.url
        return None


class FAQItem(models.Model):
    """Modelo para preguntas frecuentes de educación financiera"""
    question = models.TextField(
        verbose_name="Pregunta",
        help_text="Pregunta frecuente"
    )
    answer = models.TextField(
        verbose_name="Respuesta",
        help_text="Respuesta a la pregunta frecuente"
    )
    order = models.PositiveIntegerField(
        default=0,
        verbose_name="Orden",
        help_text="Orden de aparición de la pregunta"
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="Activo",
        help_text="Indica si la pregunta está activa"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Pregunta Frecuente"
        verbose_name_plural = "Preguntas Frecuentes"
        ordering = ['order', 'id']

    def __str__(self):
        return f"{self.question[:50]}... - Orden {self.order}"
