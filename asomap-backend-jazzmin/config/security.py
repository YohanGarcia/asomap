from django.core.cache import cache
from django.http import HttpResponseForbidden
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.conf import settings
import logging
import hashlib
import time

logger = logging.getLogger(__name__)
User = get_user_model()

class SecurityMiddleware:
    """Middleware para protección de seguridad"""
    
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        # Rate limiting
        if not self.check_rate_limit(request):
            return HttpResponseForbidden("Demasiadas solicitudes. Intenta de nuevo más tarde.")
        
        # Brute force protection
        if not self.check_brute_force(request):
            return HttpResponseForbidden("Acceso bloqueado por intentos fallidos.")
        
        response = self.get_response(request)
        return response
    
    def check_rate_limit(self, request):
        """Verificar límite de velocidad"""
        if request.path.startswith('/admin/'):
            client_ip = self.get_client_ip(request)
            cache_key = f"rate_limit_{client_ip}"
            
            # Obtener intentos actuales
            attempts = cache.get(cache_key, 0)
            
            # Límite: 100 requests por minuto
            if attempts >= 100:
                return False
            
            # Incrementar contador
            cache.set(cache_key, attempts + 1, 60)
        
        return True
    
    def check_brute_force(self, request):
        """Verificar protección contra fuerza bruta"""
        if request.path.startswith('/admin/login'):
            client_ip = self.get_client_ip(request)
            cache_key = f"login_attempts_{client_ip}"
            
            # Obtener intentos de login
            attempts = cache.get(cache_key, 0)
            
            # Bloquear después de 5 intentos fallidos
            if attempts >= 5:
                return False
        
        return True
    
    def get_client_ip(self, request):
        """Obtener IP del cliente"""
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

class AuditLogger:
    """Sistema de auditoría"""
    
    @staticmethod
    def log_login_attempt(user, success, ip_address):
        """Registrar intento de login"""
        action = "LOGIN_SUCCESS" if success else "LOGIN_FAILED"
        logger.info(f"AUDIT: {action} - User: {user}, IP: {ip_address}, Time: {timezone.now()}")
    
    @staticmethod
    def log_password_change(user, ip_address):
        """Registrar cambio de contraseña"""
        logger.info(f"AUDIT: PASSWORD_CHANGE - User: {user}, IP: {ip_address}, Time: {timezone.now()}")
    
    @staticmethod
    def log_admin_action(user, action, object_type, object_id, ip_address):
        """Registrar acción administrativa"""
        logger.info(f"AUDIT: ADMIN_ACTION - User: {user}, Action: {action}, Object: {object_type}:{object_id}, IP: {ip_address}, Time: {timezone.now()}")

def get_client_ip(request):
    """Función helper para obtener IP del cliente"""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def check_recaptcha(request):
    """Verificar reCAPTCHA (requiere configuración)"""
    if 'g-recaptcha-response' in request.POST:
        # Implementar verificación de reCAPTCHA
        # https://developers.google.com/recaptcha/docs/verify
        return True
    return False 