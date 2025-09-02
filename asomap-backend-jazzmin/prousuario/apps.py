from django.apps import AppConfig


class ProusuarioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'prousuario'
    
    def ready(self):
        """Se ejecuta cuando la app está lista"""
        try:
            # Importar la configuración del admin después de que todos los modelos estén registrados
            from . import admin_config
        except ImportError:
            pass