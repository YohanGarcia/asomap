"""
Configuración específica para manejar archivos grandes
"""
import os
import tempfile
from django.conf import settings

def get_upload_handler_for_large_files():
    """
    Retorna el handler de upload apropiado para archivos grandes
    """
    if not settings.DEBUG:
        # En producción, usar handler que escribe directamente a disco
        return 'django.core.files.uploadhandler.TemporaryFileUploadHandler'
    else:
        # En desarrollo, usar handler por defecto
        return 'django.core.files.uploadhandler.MemoryFileUploadHandler'

def get_temp_dir():
    """
    Retorna el directorio temporal apropiado
    """
    if not settings.DEBUG:
        # En producción, usar directorio temporal del sistema
        return tempfile.gettempdir()
    else:
        # En desarrollo, usar directorio local
        return os.path.join(settings.BASE_DIR, 'temp_uploads')

def validate_file_size(file_size, max_size_mb=50):
    """
    Valida el tamaño del archivo
    """
    max_size_bytes = max_size_mb * 1024 * 1024
    if file_size > max_size_bytes:
        raise ValueError(f"El archivo es demasiado grande. Máximo permitido: {max_size_mb}MB")
    return True
