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

# Construir el frontend primero
echo "📦 Construyendo frontend..."
cd asomap-ui-main
yarn install
yarn build
cd ..

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
echo "   • Aplicación principal: http://localhost:8080"
echo "   • Backend API: http://localhost:8000"
echo "   • Admin de Django: http://localhost:8080/admin"
echo "   • API Swagger: http://localhost:8000/api/schema/swagger-ui/"
echo "   • Health Check: http://localhost:8000/health/"
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
echo "💡 Para modo desarrollo: ./asomap/dev-mode.sh"
