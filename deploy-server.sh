#!/bin/bash

# 🚀 Script de Despliegue ASOMAP para Servidor con IP Directa
# Este script configura automáticamente el proyecto para funcionar en un servidor con IP directa

set -e  # Salir si hay algún error

# Colores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Función para imprimir mensajes
print_message() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

print_header() {
    echo -e "${BLUE}================================${NC}"
    echo -e "${BLUE}  DESPLIEGUE ASOMAP EN SERVIDOR${NC}"
    echo -e "${BLUE}================================${NC}"
}

# Función para obtener la IP del servidor
get_server_ip() {
    # Intentar obtener la IP externa
    EXTERNAL_IP=$(curl -s --max-time 5 https://ipinfo.io/ip 2>/dev/null || echo "")
    
    if [ -n "$EXTERNAL_IP" ]; then
        echo $EXTERNAL_IP
    else
        # Fallback: obtener IP local
        LOCAL_IP=$(hostname -I | awk '{print $1}')
        echo $LOCAL_IP
    fi
}

# Función para validar IP
validate_ip() {
    local ip=$1
    if [[ $ip =~ ^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$ ]]; then
        return 0
    else
        return 1
    fi
}

# Función para configurar variables de entorno
configure_environment() {
    local server_ip=$1
    local server_port=${2:-8080}
    local server_protocol=${3:-http}
    
    print_message "Configurando variables de entorno para IP: $server_ip"
    
    # Crear archivo .env si no existe
    if [ ! -f ".env" ]; then
        print_message "Creando archivo .env desde env.example..."
        cp env.example .env
    fi
    
    # Actualizar SERVER_IP en .env
    if grep -q "SERVER_IP=" .env; then
        sed -i "s/SERVER_IP=.*/SERVER_IP=$server_ip/" .env
    else
        echo "SERVER_IP=$server_ip" >> .env
    fi
    
    # Actualizar SERVER_PORT en .env
    if grep -q "SERVER_PORT=" .env; then
        sed -i "s/SERVER_PORT=.*/SERVER_PORT=$server_port/" .env
    else
        echo "SERVER_PORT=$server_port" >> .env
    fi
    
    # Actualizar SERVER_PROTOCOL en .env
    if grep -q "SERVER_PROTOCOL=" .env; then
        sed -i "s/SERVER_PROTOCOL=.*/SERVER_PROTOCOL=$server_protocol/" .env
    else
        echo "SERVER_PROTOCOL=$server_protocol" >> .env
    fi
    
    # Actualizar DEBUG=False para producción
    sed -i "s/DEBUG=.*/DEBUG=False/" .env
    
    # Actualizar SECRET_KEY si es necesario
    if grep -q "SECRET_KEY=your-super-secret-key-change-this-in-production" .env; then
        print_warning "¡IMPORTANTE! Cambia SECRET_KEY en el archivo .env antes de desplegar en producción"
    fi
    
    print_message "Variables de entorno configuradas en .env"
}

# Función para verificar Docker
check_docker() {
    if ! command -v docker &> /dev/null; then
        print_error "Docker no está instalado. Por favor instala Docker primero."
        exit 1
    fi
    
    if ! command -v docker compose &> /dev/null; then
        print_error "Docker Compose no está instalado. Por favor instala Docker Compose primero."
        exit 1
    fi
    
    print_message "Docker y Docker Compose están disponibles"
}

# Función para construir y ejecutar
build_and_run() {
    local server_ip=$1
    local server_port=$2
    
    print_message "Construyendo y ejecutando ASOMAP..."
    
    # Detener servicios existentes
    print_message "Deteniendo servicios existentes..."
    docker compose down --remove-orphans 2>/dev/null || true
    
    # Limpiar imágenes para forzar rebuild
    print_message "Limpiando imágenes existentes..."
    docker compose down --rmi all --volumes --remove-orphans 2>/dev/null || true
    
    # Construir sin cache
    print_message "Construyendo servicios (sin cache)..."
    docker compose build --no-cache
    
    # Ejecutar en modo producción
    print_message "Ejecutando servicios en modo producción..."
    docker compose --profile prod up -d
    
    # Esperar a que los servicios estén listos
    print_message "Esperando a que los servicios estén listos..."
    sleep 30
    
    # Verificar estado de los servicios
    print_message "Verificando estado de los servicios..."
    docker compose ps
    
    print_message "¡Despliegue completado!"
    print_message "Frontend: $server_protocol://$server_ip:$server_port"
    print_message "Backend API: $server_protocol://$server_ip:8000"
    print_message "Admin Django: $server_protocol://$server_ip:8000/admin/"
}

# Función para mostrar ayuda
show_help() {
    echo "Uso: $0 [OPCIONES]"
    echo ""
    echo "OPCIONES:"
    echo "  -i, --ip IP          IP del servidor (ej: 192.168.1.100)"
    echo "  -p, --port PORT      Puerto del servidor (default: 8080)"
    echo "  -s, --https          Usar HTTPS en lugar de HTTP"
    echo "  -a, --auto           Detectar IP automáticamente"
    echo "  -h, --help           Mostrar esta ayuda"
    echo ""
    echo "EJEMPLOS:"
    echo "  $0 -i 192.168.1.100          # Desplegar en IP específica"
    echo "  $0 -a                        # Detectar IP automáticamente"
    echo "  $0 -i 192.168.1.100 -s       # Desplegar con HTTPS"
    echo ""
}

# Función principal
main() {
    local server_ip=""
    local server_port="8080"
    local server_protocol="http"
    local auto_detect=false
    
    print_header
    
    # Parsear argumentos
    while [[ $# -gt 0 ]]; do
        case $1 in
            -i|--ip)
                server_ip="$2"
                shift 2
                ;;
            -p|--port)
                server_port="$2"
                shift 2
                ;;
            -s|--https)
                server_protocol="https"
                shift
                ;;
            -a|--auto)
                auto_detect=true
                shift
                ;;
            -h|--help)
                show_help
                exit 0
                ;;
            *)
                print_error "Opción desconocida: $1"
                show_help
                exit 1
                ;;
        esac
    done
    
    # Verificar Docker
    check_docker
    
    # Obtener IP del servidor
    if [ -z "$server_ip" ]; then
        if [ "$auto_detect" = true ]; then
            print_message "Detectando IP del servidor automáticamente..."
            server_ip=$(get_server_ip)
            if [ -z "$server_ip" ]; then
                print_error "No se pudo detectar la IP del servidor"
                exit 1
            fi
            print_message "IP detectada: $server_ip"
        else
            print_error "Debes especificar una IP con -i o usar -a para detección automática"
            show_help
            exit 1
        fi
    fi
    
    # Validar IP
    if ! validate_ip "$server_ip"; then
        print_error "IP inválida: $server_ip"
        exit 1
    fi
    
    print_message "Configurando despliegue para:"
    print_message "  IP: $server_ip"
    print_message "  Puerto: $server_port"
    print_message "  Protocolo: $server_protocol"
    
    # Configurar variables de entorno
    configure_environment "$server_ip" "$server_port" "$server_protocol"
    
    # Construir y ejecutar
    build_and_run "$server_ip" "$server_port"
    
    print_message "¡Despliegue completado exitosamente!"
    print_message "Revisa los logs si hay problemas: docker compose logs -f"
}

# Ejecutar función principal
main "$@"
