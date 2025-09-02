# 📧 Configuración de Proveedores de Email - ASOMAP

Este documento contiene las instrucciones completas para configurar diferentes proveedores de email en el sistema ASOMAP.

## 🎯 Configuración desde el Panel de Administración

### Ubicación en el Panel:
**Admin → Core → Configuraciones de Email → "Agregar Configuración de Email"**

---

## 📧 Gmail

### ⚙️ Configuración del Panel:
```
Nombre: Gmail ASOMAP
Proveedor: Gmail
Servidor SMTP: smtp.gmail.com
Puerto: 587
Usar TLS: ✅ (marcar)
Usuario: asomap@gmail.com
Contraseña: [contraseña de aplicación de 16 caracteres]
Email remitente: noreply@asomap.com
Activo: ✅ (marcar)
Configuración por defecto: ✅ (marcar)
```

### 🔐 Pasos de Preparación en Gmail:

#### Paso 1: Habilitar Verificación en Dos Pasos
1. Ve a tu cuenta de Google: https://myaccount.google.com/
2. Navega a **Seguridad** → **Verificación en dos pasos**
3. Activa la verificación en dos pasos
4. Sigue las instrucciones para completar la configuración

#### Paso 2: Generar Contraseña de Aplicación
1. Ve a **Seguridad** → **Contraseñas de aplicación**
2. Selecciona **"Otra"** en el menú desplegable
3. Escribe **"ASOMAP Backend"** como nombre
4. Haz clic en **"Generar"**
5. **Copia la contraseña de 16 caracteres** (ej: `abcd efgh ijkl mnop`)
6. **⚠️ IMPORTANTE:** Esta contraseña solo se muestra una vez

### 📊 Limitaciones:
- Máximo 500 emails por día
- Para mayor volumen, considera Gmail Workspace

---

## 📧 Outlook/Office 365

### ⚙️ Configuración del Panel:
```
Nombre: Outlook ASOMAP
Proveedor: Outlook/Office 365
Servidor SMTP: smtp.office365.com
Puerto: 587
Usar TLS: ✅ (marcar)
Usuario: asomap@outlook.com
Contraseña: [tu contraseña normal o contraseña de aplicación]
Email remitente: noreply@asomap.com
Activo: ✅ (marcar)
Configuración por defecto: ✅ (marcar)
```

### 🔐 Pasos de Preparación en Outlook:

#### Opción 1: Contraseña Normal
1. Usa tu contraseña normal de Outlook
2. Si tienes 2FA activado, necesitarás una contraseña de aplicación

#### Opción 2: Contraseña de Aplicación (si tienes 2FA)
1. Ve a **Configuración** → **Seguridad**
2. **Verificación en dos pasos** → **Contraseñas de aplicación**
3. Genera una nueva contraseña para "ASOMAP Backend"

### 📊 Limitaciones:
- Máximo 300 emails por día (cuenta gratuita)
- Office 365 Business: hasta 10,000 emails por día

---

## 📧 Yahoo

### ⚙️ Configuración del Panel:
```
Nombre: Yahoo ASOMAP
Proveedor: Yahoo
Servidor SMTP: smtp.mail.yahoo.com
Puerto: 587
Usar TLS: ✅ (marcar)
Usuario: asomap@yahoo.com
Contraseña: [contraseña de aplicación]
Email remitente: noreply@asomap.com
Activo: ✅ (marcar)
Configuración por defecto: ✅ (marcar)
```

### 🔐 Pasos de Preparación en Yahoo:

#### Paso 1: Habilitar Verificación en Dos Pasos
1. Ve a **Configuración de cuenta** → **Seguridad de la cuenta**
2. Activa **"Verificación en dos pasos"**

#### Paso 2: Generar Contraseña de Aplicación
1. Ve a **Seguridad de la cuenta** → **Contraseñas de aplicación**
2. Selecciona **"Otra aplicación"**
3. Escribe **"ASOMAP Backend"**
4. Genera y copia la contraseña

### 📊 Limitaciones:
- Máximo 500 emails por día

---

## 📧 Hotmail

