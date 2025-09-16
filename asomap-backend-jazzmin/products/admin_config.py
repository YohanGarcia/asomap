"""
Configuración del orden de modelos en el admin de products
"""
from django.contrib import admin
from django.apps import apps


def setup_admin_ordering():
    """
    Configura el orden de los modelos en el admin después de que todos estén registrados
    """
    try:
        # Obtener todos los modelos de la app
        app_models = apps.get_app_config('products').get_models()
        
        # Definir el orden deseado con números con ceros a la izquierda
        model_order = [
            ('Account', "01. 🏦 Accounts"),
            ('AccountBenefit', "02. 💰 Beneficios de Cuenta"),
            ('LoanType', "03. 🏷️ Tipos de Préstamos"),
            ('Loan', "04. 🏠 Préstamos"),
            ('Card', "05. 💳 Cards"),
            ('CardBenefit', "06. 🎁 Beneficios de Tarjeta"),
            ('Certificate', "07. 📜 Certificates"),
            ('CertificateBenefit', "08. 💎 Beneficios de Certificado"),
            ('CertificateRate', "09. 📊 Tarifas de Certificado"),
            ('CertificateDepositRate', "10. 💰 Tasas de Depósito de Certificado"),
            ('CertificateFAQ', "11. ❓ FAQs de Certificado"),
            ('Banner', "12. 🎨 Banners"),
        ]
        
        # Aplicar el orden
        for model_name, display_name in model_order:
            try:
                model = apps.get_model('products', model_name)
                if model in admin.site._registry:
                    admin.site._registry[model].model._meta.verbose_name_plural = display_name
            except Exception:
                continue
                
    except Exception as e:
        print(f"Error configurando orden del admin: {e}")


# Ejecutar la configuración
setup_admin_ordering()
