# Solución para Worker Timeout en Subida de Archivos

## 🔍 **Problema Identificado**
- **Error**: `WORKER TIMEOUT (pid:9)` en producción
- **Causa**: Subida de archivos grandes excede el timeout por defecto de Gunicorn (30s)
- **Impacto**: Los archivos no se suben correctamente

## ✅ **Soluciones Implementadas**

### 1. **Configuración de Gunicorn Optimizada**
- **Archivo**: `gunicorn.conf.py`
- **Timeout**: Aumentado a 300 segundos (5 minutos)
- **Workers**: Configurados para manejar archivos grandes
- **Memoria**: Uso de `/dev/shm` para archivos temporales

### 2. **Configuración de Django**
- **Límites de archivo**: 10MB máximo
- **Directorio temporal**: `temp_uploads/`
- **Cloudinary**: Configuración optimizada para archivos grandes

### 3. **Middleware Personalizado**
- **RequestTimeoutMiddleware**: Maneja timeouts específicos para uploads
- **FileUploadMiddleware**: Logs y optimización de subidas
- **HealthCheckMiddleware**: Respuestas rápidas para health checks

### 4. **Configuración de Cloudinary**
```python
CLOUDINARY_STORAGE = {
    'CLOUDINARY_CLOUD_NAME': cloudinary_cloud_name,
    'CLOUDINARY_API_KEY': cloudinary_api_key,
    'CLOUDINARY_API_SECRET': cloudinary_api_secret,
    'CLOUDINARY_UPLOAD_PRESET': config('CLOUDINARY_UPLOAD_PRESET', default=''),
    'CLOUDINARY_FOLDER': 'asomap_backend',
    'CLOUDINARY_TRANSFORMATION': {
        'quality': 'auto',
        'fetch_format': 'auto',
    },
    'SECURE': True,
}
```

## 🚀 **Variables de Entorno Requeridas**

### Para Railway/Producción:
```bash
# Cloudinary (opcional, si no está configurado usa almacenamiento local)
CLOUDINARY_CLOUD_NAME=tu_cloud_name
CLOUDINARY_API_KEY=tu_api_key
CLOUDINARY_API_SECRET=tu_api_secret
CLOUDINARY_UPLOAD_PRESET=tu_upload_preset

# Django
DJANGO_SETTINGS_MODULE=config.settings
DEBUG=False
```

## 📋 **Comandos de Despliegue**

### Railway:
```bash
# El Procfile ya está configurado para usar gunicorn.conf.py
railway up
```

### Local (para testing):
```bash
# Crear directorio temporal
mkdir -p temp_uploads

# Ejecutar con configuración de producción
gunicorn config.wsgi:application --config gunicorn.conf.py --bind 0.0.0.0:8000
```

## 🔧 **Monitoreo y Logs**

### Logs de Subida:
- Los middleware registran inicio y fin de subidas
- Duración de cada subida
- Errores específicos de timeout

### Health Checks:
- Respuestas rápidas para `/health/` y `/healthcheck/`
- No afectan el rendimiento de subidas

## ⚠️ **Consideraciones**

### Límites de Archivo:
- **Máximo**: 10MB por archivo
- **Formato**: PDF, imágenes (JPG, PNG, etc.)
- **Compresión**: Automática en Cloudinary

### Timeouts:
- **Gunicorn**: 300 segundos (5 minutos)
- **Django**: 10MB en memoria
- **Cloudinary**: Optimización automática

### Fallback:
- Si Cloudinary no está configurado, usa almacenamiento local
- Los archivos se guardan en `media/` localmente

## 🎯 **Resultado Esperado**
- ✅ Subidas de archivos exitosas sin timeouts
- ✅ Logs detallados para debugging
- ✅ Optimización automática de archivos
- ✅ Fallback a almacenamiento local si es necesario