### ⚙️ Configuración del Panel:
```
Nombre: Hotmail ASOMAP
Proveedor: Servidor Personalizado
Servidor SMTP: smtp-mail.outlook.com
Puerto: 587
Usar TLS: ✅ (marcar)
Usuario: asomap@hotmail.com
Contraseña: [tu contraseña normal]
Email remitente: noreply@asomap.com
Activo: ✅ (marcar)
Configuración por defecto: ✅ (marcar)
```

### 🔐 Pasos de Preparación en Hotmail:
- Usa tu contraseña normal
- Si tienes 2FA, genera una contraseña de aplicación

---

## 📧 Servidor Personalizado

### ⚙️ Configuración del Panel:
```
Nombre: [Nombre de tu servidor]
Proveedor: Servidor Personalizado
Servidor SMTP: [tu-servidor-smtp.com]
Puerto: [puerto del servidor]
Usar TLS: ✅ (recomendado)
Usuario: [tu-usuario]
Contraseña: [tu-contraseña]
Email remitente: noreply@tudominio.com
Activo: ✅ (marcar)
Configuración por defecto: ✅ (marcar)
```

### 🔐 Consideraciones:
- Verifica con tu proveedor de hosting los datos exactos
- Algunos servidores usan puerto 465 con SSL en lugar de 587 con TLS
- Asegúrate de que el servidor permita envío de emails

---

## 🧪 Probar la Configuración

### Desde el Panel de Administración:
1. Ve a **Configuraciones de Email**
2. Selecciona la configuración que quieres probar
3. Acción: **"Probar configuración de email"**
4. Verifica el resultado en los mensajes del sistema

### Desde Línea de Comandos:
```bash
# Probar configuración activa
python manage.py test_email_config

# Probar configuración específica
python manage.py test_email_config --config-id 1
```

### Resultados Esperados:
- ✅ **"Email de prueba enviado exitosamente"** = Configuración correcta
- ❌ **"Error al enviar email"** = Revisar configuración

---

## 🔧 Solución de Problemas

### Error: "Authentication failed"
- Verifica que la contraseña sea correcta
- Para Gmail/Yahoo: Asegúrate de usar contraseña de aplicación
- Verifica que 2FA esté habilitado

### Error: "Connection refused"
- Verifica el servidor SMTP y puerto
- Asegúrate de que "Usar TLS" esté marcado
- Verifica tu conexión a internet

### Error: "SMTP server not found"
- Verifica que el servidor SMTP esté escrito correctamente
- Prueba hacer ping al servidor

### Emails no llegan
- Revisa la carpeta de spam
- Verifica que el email remitente sea válido
- Asegúrate de que no haya límites de envío

---

## 📋 Checklist de Configuración

### ✅ Antes de Configurar:
- [ ] Tener cuenta de email activa
- [ ] Habilitar verificación en dos pasos (si aplica)
- [ ] Generar contraseña de aplicación (si aplica)
- [ ] Tener acceso al panel de administración

### ✅ Durante la Configuración:
- [ ] Llenar todos los campos requeridos
- [ ] Marcar "Usar TLS" para mayor seguridad
- [ ] Usar email remitente profesional
- [ ] Marcar como "Activo" y "Configuración por defecto"

### ✅ Después de Configurar:
- [ ] Probar la configuración
- [ ] Verificar que el email de prueba llegue
- [ ] Probar envío de reclamo desde el frontend
- [ ] Verificar email de confirmación

---

## 🚀 Uso Automático

Una vez configurado correctamente:

1. **Los reclamos se enviarán automáticamente** usando esta configuración
2. **No es necesario configurar variables de entorno**
3. **Puedes cambiar la configuración desde el panel** sin reiniciar el servidor
4. **Múltiples configuraciones** permiten cambiar fácilmente entre proveedores

---

## 📞 Soporte

Si tienes problemas con la configuración:

1. Revisa este documento
2. Verifica la configuración paso a paso
3. Prueba con un proveedor diferente
4. Contacta al administrador del sistema

---

**Última actualización:** Enero 2025  
**Versión:** 1.0  
**Autor:** Sistema ASOMAP
