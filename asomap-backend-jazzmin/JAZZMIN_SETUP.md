# Configuración de Jazzmin para ASOMAP

## ¿Qué es Jazzmin?

Jazzmin es una biblioteca de Django que proporciona una interfaz de administración moderna y atractiva, reemplazando la interfaz por defecto de Django Admin con un diseño más elegante y funcional.

## Características implementadas

### 🎨 **Diseño Moderno con Colores ASOMAP**
- Interfaz limpia y profesional
- **Colores corporativos de ASOMAP** basados en [asomap.com.do](https://www.asomap.com.do/)
- Azul principal (#2f4495) y naranja (#ff9900) como colores base
- Iconos FontAwesome para todos los modelos
- Barra lateral colapsable

### 📱 **Responsive**
- Diseño adaptativo para móviles y tablets
- Navegación optimizada para diferentes tamaños de pantalla

### 🔧 **Configuración Personalizada ASOMAP**
- Logo y branding de ASOMAP
- **Colores corporativos oficiales**:
  - Azul principal: #2f4495
  - Azul oscuro: #1e2d5f
  - Azul claro: #4a5ba8
  - Naranja: #ff9900
  - Naranja oscuro: #c67905
  - Naranja claro: #ffb333
- Iconos específicos para cada modelo
- Orden de aplicaciones personalizado

## Archivos de configuración

### `config/jazzmin.py`
Contiene toda la configuración de Jazzmin:
- Configuración del sitio (título, logo, colores)
- **Colores personalizados de ASOMAP**
- Iconos para cada modelo
- Configuración de la barra lateral
- Configuración de formularios
- Orden de aplicaciones

### `config/settings.py`
Importa la configuración de Jazzmin:
```python
from .jazzmin import JAZZMIN_SETTINGS, JAZZMIN_UI_TWEAKS
```

### `static/admin/css/asomap-jazzmin.css`
**Archivo CSS personalizado** con los colores exactos de ASOMAP:
- Variables CSS con colores corporativos
- Estilos personalizados para navbar, sidebar, botones
- Responsive design optimizado

## Paleta de Colores ASOMAP

### 🎨 **Colores Principales**
- **Azul ASOMAP**: #2f4495 (Color principal)
- **Azul Oscuro**: #1e2d5f (Sidebar, hover)
- **Azul Claro**: #4a5ba8 (Enlaces, hover)
- **Naranja ASOMAP**: #ff9900 (Color secundario)
- **Naranja Oscuro**: #c67905 (Hover naranja)

### 🎯 **Aplicación de Colores**
- **Navbar**: Azul ASOMAP (#2f4495)
- **Sidebar**: Azul oscuro (#1e2d5f)
- **Botones principales**: Azul ASOMAP
- **Botones de éxito**: Naranja ASOMAP
- **Enlaces**: Azul ASOMAP
- **Hover**: Naranja ASOMAP
- **Tablas**: Cabeceras azules
- **Formularios**: Focus azul
- **Títulos**: Azul ASOMAP

## Iconos implementados

### Auth
- `auth.user`: 👤 Usuario
- `auth.Group`: 👥 Grupos

### About
- `about.Hero`: ⭐ Héroe
- `about.QuienesSomos`: ℹ️ Quiénes Somos
- `about.NuestraHistoria`: 📚 Historia
- `about.Mision`: 🎯 Misión
- `about.Vision`: 👁️ Visión
- `about.Valor`: ❤️ Valores
- `about.Director`: 👔 Directores
- `about.CommunitySupport`: 🤝 Apoyo Comunitario
- `about.CommunityCategory`: 🏷️ Categorías
- `about.CommunityInitiative`: 💡 Iniciativas
- `about.FinancialStatement`: 📈 Estados Financieros
- `about.Memory`: 📖 Memoria
- `about.Policy`: 📄 Políticas

### News
- `news.News`: 📰 Noticias
- `news.Promotion`: 🎁 Promociones

### Products
- `products.Account`: 🏦 Cuentas
- `products.Loan`: 💰 Préstamos
- `products.Card`: 💳 Tarjetas
- `products.Certificate`: 🏆 Certificados

### Header & Layout
- `header.Navigation`: ☰ Navegación
- `header.ExchangeRate`: 💱 Tipos de Cambio
- `layout.Footer`: 👣 Footer

## Características especiales

### 🎛️ **UI Builder**
- Acceso al constructor de UI de Jazzmin
- Personalización en tiempo real
- Cambios de tema sin reiniciar el servidor

### 📋 **Formularios Mejorados**
- Formularios con pestañas horizontales
- Formularios colapsables para usuarios y grupos
- Mejor organización de campos

### 🔍 **Búsqueda Avanzada**
- Búsqueda en usuarios y héroes
- Filtros mejorados
- Navegación rápida

### 📊 **Dashboard**
- Vista general del sistema
- Estadísticas rápidas
- Acceso directo a funciones principales

## Cómo usar

1. **Acceder al admin**: `http://localhost:8000/` (ruta principal)
2. **UI Builder**: Click en el ícono de configuración en la barra superior
3. **Cambiar tema**: Usar el selector de temas en la barra superior
4. **Personalizar**: Modificar `config/jazzmin.py` para cambios permanentes

## Personalización de Colores

### Cambiar colores principales
```python
JAZZMIN_SETTINGS = {
    "brand_colour": "info",  # Azul ASOMAP (#2f4495)
    "accent": "accent-warning",  # Acento naranja (#ff9900)
    "navbar": "navbar-info",  # Navbar azul
    "sidebar": "sidebar-dark-info",  # Sidebar azul oscuro
}
```

### Modificar CSS personalizado
Editar `static/admin/css/asomap-jazzmin.css`:
```css
:root {
    --asomap-blue: #2f4495;      /* Azul principal ASOMAP */
    --asomap-blue-dark: #1e2d5f; /* Azul oscuro */
    --asomap-orange: #ff9900;    /* Naranja ASOMAP */
    --asomap-orange-dark: #c67905; /* Naranja oscuro */
}
```

### Agregar iconos
```python
JAZZMIN_SETTINGS = {
    "icons": {
        "app.Model": "fas fa-icon-name",
    }
}
```

### Cambiar orden de aplicaciones
```python
JAZZMIN_SETTINGS = {
    "order_with_respect_to": [
        "auth",
        "about",
        "news",
        # ... más apps
    ],
}
```

## Temas disponibles

- `cosmo` (por defecto - complementa los azules de ASOMAP)
- `flatly`
- `journal`
- `litera`
- `lumen`
- `minty`
- `pulse`
- `sandstone`
- `simplex`
- `sketchy`
- `spacelab`
- `united`
- `yeti`

## Comandos útiles

```bash
# Verificar configuración
python manage.py check

# Ejecutar servidor
python manage.py runserver

# Crear superusuario
python manage.py createsuperuser

# Recolectar archivos estáticos (para CSS personalizado)
python manage.py collectstatic
```

## Rutas importantes

- **Panel de administración**: `http://localhost:8000/` (ruta principal)
- **Healthcheck**: `http://localhost:8000/health/`
- **API**: `http://localhost:8000/api/`
- **Documentación API**: `http://localhost:8000/api/schema/swagger-ui/`

## Notas importantes

- Jazzmin requiere Bootstrap 4
- Los iconos usan FontAwesome 5
- La configuración se carga automáticamente al iniciar Django
- Los cambios en `jazzmin.py` requieren reiniciar el servidor
- El UI Builder permite cambios temporales sin reiniciar
- **Los colores están basados en la identidad visual oficial de ASOMAP**
- El archivo CSS personalizado asegura consistencia con la marca
- **Color principal**: #2f4495 (Azul ASOMAP)
- **Color secundario**: #ff9900 (Naranja ASOMAP)
- **El admin está en la ruta principal** (`/`) en lugar de `/admin/`
