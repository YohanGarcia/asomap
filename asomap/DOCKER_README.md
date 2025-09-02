# 🐳 ASOMAP con Docker - Estructura Monorepo Estándar

Este proyecto sigue las mejores prácticas de Docker para monorepos, con contenedores separados para backend, frontend y nginx.

## 📁 Estructura del proyecto (REORGANIZADA)

```
proyecto-root/
├── docker-compose.yml          # Orquestador principal (RAÍZ)
├── env.example                 # Variables de entorno de ejemplo (RAÍZ)
├── build-and-run.sh            # Script para producción (RAÍZ)
├── dev-mode.sh                 # Script para desarrollo (RAÍZ)
├── .dockerignore               # Archivos a excluir del build (RAÍZ)
├── asomap/                     # Infraestructura y scripts
│   ├── nginx/                  # Configuración de Nginx
│   │   ├── Dockerfile          # Dockerfile de Nginx
│   │   └── default.conf        # Configuración del servidor
│   ├── build-and-run.sh        # Script interno (legacy)
│   ├── dev-mode.sh             # Script interno (legacy)
│   └── DOCKER_README.md        # Este archivo
├── asomap-backend-jazzmin/     # Backend Django
│   ├── Dockerfile              # Dockerfile específico del backend
│   ├── requirements.txt        # Dependencias de Python
│   └── ...
└── asomap-ui-main/            # Frontend React + Vite
    ├── Dockerfile              # Dockerfile específico del frontend
    ├── package.json            # Dependencias de Node.js
    └── ...
```

## 🚀 Inicio rápido

### 1. Modo Producción (Recomendado para primera vez)

```bash
# Desde la raíz del proyecto
chmod +x build-and-run.sh dev-mode.sh
./build-and-run.sh
```

### 2. Modo Desarrollo (Con hot reload)

```bash
# Desde la raíz del proyecto
./dev-mode.sh
```

## 🌐 URLs disponibles

### Modo Producción
- **Aplicación principal**: http://localhost:8080 (Nginx)
- **Backend API**: http://localhost:8000
- **Admin Django**: http://localhost:8080/admin
- **API Swagger**: http://localhost:8000/api/schema/swagger-ui/
- **Health Check**: http://localhost:8000/health/

### Modo Desarrollo
- **Frontend (Vite)**: http://localhost:3000
- **Backend (Django)**: http://localhost:8000
- **Aplicación principal**: http://localhost:8080 (Nginx)
- **Admin Django**: http://localhost:8080/admin
- **API Swagger**: http://localhost:8000/api/schema/swagger-ui/

## 🐳 Servicios Docker

### 1. **db** (PostgreSQL)
- **Puerto**: 5433 (externo) / 5432 (interno)
- **Base de datos**: asomap
- **Usuario**: asomap_user
- **Contraseña**: asomap_password

### 2. **backend** (Django)
- **Puerto**: 8000
- **Framework**: Django 4.2.7
- **Base de datos**: PostgreSQL
- **Health check**: /health/

### 3. **frontend-dev** (React + Vite)
- **Puerto**: 3000
- **Framework**: React 18 + Vite
- **Hot reload**: ✅ Activado
- **Profile**: dev

### 4. **nginx** (Servidor web)
- **Puerto**: 8080 (externo) / 80 (interno)
- **Función**: Proxy reverso + servidor de archivos estáticos
- **Profile**: dev

### 5. **nginx-prod** (Producción)
- **Puerto**: 8080 (externo) / 80 (interno)
- **Función**: Solo proxy reverso
- **Profile**: prod

## 🔧 Comandos útiles

### Producción
```bash
# Construir e iniciar en modo producción
./build-and-run.sh

# Ver logs
docker compose logs -f

# Ver logs específicos
docker compose logs -f backend
docker compose logs -f nginx-prod

# Detener servicios
docker compose down
```

### Desarrollo
```bash
# Iniciar modo desarrollo
./dev-mode.sh

# Ver logs
docker compose logs -f

# Ver logs específicos
docker compose logs -f frontend-dev
docker compose logs -f backend

# Detener servicios
docker compose down
```

