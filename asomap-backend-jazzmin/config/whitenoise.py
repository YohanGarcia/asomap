"""
Configuración específica para WhiteNoise
"""
from whitenoise import WhiteNoise

class CustomWhiteNoise(WhiteNoise):
    """
    Configuración personalizada de WhiteNoise para ASOMAP
    """
    def __init__(self, application, **kwargs):
        super().__init__(application, **kwargs)
        
        # Configuración específica para archivos estáticos
        self.add_files('staticfiles/', prefix='static/')
        
        # Configuración de cache
        self.max_age = 31536000  # 1 año
        self.autorefresh = True
        
        # Configuración de compresión
        self.compress = True
        self.compress_level = 6
        
        # Configuración de logs
        self.log_function = self._log_function
    
    def _log_function(self, message):
        """
        Función de logging personalizada
        """
        import logging
        logger = logging.getLogger('whitenoise')
        logger.info(message)
