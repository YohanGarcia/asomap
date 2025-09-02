#!/bin/bash

echo "🔨 Construyendo frontend con Docker..."

# Verificar si Docker está ejecutándose
if ! docker info > /dev/null 2>&1; then
    echo "❌ Docker no está ejecutándose. Por favor, inicia Docker primero."
    exit 1
fi

# Crear directorio build si no existe
mkdir -p asomap-ui-main/build

# Construir el frontend usando Docker
echo "🐳 Construyendo frontend con Node.js 18..."
docker run --rm -v "$(pwd)/asomap-ui-main:/app" -w /app node:18-alpine sh -c "
    yarn install --frozen-lockfile &&
    yarn build
"

if [ $? -eq 0 ]; then
    echo "✅ Frontend construido exitosamente!"
    echo "📁 Archivos generados en: asomap-ui-main/build/"
else
    echo "❌ Error al construir el frontend"
    exit 1
fi
