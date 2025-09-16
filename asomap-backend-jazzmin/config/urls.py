"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

from django.http import JsonResponse

def health_check(request):
    """Healthcheck mínimo: siempre 200 sin tocar BD ni inicializar nada extra."""
    return JsonResponse({'status': 'ok'}, status=200)

urlpatterns = [
    # Healthcheck endpoints - MÁXIMA PRIORIDAD
    path('health/', health_check, name='health_check'),
    path('healthcheck/', health_check, name='health_check_alt'),
]

# Servir archivos de media PRIMERO (antes de las APIs)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# API URLs
urlpatterns += [
    path('api/', include('about.urls')),
    path('api/', include('news.urls')),
    path('api/', include('products.urls')),
    path('api/', include('header.urls')),
    path('api/', include('layout.urls')),
    path('api/', include('home.urls')),
    path('api/', include('locations.urls')),
    path('api/financial-guidance/', include('educacionfinanciera.urls')),
    path('api/', include('prousuario.urls')),
    path('api/', include('service.urls')),
    
    # API Documentation (Swagger/OpenAPI)
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    
    # Admin por defecto de Django - RUTA PRINCIPAL (última prioridad)
    path('', admin.site.urls),
]

# Servir archivos estáticos
if settings.DEBUG:
    # En desarrollo, servir desde STATICFILES_DIRS
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
else:
    # En producción, WhiteNoise se encarga de servir archivos estáticos
    # pero agregamos fallback para casos específicos
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
