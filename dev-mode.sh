#!/bin/bash

echo "🔧 Iniciando ASOMAP en modo desarrollo..."

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

# Detener servicios de producción si están ejecutándose
echo "🛑 Deteniendo servicios de producción..."
docker compose --profile prod down

# Construir las imágenes para desarrollo
echo "📦 Construyendo imágenes para desarrollo..."
docker compose build

if [ $? -ne 0 ]; then
    echo "❌ Error al construir las imágenes. Revisa los logs."
    exit 1
fi

# Ejecutar servicios de desarrollo
echo "🚀 Iniciar servicios de desarrollo..."
docker compose --profile dev up -d

if [ $? -ne 0 ]; then
    echo "❌ Error al iniciar los servicios. Revisa los logs."
    exit 1
fi

echo "✅ Servicios de desarrollo iniciados exitosamente!"
echo ""
echo "🌐 URLs disponibles:"
echo "   • Frontend (Vite con Hot Reload): http://localhost:3000"
echo "   • Backend (Django): http://localhost:8000"
echo "   • Aplicación principal (Nginx): http://localhost:8080"
echo "   • Admin de Django: http://localhost:8080/admin"
echo "   • API Swagger: http://localhost:8000/api/schema/swagger-ui/"
echo ""
echo "📋 Comandos útiles:"
echo "   • Ver logs: docker compose logs -f"
echo "   • Ver logs específicos: docker compose logs -f backend"
echo "   • Detener servicios: docker compose down"
echo "   • Reiniciar: docker compose restart"
echo "   • Ver estado: docker compose ps"
echo ""
echo "🔄 Hot reload activado:"
echo "   • Frontend: Cambios automáticos en http://localhost:3000 (Vite)"
echo "   • Backend: Requiere reiniciar contenedor"
echo "   • Nginx: Sirve el frontend desde http://localhost:8080"
echo ""

# Esperar un momento para que los servicios se inicien
echo "⏳ Esperando que los servicios se inicien..."
sleep 20

# Verificar el estado de los servicios
echo "🔍 Verificando estado de los servicios..."
docker compose ps

echo ""
echo "🎉 ¡Modo desarrollo activado!"
echo "💡 Para volver a producción: ./build-and-run.sh"
echo ""
echo "📝 Notas importantes:"
echo "   • El frontend se ejecuta en http://localhost:3000 con hot reload (Vite)"
echo "   • Nginx sirve como proxy y sirve el frontend en http://localhost:8080"
echo "   • Los cambios en el backend requieren reiniciar el contenedor"
echo "   • La base de datos PostgreSQL está disponible en puerto 5433"
echo "   • Para desarrollo real: usa http://localhost:3000 (no 8080)"
