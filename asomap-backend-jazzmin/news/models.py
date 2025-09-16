from django.db import models
from django.core.validators import MinValueValidator
from django_prose_editor.fields import ProseEditorField


class News(models.Model):
    """
    Modelo para noticias que coincide con la interfaz INewsSlide del frontend
    """
    # Información básica
    title = models.CharField(
        max_length=200,
        verbose_name="Título",
        help_text="Título de la noticia"
    )
    description = models.TextField(
        verbose_name="Descripción",
        help_text="Descripción breve de la noticia para listas/previews"
    )
    image = models.ImageField(
        upload_to='news/',
        verbose_name="Imagen principal",
        help_text="Imagen principal de la noticia"
    )
    
    # Metadatos
    author = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name="Autor",
        help_text="Autor de la noticia"
    )
    category = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Categoría",
        help_text="Categoría de la noticia"
    )
    tags = models.TextField(
        blank=True,
        verbose_name="Etiquetas",
        help_text="Etiquetas separadas por comas (ej: tecnología, finanzas, innovación)"
    )
    
    # Fechas
    fecha_publicacion = models.DateTimeField(
        verbose_name="Fecha de publicación",
        help_text="Fecha y hora de publicación"
    )
    
    # Contenido completo con ProseEditor
    full_content = ProseEditorField(
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
        help_text="Contenido completo de la noticia con formato enriquecido"
    )
    
    # Media adicional (opcional)
    media_urls = models.TextField(
        blank=True,
        verbose_name="URLs de media adicional",
        help_text="URLs de imágenes/videos separadas por comas"
    )
    
    # Enlaces relacionados (opcional)
    related_links = models.TextField(
        blank=True,
        verbose_name="Enlaces relacionados",
        help_text="URLs de enlaces relacionados separadas por comas"
    )
    
    # Estado
    is_active = models.BooleanField(
        default=True,
        verbose_name="Activo",
        help_text="Indica si la noticia está activa"
    )
    
    # Timestamps
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Fecha de creación"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Fecha de actualización"
    )

    class Meta:
        verbose_name = "Noticia"
        verbose_name_plural = "Noticias"
        ordering = ['-fecha_publicacion']

    def __str__(self):
        return self.title

    @property
    def image_url(self):
        """
        Retorna la URL de la imagen para el frontend
        """
        if self.image:
            return self.image.url
        return None

    @property
    def tags_list(self):
        """
        Retorna las etiquetas como lista para el frontend
        """
        if self.tags:
            return [tag.strip() for tag in self.tags.split(',') if tag.strip()]
        return []

    @property
    def terms_list(self):
        """
        Retorna los términos y condiciones como lista para el frontend
        """
        if self.terms:
            return [term.strip() for term in self.terms.split(',') if term.strip()]
        return []

    @property
    def media_list(self):
        """
        Retorna las URLs de media como lista para el frontend
        """
        if self.media_urls:
            return [url.strip() for url in self.media_urls.split(',') if url.strip()]
        return []

    @property
    def related_links_list(self):
        """
        Retorna los enlaces relacionados como lista para el frontend
        """
        if self.related_links:
            return [link.strip() for link in self.related_links.split(',') if link.strip()]
        return []

    @property
    def valid_until(self):
        """
        Retorna la fecha de fin formateada como 'validUntil' para el frontend
        """
        from django.utils import timezone
        from datetime import datetime
        
        if self.fecha_fin:
            # Formato: "31 de marzo, 2025"
            months = {
                1: 'enero', 2: 'febrero', 3: 'marzo', 4: 'abril',
                5: 'mayo', 6: 'junio', 7: 'julio', 8: 'agosto',
                9: 'septiembre', 10: 'octubre', 11: 'noviembre', 12: 'diciembre'
            }
            
            date = self.fecha_fin
            return f"{date.day} de {months[date.month]}, {date.year}"
        return None

    @property
    def formatted_date(self):
        """
        Retorna la fecha formateada para el frontend
        """
        from django.utils import timezone
        from datetime import datetime
        
        if self.fecha_publicacion:
            # Formato: "21 de septiembre, 2024"
            months = {
                1: 'enero', 2: 'febrero', 3: 'marzo', 4: 'abril',
                5: 'mayo', 6: 'junio', 7: 'julio', 8: 'agosto',
                9: 'septiembre', 10: 'octubre', 11: 'noviembre', 12: 'diciembre'
            }
            
            date = self.fecha_publicacion
            return f"{date.day} de {months[date.month]}, {date.year}"
        return None


