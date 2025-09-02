# 🚀 Despliegue en Railway

## 📋 Requisitos Previos

1. **Cuenta en Railway**: [railway.app](https://railway.app)
2. **Repositorio en GitHub**: Código subido a GitHub
3. **Servicio PostgreSQL**: Crear en Railway
4. (Opcional) Variables para admin: `CREATE_SUPERUSER=true` y credenciales

## 🔧 Configuración en Railway

### 1. Crear Proyecto

1. Ve a [Railway Dashboard](https://railway.app/dashboard)
2. Haz clic en "New Project"
3. Selecciona "Deploy from GitHub repo"
4. Conecta tu repositorio de GitHub
5. Selecciona el repositorio `asomap-backend`

### 2. Crear Base de Datos

1. En tu proyecto Railway, haz clic en "New"
2. Selecciona "Database" → "PostgreSQL"
3. Railway creará automáticamente la variable `DATABASE_URL`

### 3. Configurar Variables de Entorno

En tu proyecto Railway, ve a "Variables" y agrega (puedes usar `railway.env.example` como guía):

```bash
# OBLIGATORIAS
SECRET_KEY=tu-clave-secreta
DEBUG=False

# Seguridad detrás de proxy (evita bucles de redirección)
SECURE_PROXY_SSL_HEADER=HTTP_X_FORWARDED_PROTO,https

# CSRF (requerido si usas cookies/sesión en HTTPS)
CSRF_TRUSTED_ORIGINS=https://web-production-xxxx.up.railway.app,https://asomap-frontend.vercel.app

# OPCIONALES
CORS_ALLOWED_ORIGINS=https://asomap-frontend.vercel.app,https://asomap.vercel.app
FRONTEND_URL=https://asomap-frontend.vercel.app

# (Opcional) Crear superusuario en deploy
CREATE_SUPERUSER=false
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_EMAIL=admin@asomap.com
DJANGO_SUPERUSER_PASSWORD=defíneme
```

### 4. Configurar Dominio

1. Ve a "Settings" → "Domains"
2. Railway asignará un dominio automáticamente
3. Opcional: Configura un dominio personalizado

## 🔄 Proceso de Despliegue

### Automático (Recomendado)

1. **Railway detecta** cambios en GitHub automáticamente
2. **Ejecuta** el script `railway-init.sh`
3. **Aplica** migraciones y recolecta archivos estáticos
4. (Opcional) Crea superusuario si `CREATE_SUPERUSER=true`
5. **Inicia** Gunicorn con la aplicación

### Manual (Si hay problemas)

Si el despliegue automático falla, ejecuta en Railway Console:

```bash
# Verificar variables
echo $SECRET_KEY
echo $DATABASE_URL

# Ejecutar migraciones
python manage.py migrate --noinput

# Recolectar estáticos
python manage.py collectstatic --noinput

# Crear superusuario
python manage.py createsuperuser

# Verificar aplicación
python manage.py check --deploy
```

## ✅ Verificación

### 1. Healthcheck
```bash
# Endpoint principal
curl https://web-production-c493c.up.railway.app/
# Debe devolver: {"status": "healthy", "message": "ASOMAP Backend is running", ...}

# Endpoint específico de healthcheck
curl https://web-production-c493c.up.railway.app/health/
# Debe devolver: {"status": "healthy", "message": "ASOMAP Backend is running", ...}
```

### 2. Admin Panel
```bash
# Visita: https://web-production-c493c.up.railway.app/admin/
# Usa el superusuario que creaste manualmente o por variables
```

### 3. API Endpoints
```bash
# Swagger UI: https://web-production-c493c.up.railway.app/api/schema/swagger-ui/
# API Base: https://web-production-c493c.up.railway.app/api/
```

## 🐛 Solución de Problemas

### Error: "Service Unavailable"
- ✅ Verificar `SECRET_KEY` está configurada
- ✅ Verificar `DATABASE_URL` está configurada
- ✅ Verificar `DEBUG=False`

### Error: "Database connection failed"
- ✅ Verificar servicio PostgreSQL está activo
- ✅ Verificar `DATABASE_URL` es correcta
- ✅ Ejecutar migraciones manualmente

### Error: "Static files not found"
- ✅ Ejecutar `python manage.py collectstatic --noinput`
- ✅ Verificar `STATIC_ROOT` está configurado

### Error: "ALLOWED_HOSTS"
- ✅ Verificar `DEBUG=False` en variables
- ✅ En producción puedes definir `ALLOWED_HOSTS` por variables (o dejar `*` temporalmente)
- ✅ Incluir `healthcheck.railway.app` y tu dominio de Railway

### Error: "Healthcheck failed"
- ✅ Verificar endpoint `/health/` responde con 200
- ✅ Verificar variable `PORT` está configurada
- ✅ Verificar `healthcheck.railway.app` en ALLOWED_HOSTS
- ✅ Verificar timeout de healthcheck (300s por defecto)
- ✅ Verificar `SECURE_PROXY_SSL_HEADER` correctamente definido

## 📊 Monitoreo

### Logs en Railway
1. Ve a tu proyecto en Railway
2. Haz clic en el servicio
3. Ve a la pestaña "Logs"
4. Monitorea errores y warnings

### Métricas
- **Uptime**: Railway Dashboard
- **Performance**: Logs de Gunicorn
- **Database**: PostgreSQL Dashboard

## 🔒 Seguridad

### Variables Sensibles
- ✅ `SECRET_KEY`: Cambiar en producción
- ✅ `DATABASE_URL`: Railway la maneja automáticamente
- ✅ `DEBUG=False`: Siempre en producción

### HTTPS
- ✅ Railway proporciona HTTPS automáticamente
- ✅ Certificados SSL renovados automáticamente

## 📞 Soporte

Si tienes problemas:

1. **Revisar logs** en Railway Dashboard
2. **Verificar variables** de entorno
3. **Ejecutar comandos** manualmente en Railway Console
4. **Contactar soporte** de Railway si es necesario

---

**¡Tu aplicación ASOMAP Backend debería estar funcionando en Railway!** 🎉
