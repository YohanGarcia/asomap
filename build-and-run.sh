#!/bin/bash

echo "🚀 Construyendo y ejecutando ASOMAP con Docker Compose..."

# Verificar si Docker está ejecutándose
if ! docker info > /dev/null 2>&1; then
    echo "❌ Docker no está ejecutándose. Por favor, inicia Docker primero."
    exit 1
fi

# Verificar si Docker Compose está disponible
if ! docker compose version &> /dev/null; then
    echo "❌ Docker Compose no está disponible. Por favor, verifica la instalación."
    exit 1
fi

# Verificar si existe el archivo .env
if [ ! -f .env ]; then
    echo "⚠️  Archivo .env no encontrado. Copiando desde env.example..."
    cp env.example .env
    echo "✅ Archivo .env creado. Revisa y modifica las variables según necesites."
fi

# Verificar que las variables de entorno estén configuradas
echo "🔍 Verificando configuración del servidor..."
if [ -f .env ]; then
    source .env
    if [ -z "$SERVER_IP" ]; then
        echo "❌ SERVER_IP no está configurada en .env"
        echo "💡 Configura SERVER_IP=192.168.54.10 en tu archivo .env"
        exit 1
    fi
    echo "✅ Servidor configurado para IP: $SERVER_IP"
else
    echo "❌ No se pudo cargar el archivo .env"
    exit 1
fi

# Construir el frontend usando el script existente
echo "📦 Construyendo frontend..."
if [ -f "build-frontend.sh" ]; then
    ./build-frontend.sh
else
    echo "⚠️  build-frontend.sh no encontrado, construyendo manualmente..."
    cd asomap-ui-main
    yarn install
    yarn build
    cd ..
fi

# Construir las imágenes Docker
echo "🐳 Construyendo imágenes Docker..."
docker compose build

if [ $? -ne 0 ]; then
    echo "❌ Error al construir las imágenes. Revisa los logs."
    exit 1
fi

# Ejecutar los servicios en modo producción
echo "🚀 Iniciando servicios en modo producción..."
docker compose --profile prod up -d

if [ $? -ne 0 ]; then
    echo "❌ Error al iniciar los servicios. Revisa los logs."
    exit 1
fi

echo "✅ Servicios iniciados exitosamente!"
echo ""
echo "🌐 URLs disponibles:"
echo "   • Aplicación principal: http://$SERVER_IP:8080"
echo "   • Backend API: http://$SERVER_IP:8000"
echo "   • Admin de Django: http://$SERVER_IP:8080/admin"
echo "   • API Swagger: http://$SERVER_IP:8000/api/schema/swagger-ui/"
echo "   • Health Check: http://$SERVER_IP:8000/health/"
echo ""
echo "📋 Comandos útiles:"
echo "   • Ver logs: docker compose logs -f"
echo "   • Detener servicios: docker compose down"
echo "   • Reiniciar: docker compose restart"
echo "   • Ver estado: docker compose ps"
echo ""

# Esperar un momento para que los servicios se inicien
echo "⏳ Esperando que los servicios se inicien..."
sleep 15

# Verificar el estado de los servicios
echo "🔍 Verificando estado de los servicios..."
docker compose ps

echo ""
echo "🎉 ¡ASOMAP está listo en modo producción!"
echo ""
echo "🔧 Configuración aplicada:"
echo "   • IP del servidor: $SERVER_IP"
echo "   • ALLOWED_HOSTS: Configurado para $SERVER_IP"
echo "   • CSRF_TRUSTED_ORIGINS: Configurado para $SERVER_IP"
echo "   • CORS_ALLOWED_ORIGINS: Configurado para $SERVER_IP"
echo "   • CORS_ORIGIN_ALLOW_ALL: $(if [ "$DEBUG" = "False" ]; then echo "False (Producción)"; else echo "True (Desarrollo)"; fi)"
echo "   • CORS_ALLOW_CREDENTIALS: $(if [ "$DEBUG" = "False" ]; then echo "True (Producción)"; else echo "False (Desarrollo)"; fi)"
echo ""
echo "💡 Para modo desarrollo: ./dev-mode.sh"
echo "💡 Para ver logs: docker compose logs -f"
