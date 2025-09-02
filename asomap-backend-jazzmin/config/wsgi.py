"""
WSGI config for asomap_backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_wsgi_application()

# Configurar WhiteNoise para servir archivos estáticos en producción
if not settings.DEBUG:
    try:
        from whitenoise import WhiteNoise
        application = WhiteNoise(application, root=settings.STATIC_ROOT)
        application.add_files(settings.STATIC_ROOT, prefix='static/')
    except ImportError:
        pass  # WhiteNoise no está instalado
