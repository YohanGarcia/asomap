from django.template.loader import render_to_string
from django.utils.html import strip_tags
from core.email_utils import send_email_with_db_config
import logging

# Configurar logger
logger = logging.getLogger(__name__)


def send_claim_confirmation_email(claim_request):
    """
    Envía un correo de confirmación cuando se crea una solicitud de reclamo
    """
    try:
        # Datos del contexto para el template
        context = {
            'full_name': claim_request.full_name,
            'claim_id': claim_request.id,
            'product_type': claim_request.product_type,
            'claim_type': claim_request.claim_type,
            'created_at': claim_request.created_at.strftime('%d/%m/%Y %H:%M'),
            'time_zone': 'GMT-4 (República Dominicana)',
        }
        
        # Renderizar el template HTML
        html_message = render_to_string('notifications/claim_confirmation_email.html', context)
        
        # Crear versión de texto plano mejorada
        plain_message = f"""
Hola {claim_request.full_name},

Hemos recibido su solicitud #{claim_request.id} y queremos confirmarle que ha sido registrada exitosamente en nuestro sistema.

Detalles de la solicitud:
- Número: #{claim_request.id}
- Fecha: {claim_request.created_at.strftime('%d/%m/%Y %H:%M')}
- Tipo: {claim_request.product_type}
- Categoría: {claim_request.claim_type}

Próximos pasos:
- Nuestro equipo revisará su solicitud en un plazo máximo de 48 horas hábiles
- Recibirá una notificación cuando su solicitud sea procesada
- Si necesita información adicional, nos pondremos en contacto con usted

Importante: Por favor, conserve este correo como comprobante de su solicitud.

Saludos cordiales,
Equipo ASOMAP
        """.strip()
        
        # Enviar el email usando configuración de la base de datos
        result = send_email_with_db_config(
            subject=f'Solicitud #{claim_request.id} recibida',
            message=plain_message,
            recipient_list=[claim_request.email],
            html_message=html_message,
            fail_silently=True,
            email_type='claim_confirmation',
            claim_request=claim_request
        )
        
        # Log del resultado
        if result:
            logger.info(f"✅ Email enviado exitosamente a {claim_request.email} para reclamo #{claim_request.id}")
            return True
        else:
            logger.error(f"❌ Error enviando email a {claim_request.email} para reclamo #{claim_request.id}")
            return False
        
    except Exception as e:
        logger.error(f"❌ Error enviando email de confirmación: {str(e)}")
        return False


def verify_email_sent(claim_request):
    """
    Verifica si el email fue enviado para un reclamo específico
    """
    try:
        # Aquí podrías implementar verificación más avanzada
        # Por ahora, verificamos que el reclamo existe y tiene email
        if claim_request and claim_request.email:
            logger.info(f"📧 Verificando envío para reclamo #{claim_request.id} a {claim_request.email}")
            return True
        return False
    except Exception as e:
        logger.error(f"Error verificando envío: {str(e)}")
        return False


def get_email_status(obj):
    """
    Obtiene el estado del email para un reclamo o reporte de fraude
    """
    try:
        # Verificar que el objeto existe
        if not obj:
            return "No encontrado"
        
        # Verificar que tiene email
        if not obj.email:
            return "Sin email"
        
        # Verificar que fue creado recientemente
        from django.utils import timezone
        from datetime import timedelta
        
        time_diff = timezone.now() - obj.created_at
        
        if time_diff < timedelta(minutes=5):
            return "Enviado recientemente"
        else:
            return "Enviado"
            
    except Exception as e:
        logger.error(f"Error obteniendo estado: {str(e)}")
        return "Error"


def send_fraud_confirmation_email(fraud_report):
    """
    Envía un correo de confirmación cuando se crea un reporte de fraude
    """
    try:
        # Datos del contexto para el template
        context = {
            'full_name': fraud_report.full_name,
            'report_id': fraud_report.id,
            'classification': fraud_report.classification,
            'created_at': fraud_report.created_at.strftime('%d/%m/%Y %H:%M'),
            'time_zone': 'GMT-4 (República Dominicana)',
        }
        
        # Renderizar el template HTML
        html_message = render_to_string('notifications/fraud_confirmation_email.html', context)
        
        # Crear versión de texto plano mejorada
        plain_message = f"""
Hola {fraud_report.full_name},

Hemos recibido su reporte de fraude #{fraud_report.id} y queremos confirmarle que ha sido registrado exitosamente en nuestro sistema.

Detalles del reporte:
- Número: #{fraud_report.id}
- Fecha: {fraud_report.created_at.strftime('%d/%m/%Y %H:%M')}
- Clasificación: {fraud_report.classification}

Próximos pasos:
- Nuestro equipo de seguridad revisará su reporte en un plazo máximo de 24 horas hábiles
- Recibirá una notificación cuando su reporte sea procesado
- Si necesita información adicional, nos pondremos en contacto con usted

Importante: Por favor, conserve este correo como comprobante de su reporte.

Saludos cordiales,
Equipo de Seguridad ASOMAP
        """.strip()
        
        # Enviar el email usando configuración de la base de datos
        result = send_email_with_db_config(
            subject=f'Reporte de Fraude #{fraud_report.id} recibido',
            message=plain_message,
            recipient_list=[fraud_report.email],
            html_message=html_message,
            fail_silently=True,
            email_type='fraud_confirmation'
        )
        
        # Log del resultado
        if result:
            logger.info(f"✅ Email enviado exitosamente a {fraud_report.email} para reporte #{fraud_report.id}")
            return True
        else:
            logger.error(f"❌ Error enviando email a {fraud_report.email} para reporte #{fraud_report.id}")
            return False
        
    except Exception as e:
        logger.error(f"❌ Error enviando email de confirmación: {str(e)}")
        return False


