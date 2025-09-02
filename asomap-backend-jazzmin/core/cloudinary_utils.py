"""
Utilidades para manejar Cloudinary con formatos de imagen modernos
"""
import cloudinary
from django.conf import settings


def configure_cloudinary():
    """Configura Cloudinary con soporte para formatos modernos"""
    if hasattr(settings, 'CLOUDINARY_STORAGE'):
        cloudinary.config(
            cloud_name=settings.CLOUDINARY_STORAGE['CLOUDINARY_CLOUD_NAME'],
            api_key=settings.CLOUDINARY_STORAGE['CLOUDINARY_API_KEY'],
            api_secret=settings.CLOUDINARY_STORAGE['CLOUDINARY_API_SECRET'],
            secure=True
        )


def get_cloudinary_transformation(format_type='image'):
    """Obtiene la transformación de Cloudinary para un tipo específico"""
    if format_type == 'image':
        return {
            'quality': 'auto',
            'fetch_format': 'auto',
            'format': 'auto',
            'flags': 'progressive',
            'delivery_type': 'upload',
        }
    elif format_type == 'video':
        return {
            'quality': 'auto',
            'fetch_format': 'auto',
            'format': 'auto',
            'delivery_type': 'upload',
        }
    return {}


def is_cloudinary_configured():
    """Verifica si Cloudinary está configurado"""
    return hasattr(settings, 'CLOUDINARY_STORAGE') and all([
        settings.CLOUDINARY_STORAGE.get('CLOUDINARY_CLOUD_NAME'),
        settings.CLOUDINARY_STORAGE.get('CLOUDINARY_API_KEY'),
        settings.CLOUDINARY_STORAGE.get('CLOUDINARY_API_SECRET'),
    ])


def get_supported_formats():
    """Obtiene los formatos de imagen soportados"""
    return getattr(settings, 'SUPPORTED_IMAGE_FORMATS', [
        'jpg', 'jpeg', 'png', 'gif', 'webp', 'avif', 'svg'
    ])
