import time
import logging
from django.http import HttpResponse
from django.conf import settings
import os
from django.http import HttpResponse, Http404
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

logger = logging.getLogger(__name__)


class RequestTimeoutMiddleware:
    """
    Middleware para manejar timeouts en subida de archivos
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Solo aplicar timeout en producción
        if not settings.DEBUG:
            # Verificar si es una subida de archivo
            if request.method == 'POST' and request.FILES:
                # Aumentar timeout para subidas de archivo
                request._upload_timeout = 300  # 5 minutos
        
        response = self.get_response(request)
        return response


class FileUploadMiddleware:
    """
    Middleware para optimizar subidas de archivo
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.method == 'POST' and request.FILES:
            # Log de inicio de subida
            logger.info(f"Iniciando subida de archivo: {request.path}")
            start_time = time.time()
            
            # Verificar tamaño de archivos
            total_size = 0
            for uploaded_file in request.FILES.values():
                if hasattr(uploaded_file, 'size'):
                    total_size += uploaded_file.size
                    logger.info(f"Archivo: {uploaded_file.name}, Tamaño: {uploaded_file.size / (1024*1024):.2f} MB")
            
            logger.info(f"Tamaño total de subida: {total_size / (1024*1024):.2f} MB")
            
            try:
                response = self.get_response(request)
                
                # Log de fin de subida
                end_time = time.time()
                duration = end_time - start_time
                logger.info(f"Subida completada en {duration:.2f} segundos")
                
                return response
                
            except Exception as e:
                # Log de error
                end_time = time.time()
                duration = end_time - start_time
                logger.error(f"Error en subida después de {duration:.2f} segundos: {str(e)}")
                raise
        
        return self.get_response(request)


class HealthCheckMiddleware:
    """Middleware para healthcheck que responde antes de cualquier otro middleware."""
    
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Healthcheck endpoints - responder inmediatamente sin autenticación
        if request.path in ['/health/', '/healthcheck/']:
            from django.http import JsonResponse
            return JsonResponse({'status': 'ok'}, status=200)
        
        response = self.get_response(request)
        return response

class PublicMediaMiddleware:
    """Middleware para servir archivos de media públicamente sin autenticación."""
    
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Si la petición es para archivos de media, servir directamente
        if request.path.startswith('/media/'):
            try:
                # Obtener la ruta del archivo relativa a MEDIA_ROOT
                media_path = request.path.replace('/media/', '')
                full_path = os.path.join(settings.MEDIA_ROOT, media_path)
                
                # Verificar que el archivo existe
                if os.path.exists(full_path) and os.path.isfile(full_path):
                    # Servir el archivo directamente
                    with open(full_path, 'rb') as f:
                        content = f.read()
                    
                    # Determinar el tipo MIME basado en la extensión
                    import mimetypes
                    content_type, _ = mimetypes.guess_type(full_path)
                    if content_type is None:
                        content_type = 'application/octet-stream'
                    
                    response = HttpResponse(content, content_type=content_type)
                    
                    # Agregar headers para cache y CORS
                    response['Cache-Control'] = 'public, max-age=31536000'  # 1 año
                    response['Access-Control-Allow-Origin'] = '*'
                    response['Access-Control-Allow-Methods'] = 'GET, HEAD, OPTIONS'
                    response['Access-Control-Allow-Headers'] = 'DNT,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type,Range,Authorization'
                    
                    return response
                else:
                    raise Http404("Archivo no encontrado")
                    
            except Exception as e:
                # Si hay algún error, devolver 404
                raise Http404(f"Error al servir archivo: {str(e)}")
        
        response = self.get_response(request)
        return response 