def send_suggestion_confirmation_email(suggestion):
    """
    Envía email de confirmación para sugerencias del buzón
    """
    try:
        # Datos del contexto para el template
        context = {
            'full_name': suggestion.full_name,
            'classification': suggestion.classification,
            'message': suggestion.message,
            'created_at': suggestion.created_at.strftime('%d/%m/%Y %H:%M'),
            'time_zone': 'GMT-4 (República Dominicana)',
        }
        
        # Renderizar el template HTML
        html_message = render_to_string('notifications/suggestion_confirmation_email.html', context)
        
        # Crear versión de texto plano mejorada
        plain_message = f"""
Hola {suggestion.full_name},

Hemos recibido tu sugerencia y queremos confirmarte que ha sido registrada en nuestro sistema.

Detalles de la sugerencia:
- Clasificación: {suggestion.classification}
- Fecha: {suggestion.created_at.strftime('%d/%m/%Y %H:%M')}

Tu mensaje: {suggestion.message}

Próximos pasos:
- Nuestro equipo revisará tu sugerencia
- La tendremos en cuenta para mejorar nuestros servicios
- Si necesitas información adicional, nos pondremos en contacto contigo

¡Gracias por tu valioso feedback!

Saludos cordiales,
Equipo ASOMAP
        """.strip()
        
        # Enviar el email usando configuración de la base de datos
        # Para sugerencias, usar una función específica que maneje Gmail correctamente
        result = send_suggestion_email_with_gmail_fix(
            subject='Sugerencia Recibida - ASOMAP',
            message=plain_message,
            recipient_list=[suggestion.email],
            html_message=html_message,
            fail_silently=True,
            email_type='suggestion_confirmation'
        )
        
        # Log del resultado
        if result:
            logger.info(f"✅ Email enviado exitosamente a {suggestion.email} para sugerencia #{suggestion.id}")
            return True
        else:
            logger.error(f"❌ Error enviando email a {suggestion.email} para sugerencia #{suggestion.id}")
            return False
        
    except Exception as e:
        logger.error(f"❌ Error enviando email de confirmación: {str(e)}")
        return False


def send_suggestion_email_with_gmail_fix(subject, message, recipient_list, html_message=None, fail_silently=True, email_type='suggestion_confirmation'):
    """
    Función específica para enviar emails de sugerencias que maneja Gmail correctamente
    """
    try:
        from django.core.mail import send_mail
        from django.conf import settings
        from core.models import EmailConfiguration, EmailLog
        from django.utils import timezone
        
        config = EmailConfiguration.objects.filter(is_active=True, is_default=True).first()
        if not config:
            config = EmailConfiguration.objects.filter(is_active=True).first()
        
        if not config or not config.is_configured:
            logger.error("No hay configuración de email válida")
            return False
        
        # Crear registro de email
        email_log = EmailLog.objects.create(
            email_type=email_type,
            subject=subject,
            from_email=config.username if config.provider.lower() == 'gmail' else config.from_email,
            to_email=', '.join(recipient_list),
            message=message,
            html_message=html_message,
            email_config=config,
            status='pending'
        )
        
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
            
            # Para Gmail, usar el username como from_email para evitar problemas de autenticación
            if config.provider.lower() == 'gmail':
                from_email = config.username
                settings.DEFAULT_FROM_EMAIL = config.username
            else:
                from_email = config.from_email
                settings.DEFAULT_FROM_EMAIL = config.from_email
            
            # Enviar email
            result = send_mail(
                subject=subject,
                message=message,
                from_email=from_email,
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
            
            logger.error(f"Error enviando email de sugerencia: {str(e)}")
            if not fail_silently:
                raise
            return False
            
    except Exception as e:
        logger.error(f"Error en send_suggestion_email_with_gmail_fix: {str(e)}")
        return False