### Gestión general
```bash
# Ver estado de los servicios
docker compose ps

# Reiniciar un servicio específico
docker compose restart backend

# Reconstruir una imagen específica
docker compose build backend

# Ver logs en tiempo real
docker compose logs -f --tail=100
```

## 🔄 Perfiles de Docker Compose

### Profile: `prod`
- **Servicios**: db, backend, nginx-prod
- **Uso**: Producción sin frontend de desarrollo

### Profile: `dev`
- **Servicios**: db, backend, frontend-dev, nginx
- **Uso**: Desarrollo con hot reload

## 🗄️ Base de datos

### Cambiar a PostgreSQL

El proyecto ya está configurado para usar PostgreSQL. Si quieres cambiar la configuración, modifica `asomap-backend-jazzmin/config/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME', 'asomap'),
        'USER': os.environ.get('DB_USER', 'asomap_user'),
        'PASSWORD': os.environ.get('DB_PASS', 'asomap_password'),
        'HOST': os.environ.get('DB_HOST', 'db'),
        'PORT': os.environ.get('DB_PORT', '5432'),
    }
}
```

## 🔄 Hot Reload

### Frontend (React + Vite)
- ✅ **Modo desarrollo**: Cambios automáticos en http://localhost:3000
- ✅ **Modo producción**: Nginx sirve archivos estáticos

### Backend (Django)
- ❌ **Modo desarrollo**: Requiere reiniciar contenedor
- ❌ **Modo producción**: Requiere reconstruir imagen

## 📝 Variables de entorno

Copia `env.example` a `.env` y modifica según necesites:

```bash
# Base de datos
DB_USER=asomap_user
DB_PASS=asomap_password
DB_NAME=asomap

# Django
DEBUG=False
SECRET_KEY=tu-clave-secreta-aqui
ALLOWED_HOSTS=localhost,127.0.0.1,0.0.0.0

# Frontend
VITE_API_URL=http://localhost:8000
```

## 🐛 Solución de problemas

### Error: Puerto ya en uso
```bash
# Ver qué está usando el puerto
sudo lsof -i :8080
sudo lsof -i :8000
sudo lsof -i :3000

# Detener servicios Docker
docker compose down
```

### Error: Frontend no se construye
```bash
# Verificar dependencias
cd asomap-ui-main
yarn install
yarn build
cd ..
```

### Error: Backend no conecta a la base de datos
```bash
# Verificar que PostgreSQL esté ejecutándose
docker compose ps db

# Ver logs de PostgreSQL
docker compose logs db

# Verificar variables de entorno
docker compose exec backend env | grep DB
```

### Error: Nginx no sirve el frontend
```bash
# Verificar que el frontend esté construido
ls -la asomap-ui-main/build/

# Ver logs de Nginx
docker compose logs nginx
```

## 🚀 Despliegue en producción

Para producción, considera:

1. **Cambiar SECRET_KEY** por una clave segura
2. **Configurar ALLOWED_HOSTS** con tu dominio
3. **Usar variables de entorno** para configuraciones sensibles
4. **Configurar HTTPS** con certificados SSL
5. **Usar Gunicorn** en lugar del servidor de desarrollo de Django
6. **Configurar backups** de la base de datos

## 📚 Recursos adicionales

- [Docker Documentation](https://docs.docker.com/)
- [Docker Compose Documentation](https://docs.docker.com/compose/)
- [Django Deployment](https://docs.djangoproject.com/en/stable/howto/deployment/)
- [Vite Build](https://vitejs.dev/guide/build.html)
- [Nginx Configuration](https://nginx.org/en/docs/)

## 🤝 Contribuir

Si encuentras problemas o quieres mejorar la configuración:

1. Revisa los logs: `docker compose logs -f`
2. Verifica el estado: `docker compose ps`
3. Revisa la configuración de Docker
4. Crea un issue o pull request

---

**¡Disfruta desarrollando con ASOMAP usando la estructura estándar de Docker! 🎉**
