# Usar Node.js 18 como base (ya incluye yarn)
FROM node:18-alpine

# Establecer directorio de trabajo
WORKDIR /app

# Copiar package.json y yarn.lock
COPY package.json yarn.lock ./

# Instalar dependencias
RUN yarn install --frozen-lockfile

# Copiar código del frontend
COPY . .

# Construir la aplicación
RUN yarn build

# Instalar serve para servir archivos estáticos
RUN yarn global add serve

# Exponer puerto
EXPOSE 3000

# Comando para servir la aplicación construida
CMD ["serve", "-s", "build", "-l", "3000"]
