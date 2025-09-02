from django.db import models


class Service(models.Model):
    """
    Modelo para servicios disponibles en las ubicaciones
    """
    name = models.CharField(
        max_length=100,
        verbose_name="Nombre del servicio",
        help_text="Nombre del servicio disponible"
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Descripción",
        help_text="Descripción opcional del servicio"
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="Activo",
        help_text="Indica si el servicio está activo"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Fecha de creación"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Fecha de actualización"
    )

    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"
        ordering = ['name']

    def __str__(self):
        return self.name


class Schedule(models.Model):
    """
    Modelo para horarios de ubicaciones
    """
    SCHEDULE_CHOICES = [
        # Horarios tempranos
        ('6:00 AM - 4:00 PM', '6:00 AM - 4:00 PM'),
        ('6:30 AM - 4:00 PM', '6:30 AM - 4:00 PM'),
        ('7:00 AM - 4:00 PM', '7:00 AM - 4:00 PM'),
        ('7:30 AM - 4:00 PM', '7:30 AM - 4:00 PM'),
        
        # Horarios estándar mañana
        ('8:00 AM - 4:00 PM', '8:00 AM - 4:00 PM'),
        ('8:00 AM - 4:30 PM', '8:00 AM - 4:30 PM'),
        ('8:00 AM - 5:00 PM', '8:00 AM - 5:00 PM'),
        ('8:30 AM - 4:00 PM', '8:30 AM - 4:00 PM'),
        ('8:30 AM - 4:30 PM', '8:30 AM - 4:30 PM'),
        ('8:30 AM - 5:00 PM', '8:30 AM - 5:00 PM'),
        ('8:30 AM - 5:30 PM', '8:30 AM - 5:30 PM'),
        
        # Horarios estándar tarde
        ('9:00 AM - 4:00 PM', '9:00 AM - 4:00 PM'),
        ('9:00 AM - 4:30 PM', '9:00 AM - 4:30 PM'),
        ('9:00 AM - 5:00 PM', '9:00 AM - 5:00 PM'),
        ('9:00 AM - 5:30 PM', '9:00 AM - 5:30 PM'),
        ('9:00 AM - 6:00 PM', '9:00 AM - 6:00 PM'),
        ('9:30 AM - 5:00 PM', '9:30 AM - 5:00 PM'),
        ('9:30 AM - 5:30 PM', '9:30 AM - 5:30 PM'),
        ('9:30 AM - 6:00 PM', '9:30 AM - 6:00 PM'),
        
        # Horarios extendidos
        ('8:00 AM - 6:00 PM', '8:00 AM - 6:00 PM'),
        ('8:30 AM - 6:00 PM', '8:30 AM - 6:00 PM'),
        ('8:30 AM - 6:30 PM', '8:30 AM - 6:30 PM'),
        ('9:00 AM - 6:30 PM', '9:00 AM - 6:30 PM'),
        ('9:00 AM - 7:00 PM', '9:00 AM - 7:00 PM'),
        
        # Horarios muy tempranos
        ('5:00 AM - 3:00 PM', '5:00 AM - 3:00 PM'),
        ('5:30 AM - 3:00 PM', '5:30 AM - 3:00 PM'),
        ('5:30 AM - 3:30 PM', '5:30 AM - 3:30 PM'),
        ('6:00 AM - 3:00 PM', '6:00 AM - 3:00 PM'),
        ('6:00 AM - 3:30 PM', '6:00 AM - 3:30 PM'),
        
        # Horarios tarde
        ('10:00 AM - 6:00 PM', '10:00 AM - 6:00 PM'),
        ('10:00 AM - 6:30 PM', '10:00 AM - 6:30 PM'),
        ('10:00 AM - 7:00 PM', '10:00 AM - 7:00 PM'),
        ('10:30 AM - 6:00 PM', '10:30 AM - 6:00 PM'),
        ('10:30 AM - 6:30 PM', '10:30 AM - 6:30 PM'),
        ('10:30 AM - 7:00 PM', '10:30 AM - 7:00 PM'),
        
        # Horarios nocturnos
        ('11:00 AM - 7:00 PM', '11:00 AM - 7:00 PM'),
        ('11:00 AM - 8:00 PM', '11:00 AM - 8:00 PM'),
        ('12:00 PM - 8:00 PM', '12:00 PM - 8:00 PM'),
        ('1:00 PM - 9:00 PM', '1:00 PM - 9:00 PM'),
        ('2:00 PM - 10:00 PM', '2:00 PM - 10:00 PM'),
        
        # Horarios muy extendidos
        ('6:00 AM - 10:00 PM', '6:00 AM - 10:00 PM'),
        ('7:00 AM - 10:00 PM', '7:00 AM - 10:00 PM'),
        ('7:00 AM - 11:00 PM', '7:00 AM - 11:00 PM'),
        ('8:00 AM - 10:00 PM', '8:00 AM - 10:00 PM'),
        ('8:00 AM - 11:00 PM', '8:00 AM - 11:00 PM'),
        
        # Horarios especiales
        ('24/7', '24/7 - Siempre abierto'),
        ('6:00 AM - 12:00 AM', '6:00 AM - 12:00 AM'),
        ('7:00 AM - 12:00 AM', '7:00 AM - 12:00 AM'),
        ('8:00 AM - 12:00 AM', '8:00 AM - 12:00 AM'),
        
        # Horarios de fin de semana
        ('Lunes a Viernes 8:00 AM - 5:00 PM', 'Lunes a Viernes 8:00 AM - 5:00 PM'),
        ('Lunes a Viernes 8:30 AM - 5:00 PM', 'Lunes a Viernes 8:30 AM - 5:00 PM'),
        ('Lunes a Viernes 9:00 AM - 6:00 PM', 'Lunes a Viernes 9:00 AM - 6:00 PM'),
        ('Lunes a Viernes 9:00 AM - 5:30 PM', 'Lunes a Viernes 9:00 AM - 5:30 PM'),
        ('Lunes a Sábado 8:00 AM - 5:00 PM', 'Lunes a Sábado 8:00 AM - 5:00 PM'),
        ('Lunes a Sábado 8:30 AM - 5:00 PM', 'Lunes a Sábado 8:30 AM - 5:00 PM'),
        ('Lunes a Sábado 9:00 AM - 6:00 PM', 'Lunes a Sábado 9:00 AM - 6:00 PM'),
        ('Lunes a Sábado 9:00 AM - 5:30 PM', 'Lunes a Sábado 9:00 AM - 5:30 PM'),
    ]
    
    name = models.CharField(
        max_length=100,
        choices=SCHEDULE_CHOICES,
        verbose_name="Horario",
        help_text="Selecciona el horario de la ubicación"
    )
    opening_time = models.TimeField(
        verbose_name="Hora de apertura",
        help_text="Hora de apertura (formato HH:MM)"
    )
    closing_time = models.TimeField(
        verbose_name="Hora de cierre",
        help_text="Hora de cierre (formato HH:MM)"
    )
    is_24_7 = models.BooleanField(
        default=False,
        verbose_name="24/7",
        help_text="Indica si está abierto 24/7"
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="Activo",
        help_text="Indica si el horario está activo"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Fecha de creación"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Fecha de actualización"
    )

    class Meta:
        verbose_name = "Horario"
        verbose_name_plural = "Horarios"
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Si es 24/7, establecer horarios especiales
        if self.is_24_7:
            from datetime import time
            self.opening_time = time(0, 0)  # 00:00
            self.closing_time = time(23, 59)  # 23:59
        super().save(*args, **kwargs)


