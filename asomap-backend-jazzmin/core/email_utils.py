from django.core.mail import send_mail
from django.conf import settings
from .models import EmailConfiguration


def get_active_email_config():
    """
    Obtiene la configuración de email activa desde la base de datos
    """
    try:
        # Primero intentar obtener la configuración por defecto
        config = EmailConfiguration.objects.filter(
            is_active=True,
            is_default=True
        ).first()
        
        # Si no hay configuración por defecto, obtener la primera activa
        if not config:
            config = EmailConfiguration.objects.filter(
                is_active=True
            ).first()
        
        return config
    except Exception as e:
        print(f"Error obteniendo configuración de email: {str(e)}")
        return None


def send_email_with_db_config(subject, message, recipient_list, html_message=None, fail_silently=True, email_type='other', claim_request=None, fraud_report=None):
    """
    Envía email usando la configuración de la base de datos y registra el envío
    """
    from django.utils import timezone
    from .models import EmailLog
    
    config = get_active_email_config()
    
    # Crear registro de email
    email_log = EmailLog.objects.create(
        email_type=email_type,
        subject=subject,
        from_email=config.from_email if config else '',
        to_email=', '.join(recipient_list),
        message=message,
        html_message=html_message,
        claim_request=claim_request,
        fraud_report=fraud_report,
        email_config=config,
        status='pending'
    )
    
    if not config or not config.is_configured:
        email_log.status = 'failed'
        email_log.error_message = "No hay configuración de email válida"
        email_log.save()
        
        if fail_silently:
            print("No hay configuración de email válida")
            return False
        else:
            raise Exception("No hay configuración de email válida")
    
    try:
        # Configurar temporalmente los settings de email
        original_settings = {
            'EMAIL_HOST': getattr(settings, 'EMAIL_HOST', ''),
            'EMAIL_PORT': getattr(settings, 'EMAIL_PORT', 587),
            'EMAIL_USE_TLS': getattr(settings, 'EMAIL_USE_TLS', True),
            'EMAIL_HOST_USER': getattr(settings, 'EMAIL_HOST_USER', ''),
            'EMAIL_HOST_PASSWORD': getattr(settings, 'EMAIL_HOST_PASSWORD', ''),
            'DEFAULT_FROM_EMAIL': getattr(settings, 'DEFAULT_FROM_EMAIL', ''),
        }
        
        # Aplicar configuración de la base de datos
        settings.EMAIL_HOST = config.host
        settings.EMAIL_PORT = config.port
        settings.EMAIL_USE_TLS = config.use_tls
        settings.EMAIL_HOST_USER = config.username
        settings.EMAIL_HOST_PASSWORD = config.password
        settings.DEFAULT_FROM_EMAIL = config.from_email
        
        # Enviar email
        result = send_mail(
            subject=subject,
            message=message,
            from_email=config.from_email,
            recipient_list=recipient_list,
            html_message=html_message,
            fail_silently=fail_silently,
        )
        
        # Actualizar registro
        email_log.status = 'sent' if result else 'failed'
        email_log.sent_at = timezone.now()
        email_log.save()
        
        # Restaurar configuración original
        for key, value in original_settings.items():
            setattr(settings, key, value)
        
        return result
        
    except Exception as e:
        # Actualizar registro con error
        email_log.status = 'failed'
        email_log.error_message = str(e)
        email_log.save()
        
        print(f"Error enviando email: {str(e)}")
        if not fail_silently:
            raise
        return False


def test_email_configuration(config_id=None):
    """
    Prueba una configuración de email específica
    """
    try:
        if config_id:
            config = EmailConfiguration.objects.get(id=config_id)
        else:
            config = get_active_email_config()
        
        if not config:
            return False, "No hay configuración de email disponible"
        
        if not config.is_configured:
            return False, "La configuración no está completa"
        
        # Enviar email de prueba
        result = send_email_with_db_config(
            subject='Prueba de Configuración - ASOMAP',
            message='Esta es una prueba de la configuración de email.',
            recipient_list=[config.username],  # Enviar al email configurado
            fail_silently=False,
            email_type='test'
        )
        
        if result:
            return True, "Email de prueba enviado exitosamente"
        else:
            return False, "Error al enviar email de prueba"
            
    except Exception as e:
        return False, f"Error: {str(e)}"
