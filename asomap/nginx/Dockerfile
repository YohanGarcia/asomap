# Usar Nginx Alpine como base
FROM nginx:alpine

# Copiar configuración personalizada
COPY default.conf /etc/nginx/conf.d/default.conf

# Crear directorio para el frontend
RUN mkdir -p /usr/share/nginx/html

# Exponer puerto 80
EXPOSE 80

# Comando por defecto de Nginx
CMD ["nginx", "-g", "daemon off;"]
