# 🏦 ASOMAP - Asociación de Ahorros y Préstamos Moca

## 📋 Descripción

ASOMAP es una aplicación web completa para la Asociación de Ahorros y Préstamos Moca, que incluye un backend Django con Jazzmin y un frontend React con Vite. El proyecto está completamente containerizado con Docker y automatizado para desarrollo y producción.

## 🏗️ Arquitectura del Proyecto

```
asomap/
├── asomap-backend-jazzmin/     # Backend Django con Jazzmin
├── asomap-ui-main/             # Frontend React con Vite
├── asomap/                     # Configuración de infraestructura
├── docker-compose.yml          # Orquestación de servicios
├── .env                        # Variables de entorno
├── env.example                 # Ejemplo de variables de entorno
├── build-and-run.sh            # Script para producción
├── dev-mode.sh                 # Script para desarrollo
└── build-frontend.sh           # Script para construir frontend
```

## 🚀 Características Principales

### Backend Django
- **Framework**: Django con Jazzmin Admin
- **Base de datos**: PostgreSQL
- **APIs**: RESTful con Django REST Framework
- **Autenticación**: Sistema de usuarios completo
- **CORS**: Configurado para desarrollo y producción

### Frontend React
- **Framework**: React con Vite
- **Lenguaje**: TypeScript
- **Gestión de estado**: Context API
- **Routing**: React Router
- **UI**: Componentes modernos y responsivos

### Infraestructura Docker
- **Containerización**: Todos los servicios en Docker
- **Orquestación**: Docker Compose
- **Proxy reverso**: Nginx
- **Persistencia**: Volúmenes Docker para datos

## 🛠️ Tecnologías Utilizadas

- **Backend**: Python 3.11, Django 4.x, Django REST Framework
- **Frontend**: Node.js 18, React 18, TypeScript, Vite
- **Base de datos**: PostgreSQL 15
- **Web Server**: Nginx
- **Containerización**: Docker, Docker Compose
- **Admin**: Django Jazzmin

## 📦 Instalación y Configuración

### Prerrequisitos
- Docker
- Docker Compose
- Git

### 1. Clonar el repositorio
```bash
git clone https://github.com/YohanGarcia/asomap.git
cd asomap
```

### 2. Configurar variables de entorno
```bash
cp env.example .env
# Editar .env con tus configuraciones
```

### 3. Ejecutar en modo desarrollo
```bash
./dev-mode.sh
```

### 4. Ejecutar en modo producción
```bash
./build-and-run.sh
```

## 🐳 Servicios Docker

### Servicios Disponibles
- **db**: PostgreSQL 15 (puerto 5433)
- **backend**: Django Backend (puerto 8000)
- **frontend-dev**: React Development (puerto 3000)
- **nginx-prod**: Nginx Production (puerto 8080)

### Puertos
- **Frontend Dev**: http://localhost:3000
- **Frontend Prod**: http://localhost:8080
- **Backend API**: http://localhost:8000
- **Base de datos**: localhost:5433

## 📊 Aplicaciones Django

### 1. About
- **Modelos**: Hero, QuienesSomos, Mision, Vision, Valor, Director
- **Datos**: 7 secciones principales de la institución

### 2. Community
- **Modelos**: CommunityCategory, CommunityInitiative
- **Datos**: 3 categorías, 2 iniciativas comunitarias

### 3. Financial
- **Modelos**: FinancialDocument, FinancialStatement
- **Datos**: 13 documentos financieros (2022-2024)

### 4. Memory
- **Modelos**: MemoryConfig, MemoryDocument
- **Datos**: 9 memorias anuales (2014-2023)

### 5. Policy
- **Modelos**: PolicyCategory, PolicyConfig, PolicyDocument
- **Datos**: 15 documentos de políticas en 3 categorías

### 6. Financial Guidance
- **Modelos**: SavingTip, FAQItem, FinancialSlide
- **Datos**: 3 consejos, 3 slides, 6 FAQs

### 7. Home
- **Modelos**: DebitCardPromo, EducationItem, Product, SliderItem
- **Datos**: Promociones, educación, productos, slider

### 8. Locations
- **Modelos**: Service, Schedule
- **Datos**: 31 servicios bancarios, 57 horarios

### 9. News
- **Modelos**: News, Promotion
- **Datos**: 3 noticias, 3 promociones

### 10. Products
- **Modelos**: Account, Card, Certificate, Loan
- **Datos**: Cuentas, tarjetas, certificados, préstamos

### 11. Pro Usuario
- **Modelos**: Province, ServiceRatesPage, ContractCategory
- **Datos**: 32 provincias RD, tarifas, contratos, derechos

### 12. Service
- **Modelos**: ServicesPage, ServiceInfo
- **Datos**: 7 servicios bancarios completos

## 🔄 Automatización de Datos

El proyecto incluye un sistema completo de automatización de datos que se ejecuta automáticamente al iniciar Docker:

### Script start.sh
- **27 comandos de datos** ejecutándose automáticamente
- **Verificación inteligente** de datos existentes
- **Manejo de errores** robusto
- **Logs detallados** de cada operación

