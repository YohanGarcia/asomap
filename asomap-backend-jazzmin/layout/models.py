from django.db import models

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