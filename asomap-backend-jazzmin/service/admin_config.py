"""
Configuración del orden de modelos en el admin de service
"""
from django.contrib import admin
from django.apps import apps


def setup_admin_ordering():
    """
    Configura el orden de los modelos en el admin después de que todos estén registrados
    """
    try:
        # Obtener todos los modelos de la app
        app_models = apps.get_app_config('service').get_models()
        
        # Definir el orden deseado con números con ceros a la izquierda
        model_order = [
            ('ServicesPage', "01. 📄 Páginas de Servicios"),
            ('ServiceInfo', "02. ℹ️ Información de Servicios"),
        ]
        
        # Aplicar el orden
        for model_name, display_name in model_order:
            try:
                model = apps.get_model('service', model_name)
                if model in admin.site._registry:
                    admin.site._registry[model].model._meta.verbose_name_plural = display_name
            except Exception:
                continue
                
    except Exception as e:
        print(f"Error configurando orden del admin: {e}")


# Ejecutar la configuración
setup_admin_ordering()