### Comandos Automatizados
```bash
# About
python manage.py create_about_data --force

# Community
python manage.py create_community_data --force

# Financial
python manage.py create_financial_data --force

# Memory
python manage.py create_memory_data --force

# Policy
python manage.py create_policy_data --force

# Financial Guidance
python manage.py create_financial_guidance_data --force

# Home
python manage.py create_home_data --force

# Locations
python manage.py create_services --force
python manage.py create_schedules --force

# News
python manage.py create_sample_news --force
python manage.py create_sample_promotions --force

# Products
python manage.py create_products --force
python manage.py create_sample_accounts --force
python manage.py create_sample_cards --force
python manage.py create_sample_certificates --force
python manage.py create_sample_loans --force

# Pro Usuario
python manage.py create_provinces --force
python manage.py create_sample_service_rates --force
python manage.py create_sample_contracts --force
python manage.py create_sample_rights_and_duties --force
python manage.py create_sample_fraud_reports --force
python manage.py create_sample_abandoned_accounts --force

# Service
python manage.py create_sample_services --force
```

## 🚀 Comandos Útiles

### Desarrollo
```bash
# Modo desarrollo
./dev-mode.sh

# Construir solo frontend
./build-frontend.sh

# Ver logs
docker compose logs -f [servicio]
```

### Producción
```bash
# Modo producción
./build-and-run.sh

# Reconstruir backend
docker compose build backend

# Reiniciar servicios
docker compose restart [servicio]
```

### Base de Datos
```bash
# Ejecutar migraciones
docker compose exec backend python manage.py migrate

# Crear superusuario
docker compose exec backend python manage.py createsuperuser

# Shell de Django
docker compose exec backend python manage.py shell
```

## 📁 Estructura de Archivos

```
asomap/
├── asomap-backend-jazzmin/
│   ├── config/                 # Configuración Django
│   ├── about/                  # App About
│   ├── community/              # App Community
│   ├── financial/              # App Financial
│   ├── memory/                 # App Memory
│   ├── policy/                 # App Policy
│   ├── educacionfinanciera/    # App Financial Guidance
│   ├── home/                   # App Home
│   ├── locations/              # App Locations
│   ├── news/                   # App News
│   ├── products/               # App Products
│   ├── prousuario/             # App Pro Usuario
│   ├── service/                # App Service
│   ├── core/                   # App Core
│   ├── requirements.txt        # Dependencias Python
│   ├── Dockerfile              # Docker del backend
│   └── start.sh                # Script de inicio
├── asomap-ui-main/
│   ├── src/                    # Código fuente React
│   ├── public/                 # Archivos públicos
│   ├── package.json            # Dependencias Node.js
│   ├── vite.config.ts          # Configuración Vite
│   └── Dockerfile              # Docker del frontend
├── asomap/
│   ├── nginx/                  # Configuración Nginx
│   └── scripts/                # Scripts adicionales
├── docker-compose.yml          # Orquestación Docker
├── .env                        # Variables de entorno
├── .dockerignore               # Archivos ignorados por Docker
└── README.md                   # Este archivo
```

## 🔧 Configuración de Entorno

### Variables de Entorno (.env)
```bash
# Django
DEBUG=True
SECRET_KEY=your-secret-key
ALLOWED_HOSTS=localhost,127.0.0.1

# Base de datos
DB_NAME=asomap_db
DB_USER=asomap_user
DB_PASSWORD=asomap_password
DB_HOST=db
DB_PORT=5432
USE_DOCKER_DB=True

# CORS
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://localhost:8080
```

## 📈 Características Avanzadas

### Middleware Personalizado
- **HealthCheckMiddleware**: Verificación de salud del sistema
- **PublicMediaMiddleware**: Servir archivos media públicamente

### APIs RESTful
- **Endpoints completos** para todas las apps
- **Serializers optimizados** para el frontend
- **Filtros y búsquedas** avanzadas
- **Documentación automática** con Swagger

### Sistema de Archivos
- **Volúmenes Docker** para persistencia
- **Soporte para imágenes** en múltiples formatos
- **Gestión de archivos** optimizada
- **Backup automático** de datos

## 🐛 Solución de Problemas

### Problemas Comunes

#### 1. Puerto ya en uso
```bash
# Cambiar puertos en docker-compose.yml
# o detener servicios que usen esos puertos
```

#### 2. Base de datos no conecta
```bash
# Verificar variables de entorno
# Reconstruir contenedor backend
docker compose build backend
```

#### 3. Frontend no carga
```bash
# Verificar que Nginx esté funcionando
# Revisar logs de Nginx
docker compose logs nginx-prod
```

#### 4. Datos no se crean
```bash
# Verificar que start.sh tenga permisos
# Reconstruir imagen backend
docker compose build --no-cache backend
```

## 🤝 Contribución

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 👥 Autores

- **Yohan García** - *Desarrollo inicial* - [YohanGarcia](https://github.com/YohanGarcia)

## 🙏 Agradecimientos

- **ASOMAP** por confiar en este proyecto
- **Comunidad Django** por el excelente framework
- **Comunidad React** por las herramientas de frontend
- **Docker** por la containerización

## 📞 Contacto

- **Proyecto**: [https://github.com/YohanGarcia/asomap](https://github.com/YohanGarcia/asomap)
- **Issues**: [https://github.com/YohanGarcia/asomap/issues](https://github.com/YohanGarcia/asomap/issues)

---

**¡ASOMAP - Más de 50 años sirviendo a la comunidad de Moca!** 🏦✨
