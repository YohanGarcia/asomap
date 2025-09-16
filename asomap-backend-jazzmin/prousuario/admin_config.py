"""
Configuración del orden de modelos en el admin de prousuario
"""
from django.contrib import admin
from django.apps import apps


def setup_admin_ordering():
    """
    Configura el orden de los modelos en el admin después de que todos estén registrados
    """
    try:
        # Obtener todos los modelos de la app
        app_models = apps.get_app_config('prousuario').get_models()
        
        # Definir el orden deseado con números con ceros a la izquierda
        model_order = [
            ('AccountContractsSection', "01. 📋 Secciones de Contratos de Adhesión"),
            ('ContractCategory', "02. 📁 Categorías de Contratos"),
            ('Contract', "03. 📄 Contratos"),
            ('AbandonedAccountsSection', "04. 📊 Secciones de Cuentas Abandonadas"),
            ('AccountType', "05. 🏷️ Tipos de Cuenta"),
            ('YearlyDocument', "06. 📅 Documentos Anuales"),
            ('ClaimRequest', "07. 📝 Solicitudes de Reclamos"),
            ('FraudReport', "08. 🚨 Reportes de Fraude"),
            ('RightsAndDutiesPage', "09. ⚖️ Páginas de Derechos y Deberes"),
            ('RightsAndDutiesSection', "10. 📋 Secciones de Derechos y Deberes"),
            ('RightsAndDutiesImage', "11. 🖼️ Imágenes de Derechos y Deberes"),
            ('ServiceRatesPage', "12. 💰 Páginas de Tarifas de Servicios"),
            ('ServiceCategory', "13. 📂 Categorías de Servicios"),
            ('ServiceRate', "14. 💵 Tarifas de Servicios"),
            ('Province', "15. 🗺️ Provincias"),
            ('SuggestionBox', "16. 📮 Buzón de Sugerencias"),
            ('SuggestionBoxPage', "17. 📮 Páginas de Buzón de Sugerencias"),
            ('FraudReportPage', "18. 🚨 Páginas de Reportes de Fraude"),
            ('ClaimRequestPage', "19. 📝 Páginas de Solicitudes de Reclamos"),
        ]
        
        # Aplicar el orden
        for model_name, display_name in model_order:
            try:
                model = apps.get_model('prousuario', model_name)
                if model in admin.site._registry:
                    admin.site._registry[model].model._meta.verbose_name_plural = display_name
            except Exception:
                continue
                
    except Exception as e:
        print(f"Error configurando orden del admin: {e}")


# Ejecutar la configuración
setup_admin_ordering()
