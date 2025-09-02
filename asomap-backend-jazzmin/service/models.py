from django.db import models
from django_prose_editor.fields import ProseEditorField


class ServicesPage(models.Model):
    """
    Modelo principal para la página de servicios bancarios
    """
    title = models.CharField(
        max_length=200,
        verbose_name="Título",
        help_text="Título principal de la página de servicios"
    )
    subtitle = models.CharField(
        max_length=300,
        verbose_name="Subtítulo",
        help_text="Subtítulo descriptivo de la página"
    )

    search_placeholder = models.CharField(
        max_length=100,
        default="Buscar servicios...",
        verbose_name="Texto del Placeholder de Búsqueda",
        help_text="Texto que aparece en el campo de búsqueda"
    )
    no_results_text = models.CharField(
        max_length=100,
        default="No se encontraron servicios",
        verbose_name="Texto de No Resultados",
        help_text="Texto que aparece cuando no hay resultados"
    )
    internet_banking_url = models.URLField(
        verbose_name="URL de Banca en Línea",
        help_text="URL para acceder a la banca en línea"
    )
    internet_banking_button = models.CharField(
        max_length=100,
        default="Acceder a Banca en Línea",
        verbose_name="Texto del Botón de Banca en Línea",
        help_text="Texto del botón para acceder a banca en línea"
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="Activo",
        help_text="Indica si la página está activa"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Página de Servicios"
        verbose_name_plural = "Páginas de Servicios"
        ordering = ['-created_at']

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        # Asegurar que solo haya una página activa
        if self.is_active:
            ServicesPage.objects.exclude(pk=self.pk).update(is_active=False)
        super().save(*args, **kwargs)


class ServiceInfo(models.Model):
    """
    Modelo para información detallada de cada servicio
    """
    services_page = models.ForeignKey(
        ServicesPage,
        on_delete=models.CASCADE,
        related_name='item_details',
        verbose_name="Página de Servicios",
        help_text="Página a la que pertenece este servicio"
    )
    title = models.CharField(
        max_length=200,
        verbose_name="Título del Servicio",
        help_text="Nombre del servicio"
    )
    description = models.TextField(
        verbose_name="Descripción",
        help_text="Descripción detallada del servicio"
    )
    steps = ProseEditorField(
        extensions={
            "Bold": True, "Italic": True, "Underline": True, "Strike": True, "Heading": True,
            "BulletList": True, "OrderedList": True, "Link": True, "Blockquote": True,
            "Code": True, "CodeBlock": True,
        },
        sanitize=True,
        verbose_name="Pasos",
        help_text="Pasos para usar el servicio (puedes usar listas con viñetas)"
    )
    image = models.ImageField(
        upload_to='services/',
        blank=True,
        null=True,
        verbose_name="Imagen",
        help_text="Imagen representativa del servicio"
    )
    image_alt = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name="Texto Alternativo de la Imagen",
        help_text="Texto alternativo para la imagen"
    )
    pdf_file = models.FileField(
        upload_to='services/pdfs/',
        blank=True,
        null=True,
        verbose_name="Archivo PDF",
        help_text="Archivo PDF relacionado con el servicio"
    )
    pdf_url = models.URLField(
        blank=True,
        null=True,
        verbose_name="URL del PDF",
        help_text="URL externa del archivo PDF"
    )
    order = models.PositiveIntegerField(
        default=0,
        verbose_name="Orden",
        help_text="Orden de aparición del servicio"
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="Activo",
        help_text="Indica si el servicio está activo"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Información de Servicio"
        verbose_name_plural = "Información de Servicios"
        ordering = ['order', 'title']

    def __str__(self):
        return self.title
    
    @property
    def image_url(self):
        """Retorna la URL de la imagen"""
        if self.image:
            return self.image.url
        return None
    
    @property
    def pdf_file_url(self):
        """Retorna la URL del archivo PDF subido"""
        if self.pdf_file:
            return self.pdf_file.url
        return None
