# Configuración de Gunicorn para manejar archivos grandes
import multiprocessing

# Configuración básica
bind = "0.0.0.0:8000"
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "sync"

# Timeouts para archivos grandes
timeout = 600  # 10 minutos para archivos muy grandes
keepalive = 2
max_requests = 1000
max_requests_jitter = 50

# Configuración para archivos grandes
max_requests_jitter = 50
graceful_timeout = 600  # 10 minutos

# Configuración de logs
accesslog = "-"
errorlog = "-"
loglevel = "info"

# Configuración de worker
worker_connections = 1000
worker_tmp_dir = "/dev/shm"  # Usar memoria compartida para archivos temporales

# Configuración de preload
preload_app = True

# Configuración de seguridad
limit_request_line = 4094
limit_request_fields = 100
limit_request_field_size = 8190

# Configuración para archivos grandes
max_requests_jitter = 50
graceful_timeout = 300
