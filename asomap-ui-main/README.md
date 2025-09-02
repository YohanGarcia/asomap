# Asomap.ui

## 📋 Descripción

Página de usuario final para una asociación de ahorros y préstamos. Desarrollada con React y TypeScript, utilizando Yarn como gestor de paquetes y servidor de desarrollo.

## 🚀 Características

* Interfaz amigable para el usuario final
* Gestión de contenidos e imágenes
* Integración con el backend (asomap.api)

## 🛠️ Tecnologías

* React
* TypeScript
* Yarn

## 🏗️ Arquitectura

El proyecto sigue una arquitectura modular y bien estructurada

``
src/
├── components/       # Componentes React reutilizables
├── services/         # Servicios para la interacción con la API
├── utils/            # Funciones utilitarias
├── styles/           # Archivos de estilos CSS/SCSS
├── App.tsx           # Componente principal de la aplicación
├── index.tsx         # Punto de entrada de la aplicación
└── ...
``

## 🔧 Instalación y Configuración Local

### 1. Requisitos Previos

* Node.js
* Yarn (gestor de paquetes)
* Git

### 2. Clonar el Repositorio

```bash
git clone https://github.com/coneystechnologies/asomap.ui.git
cd asomap.ui
```

### 3. Instalación de Dependencias

```bash
yarn install
```

### 4. Ejecución del Proyecto

Para iniciar el servidor de desarrollo:

```bash
yarn start
```

## 📦 Despliegue

### 1. Construcción de la Aplicación

Para construir la aplicación para producción:

```bash
yarn build
```

### 2. Despliegue en un Servidor Web

1. Copiar los archivos de la carpeta `build/` a tu servidor web.
2. Configurar tu servidor web (por ejemplo, Nginx, Apache) para servir los archivos estáticos de React.

## 📦 Endpoints Principales (Backend)

## ✍️ Autor

Desarrollado por `Eddy Díaz`

## 📄 Licencia

Este proyecto está bajo la licencia `coneystechnologies`.

## 🤝 Soporte

Para reportar problemas o solicitar ayuda, por favor comunicarse con `coneystechnologies`.
