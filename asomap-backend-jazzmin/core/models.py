from django.db import models
from django.utils import timezone

class TimeStampedModel(models.Model):
    """
    Abstract base model that provides self-updating created_at and updated_at fields.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class SoftDeleteModel(models.Model):
    """
    Abstract base model that provides soft delete functionality.
    """
    is_active = models.BooleanField(default=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True

    def soft_delete(self):
        self.is_active = False
        self.deleted_at = timezone.now()
        self.save()

    def restore(self):
        self.is_active = True
        self.deleted_at = None
        self.save()


class EmailConfiguration(models.Model):
    """Modelo para configuración de email del sistema"""
    
    PROVIDER_CHOICES = [
        ('gmail', 'Gmail'),
        ('outlook', 'Outlook/Office 365'),
        ('yahoo', 'Yahoo'),
        ('custom', 'Servidor Personalizado'),
    ]
    
    name = models.CharField(
        max_length=100,
        verbose_name="Nombre de la configuración",
        help_text="Nombre descriptivo de esta configuración"
    )
    provider = models.CharField(
        max_length=20,
        choices=PROVIDER_CHOICES,
        verbose_name="Proveedor de email",
        help_text="Proveedor de email a utilizar"
    )
    host = models.CharField(
        max_length=200,
        verbose_name="Servidor SMTP",
        help_text="Servidor SMTP (ej: smtp.gmail.com)"
    )
    port = models.IntegerField(
        default=587,
        verbose_name="Puerto",
        help_text="Puerto del servidor SMTP"
    )
    use_tls = models.BooleanField(
        default=True,
        verbose_name="Usar TLS",
        help_text="Habilitar cifrado TLS"
    )
    username = models.CharField(
        max_length=200,
        verbose_name="Usuario",
        help_text="Dirección de email o usuario"
    )
    password = models.CharField(
        max_length=200,
        verbose_name="Contraseña",
        help_text="Contraseña o contraseña de aplicación"
    )
    from_email = models.CharField(
        max_length=200,
        verbose_name="Email remitente",
        help_text="Email que aparecerá como remitente"
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="Activo",
        help_text="Indica si esta configuración está activa"
    )
    is_default = models.BooleanField(
        default=False,
        verbose_name="Configuración por defecto",
        help_text="Usar esta configuración como predeterminada"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Configuración de Email"
        verbose_name_plural = "Configuraciones de Email"
        ordering = ['-is_default', '-is_active', 'name']

    def __str__(self):
        return f"{self.name} ({self.provider})"
    
    def save(self, *args, **kwargs):
        # Si esta configuración se marca como default, desmarcar las demás
        if self.is_default:
            EmailConfiguration.objects.exclude(pk=self.pk).update(is_default=False)
        super().save(*args, **kwargs)
    
    @property
    def is_configured(self):
        """Verifica si la configuración está completa"""
        return all([
            self.host,
            self.port,
            self.username,
            self.password,
            self.from_email
        ])


class EmailLog(models.Model):
    """Modelo para registrar todos los emails enviados"""
    
    EMAIL_TYPE_CHOICES = [
        ('claim_confirmation', 'Confirmación de Reclamo'),
        ('fraud_confirmation', 'Confirmación de Reporte de Fraude'),
        ('test', 'Email de Prueba'),
        ('system', 'Email del Sistema'),
        ('other', 'Otro'),
    ]
    
    STATUS_CHOICES = [
        ('sent', 'Enviado'),
        ('failed', 'Fallido'),
        ('pending', 'Pendiente'),
    ]
    
    # Información del email
    email_type = models.CharField(
        max_length=50,
        choices=EMAIL_TYPE_CHOICES,
        verbose_name="Tipo de Email",
        help_text="Tipo de email enviado"
    )
    subject = models.CharField(
        max_length=200,
        verbose_name="Asunto",
        help_text="Asunto del email"
    )
    from_email = models.CharField(
        max_length=200,
        verbose_name="Remitente",
        help_text="Email remitente"
    )
    to_email = models.CharField(
        max_length=200,
        verbose_name="Destinatario",
        help_text="Email destinatario"
    )
    
    # Contenido
    message = models.TextField(
        verbose_name="Mensaje",
        help_text="Contenido del email (texto plano)"
    )
    html_message = models.TextField(
        blank=True,
        null=True,
        verbose_name="Mensaje HTML",
        help_text="Contenido HTML del email"
    )
    
    # Estado y seguimiento
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='sent',
        verbose_name="Estado",
        help_text="Estado del envío"
    )
    error_message = models.TextField(
        blank=True,
        null=True,
        verbose_name="Mensaje de Error",
        help_text="Error si el envío falló"
    )
    
    # Información relacionada
    claim_request = models.ForeignKey(
        'prousuario.ClaimRequest',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Solicitud de Reclamo",
        help_text="Reclamo relacionado (si aplica)"
    )
    fraud_report = models.ForeignKey(
        'prousuario.FraudReport',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Reporte de Fraude",
        help_text="Reporte de fraude relacionado (si aplica)"
    )
    email_config = models.ForeignKey(
        EmailConfiguration,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Configuración de Email",
        help_text="Configuración usada para el envío"
    )
    
    # Timestamps
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Fecha de Envío"
    )
    sent_at = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Fecha Real de Envío"
    )

    class Meta:
        verbose_name = "Registro de Email"
        verbose_name_plural = "Registros de Emails"
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['email_type', 'status']),
            models.Index(fields=['created_at']),
            models.Index(fields=['to_email']),
        ]

    def __str__(self):
        return f"{self.email_type} - {self.to_email} - {self.get_status_display()}"
    
    @property
    def is_successful(self):
        """Verifica si el email se envió exitosamente"""
        return self.status == 'sent'
    
    @property
    def delivery_time(self):
        """Calcula el tiempo de entrega"""
        if self.sent_at and self.created_at:
            return self.sent_at - self.created_at
        return None 