class Location(models.Model):
    """
    Modelo para ubicaciones (sucursales y cajeros automáticos)
    """
    TYPE_CHOICES = [
        ('branch', 'Sucursal'),
        ('atm', 'Cajero Automático'),
    ]
    
    # Información básica
    type = models.CharField(
        max_length=10,
        choices=TYPE_CHOICES,
        verbose_name="Tipo",
        help_text="Tipo de ubicación"
    )
    name = models.CharField(
        max_length=200,
        verbose_name="Nombre",
        help_text="Nombre de la ubicación"
    )
    address = models.TextField(
        verbose_name="Dirección",
        help_text="Dirección completa de la ubicación"
    )
    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name="Teléfono",
        help_text="Número de teléfono de contacto"
    )
    
    # Coordenadas geográficas
    latitude = models.TextField(
        verbose_name="Latitud",
        help_text="Latitud de la ubicación"
    )
    longitude = models.TextField(
        verbose_name="Longitud",
        help_text="Longitud de la ubicación"
    )
    
    # Horarios - Ahora usando modelo Schedule
    schedule = models.ForeignKey(
        Schedule,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Horario",
        help_text="Horario de la ubicación"
    )
    
    # Servicios - Ahora usando modelo Service
    services = models.ManyToManyField(
        Service,
        blank=True,
        verbose_name="Servicios",
        help_text="Servicios disponibles en esta ubicación"
    )
    
    # Estado
    is_open = models.BooleanField(
        default=True,
        verbose_name="Abierto",
        help_text="Indica si la ubicación está abierta"
    )
    
    # Campos de control
    is_active = models.BooleanField(
        default=True,
        verbose_name="Activo",
        help_text="Indica si la ubicación está activa"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Fecha de creación"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Fecha de actualización"
    )

    class Meta:
        verbose_name = "Ubicación"
        verbose_name_plural = "Ubicaciones"
        ordering = ['type', 'name']

    def __str__(self):
        return f"{self.get_type_display()} - {self.name}"

    @property
    def coordinates(self):
        """
        Retorna las coordenadas en formato para el frontend
        """
        try:
            return {
                'lat': float(self.latitude),
                'lng': float(self.longitude)
            }
        except (ValueError, TypeError):
            return {
                'lat': 0.0,
                'lng': 0.0
            }

    @property
    def hours(self):
        """
        Retorna los horarios en formato para el frontend
        """
        if self.schedule:
            if self.schedule.is_24_7:
                return {
                    'openingTime': '12:00 AM',
                    'closingTime': '11:59 PM'
                }
            else:
                return {
                    'openingTime': self.schedule.opening_time.strftime('%I:%M %p'),
                    'closingTime': self.schedule.closing_time.strftime('%I:%M %p')
                }
        return None

    @property
    def services_list(self):
        """
        Retorna la lista de servicios en formato para el frontend
        """
        return [service.name for service in self.services.filter(is_active=True)]
