from django.db import models

class SocialNetwork(models.Model):
    """
    Modelo para gestionar las redes sociales de la empresa
    """
    name = models.CharField(
        max_length=100,
        verbose_name="Nombre de la red social",
        help_text="Nombre de la red social (ej: Facebook, Instagram, Twitter)"
    )
    url = models.URLField(
        verbose_name="URL de la red social",
        help_text="Enlace completo a la página de la red social"
    )
    icon = models.CharField(
        max_length=50,
        verbose_name="Icono",
        help_text="Nombre del icono de React Icons (ej: FaFacebook, FaInstagram, FaTwitter)"
    )
    order = models.PositiveIntegerField(
        default=0,
        verbose_name="Orden",
        help_text="Orden de visualización (menor número = aparece primero)"
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="Activo",
        help_text="Indica si la red social está activa y se muestra"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Red Social"
        verbose_name_plural = "Redes Sociales"
        ordering = ['order', 'name']

    def __str__(self):
        return f"{self.name} - {self.url}"

class Contact(models.Model):
    """
    Modelo para gestionar la información de contacto de la empresa
    """
    name = models.CharField(
        max_length=100,
        verbose_name="Nombre del contacto",
        help_text="Nombre del tipo de contacto (ej: Teléfono, Email, WhatsApp, Dirección)"
    )
    url = models.URLField(
        verbose_name="URL del contacto",
        help_text="Enlace o valor del contacto (ej: tel:+1234567890, mailto:info@empresa.com, https://wa.me/1234567890)"
    )
    icon = models.CharField(
        max_length=50,
        verbose_name="Icono",
        help_text="Nombre del icono de React Icons (ej: FaPhone, FaEnvelope, FaWhatsapp, FaMapMarkerAlt)"
    )
    order = models.PositiveIntegerField(
        default=0,
        verbose_name="Orden",
        help_text="Orden de visualización (menor número = aparece primero)"
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="Activo",
        help_text="Indica si el contacto está activo y se muestra"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Contacto"
        verbose_name_plural = "Contactos"
        ordering = ['order', 'name']

    def __str__(self):
        return f"{self.name} - {self.url}"

class Footer(models.Model):
    # Secciones del footer
    sections = models.TextField(
        blank=True,
        verbose_name="Secciones del footer",
        help_text="Secciones del footer separadas por comas (ej: Productos, Servicios, Soporte)"
    )
    
    # Información de la empresa
    company_name = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="Nombre de la empresa",
        help_text="Nombre completo de la empresa"
    )
    company_description = models.TextField(
        blank=True,
        verbose_name="Descripción de la empresa",
        help_text="Breve descripción de la empresa"
    )
    company_phone = models.CharField(
        max_length=20,
        blank=True,
        verbose_name="Teléfono de la empresa",
        help_text="Número de teléfono de contacto"
    )
    company_email = models.EmailField(
        blank=True,
        verbose_name="Email de la empresa",
        help_text="Dirección de correo electrónico"
    )
    
    # Información de ubicación
    location_address = models.TextField(
        blank=True,
        verbose_name="Dirección",
        help_text="Dirección física de la empresa"
    )
    location_city = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Ciudad",
        help_text="Ciudad donde se encuentra la empresa"
    )
    location_country = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="País",
        help_text="País donde se encuentra la empresa"
    )
    
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Footer"
        verbose_name_plural = "Footers"

    def __str__(self):
        return "Footer Configuration"

    @property
    def sections_list(self):
        """
        Retorna las secciones como lista para el frontend
        """
        if self.sections:
            return [section.strip() for section in self.sections.split(',') if section.strip()]
        return []

    @property
    def company_dict(self):
        """
        Retorna la información de la empresa como diccionario para el frontend
        """
        return {
            'name': self.company_name,
            'description': self.company_description,
            'phone': self.company_phone,
            'email': self.company_email
        }

    @property
    def location_dict(self):
        """
        Retorna la información de ubicación como diccionario para el frontend
        """
        return {
            'address': self.location_address,
            'city': self.location_city,
            'country': self.location_country
        } 