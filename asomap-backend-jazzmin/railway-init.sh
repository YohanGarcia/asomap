#!/bin/bash

# Script de inicialización para Railway
echo "🚀 Iniciando despliegue en Railway..."

# Verificar si estamos en producción
if [ "$RAILWAY_ENVIRONMENT" = "production" ]; then
    echo "📦 Entorno de producción detectado"
    
    # Instalar dependencias
    echo "📥 Instalando dependencias..."
    pip install -r requirements.txt
    
    # Aplicar migraciones
    echo "🗄️  Aplicando migraciones..."
    python manage.py migrate --noinput
    
    # Crear directorios necesarios
    echo "📁 Creando directorios necesarios..."
    mkdir -p media
    mkdir -p temp_uploads
    mkdir -p staticfiles
    
    # Recolectar archivos estáticos
    echo "📁 Recolectando archivos estáticos..."
    python manage.py collectstatic --noinput --clear
    
    # Verificar que los archivos estáticos se recolectaron
    echo "✅ Verificando archivos estáticos..."
    ls -la staticfiles/
    
    # Verificar directorios temporales
    echo "✅ Verificando directorios temporales..."
    ls -la temp_uploads/ || echo "Directorio temp_uploads creado"
    echo "Directorio temporal del sistema: $(python -c 'import tempfile; print(tempfile.gettempdir())')"
    
    echo "🎉 Inicialización completada"
else
    echo "🔧 Entorno de desarrollo detectado"
    
    # Solo instalar dependencias en desarrollo
    pip install -r requirements.txt
fi

# Ejecutar el servidor
echo "🌐 Iniciando servidor..."
exec gunicorn config.wsgi:application --config gunicorn.conf.py --bind 0.0.0.0:$PORT