class NewsMedia(models.Model):
    """
    Modelo para archivos de media asociados a noticias
    """
    MEDIA_TYPE_CHOICES = [
        ('image', 'Imagen'),
        ('video', 'Video'),
        ('document', 'Documento'),
    ]
    
    news = models.ForeignKey(
        News,
        on_delete=models.CASCADE,
        related_name='media_files',
        verbose_name="Noticia",
        help_text="Noticia a la que pertenece este archivo"
    )
    file = models.FileField(
        upload_to='news/',
        verbose_name="Archivo",
        help_text="Archivo de imagen, video o documento"
    )
    media_type = models.CharField(
        max_length=20,
        choices=MEDIA_TYPE_CHOICES,
        default='image',
        verbose_name="Tipo de media",
        help_text="Tipo de archivo"
    )
    caption = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="Descripción",
        help_text="Descripción o pie de foto del archivo"
    )
    order = models.PositiveIntegerField(
        default=0,
        verbose_name="Orden",
        help_text="Orden de visualización"
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="Activo",
        help_text="Indica si el archivo está activo"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Archivo de Media"
        verbose_name_plural = "Archivos de Media"
        ordering = ['order', 'created_at']

    def __str__(self):
        return f"{self.news.title} - {self.get_media_type_display()}"

    @property
    def file_url(self):
        """
        Retorna la URL del archivo para el frontend
        """
        if self.file:
            return self.file.url
        return None


class Promotion(models.Model):
    """
    Modelo para promociones similar al de News pero con campos adicionales
    """
    # Información básica
    title = models.CharField(
        max_length=200,
        verbose_name="Título",
        help_text="Título de la promoción"
    )
    description = models.TextField(
        verbose_name="Descripción",
        help_text="Descripción breve de la promoción"
    )
    image = models.ImageField(
        upload_to='promotions/',
        null=True,
        blank=True,
        verbose_name="Imagen",
        help_text="Imagen de la promoción"
    )
    
    # Categoría
    category = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Categoría",
        help_text="Categoría de la promoción"
    )
    tags = models.TextField(
        blank=True,
        verbose_name="Etiquetas",
        help_text="Etiquetas separadas por comas (ej: descuento, nuevo cliente, limitado)"
    )
    
    # Fechas
    fecha_inicio = models.DateField(
        verbose_name="Fecha de inicio",
        help_text="Fecha de inicio de la promoción"
    )
    fecha_fin = models.DateField(
        verbose_name="Fecha de fin",
        help_text="Fecha de fin de la promoción"
    )
    
    # Contenido completo con ProseEditor
    full_content = ProseEditorField(
        blank=True,
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
        help_text="Contenido completo de la promoción con formato enriquecido"
    )
    
    # Términos y condiciones
    terms = models.TextField(
        blank=True,
        verbose_name="Términos y condiciones",
        help_text="Términos y condiciones separados por comas"
    )
    
    # Media adicional (opcional)
    media_urls = models.TextField(
        blank=True,
        verbose_name="URLs de media adicional",
        help_text="URLs de imágenes/videos adicionales separadas por comas"
    )
    
    # Enlaces relacionados (opcional)
    related_links = models.TextField(
        blank=True,
        verbose_name="Enlaces relacionados",
        help_text="URLs de enlaces relacionados separadas por comas"
    )
    
    # Estado
    is_active = models.BooleanField(
        default=True,
        verbose_name="Activo",
        help_text="Indica si la promoción está activa"
    )
    
    # Timestamps
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Fecha de creación"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Fecha de actualización"
    )

    class Meta:
        verbose_name = "Promoción"
        verbose_name_plural = "Promociones"
        ordering = ['-fecha_inicio']

    def __str__(self):
        return self.title

    @property
    def image_url(self):
        """
        Retorna la URL de la imagen para el frontend
        """
        if self.image:
            return self.image.url
        return None

    @property
    def tags_list(self):
        """
        Retorna las etiquetas como lista para el frontend
        """
        if self.tags:
            return [tag.strip() for tag in self.tags.split(',') if tag.strip()]
        return []

    @property
    def terms_list(self):
        """
        Retorna los términos y condiciones como lista para el frontend
        """
        if self.terms:
            return [term.strip() for term in self.terms.split(',') if term.strip()]
        return []

    @property
    def media_list(self):
        """
        Retorna las URLs de media como lista para el frontend
        """
        if self.media_urls:
            return [url.strip() for url in self.media_urls.split(',') if url.strip()]
        return []

    @property
    def related_links_list(self):
        """
        Retorna los enlaces relacionados como lista para el frontend
        """
        if self.related_links:
            return [link.strip() for link in self.related_links.split(',') if link.strip()]
        return []

    @property
    def valid_until(self):
        """
        Retorna la fecha de fin formateada como 'validUntil' para el frontend
        """
        from django.utils import timezone
        from datetime import datetime
        
        if self.fecha_fin:
            # Formato: "31 de marzo, 2025"
            months = {
                1: 'enero', 2: 'febrero', 3: 'marzo', 4: 'abril',
                5: 'mayo', 6: 'junio', 7: 'julio', 8: 'agosto',
                9: 'septiembre', 10: 'octubre', 11: 'noviembre', 12: 'diciembre'
            }
            
            date = self.fecha_fin
            return f"{date.day} de {months[date.month]}, {date.year}"
        return None 