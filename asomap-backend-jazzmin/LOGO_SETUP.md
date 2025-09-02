# Configuración del Logo ASOMAP

## 📋 **Instrucciones para el Logo**

### **Ubicación del archivo:**
El logo debe estar ubicado en: `static/admin/images/logo.png`

### **Especificaciones del logo:**
- **Formato**: PNG (recomendado) o JPG
- **Tamaño recomendado**: 300x80 píxeles (para ocupar todo el ancho)
- **Fondo**: Transparente o blanco
- **Resolución**: Mínimo 72 DPI

### **Descripción del logo ASOMAP:**
El logo de ASOMAP incluye:
- **Icono gráfico**: Formas geométricas en azul (#2f4495) y naranja (#ff9900)
- **Texto**: "ASOCIACION Mocana DE AHORROS Y PRESTAMOS"
- **Colores**: Azul principal, naranja y gris oscuro

## 🎨 **Configuración actual**

### **En Jazzmin:**
```python
JAZZMIN_SETTINGS = {
    "site_header": "",  # Sin texto, solo logo
    "site_brand": "",  # Sin texto, solo logo
    "site_logo": "admin/images/logo.png",  # Logo principal
    "site_logo_classes": "img-fluid",  # Responsive
    "site_icon": "admin/images/logo.png",  # Favicon
}
```

### **En CSS:**
```css
.navbar-brand {
    width: 100% !important;
    max-width: 300px;
}

.navbar-brand img {
    max-height: 50px;
    width: 100% !important;
    object-fit: contain;
}
```

## 📱 **Responsive Design**

El logo se adapta automáticamente:
- **Desktop**: Máximo 300px de ancho, 50px de altura
- **Tablet**: Máximo 200px de ancho, 40px de altura
- **Mobile**: Máximo 150px de ancho, 35px de altura
- **Proporción**: Se mantiene automáticamente

## 🔧 **Cómo agregar el logo**

1. **Guardar el archivo** como `logo.png`
2. **Copiar** a `static/admin/images/`
3. **Reiniciar** el servidor Django
4. **Verificar** que aparece en el navbar sin texto

## 🎯 **Características especiales**

- **Sin texto**: Solo aparece el logo, sin texto "ASOMAP"
- **Ancho completo**: El logo ocupa todo el ancho disponible (hasta 300px)
- **Responsive**: Se adapta a diferentes tamaños de pantalla
- **Proporción**: Mantiene la proporción original del logo

## 🎯 **Ubicaciones donde aparece el logo**

- **Navbar superior** (principal, sin texto)
- **Favicon** del navegador
- **Página de login** (si está configurado)
- **Página de error** (si está configurado)

## 📝 **Notas importantes**

- El logo debe tener fondo transparente para mejor integración
- Se recomienda usar PNG para mantener transparencia
- El tamaño recomendado es 300x80 píxeles para ocupar todo el ancho
- El logo se escala automáticamente para diferentes dispositivos
- **No aparece texto "ASOMAP"** al lado del logo
- El logo ocupa todo el ancho disponible en el navbar
