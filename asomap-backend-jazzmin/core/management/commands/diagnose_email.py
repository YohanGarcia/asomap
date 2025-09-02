from django.core.management.base import BaseCommand
from core.models import EmailConfiguration
from core.email_utils import get_active_email_config


class Command(BaseCommand):
    help = 'Diagnostica problemas de configuración de email'

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.SUCCESS('🔍 Diagnóstico de configuración de email...')
        )
        
        # Verificar configuración activa
        config = get_active_email_config()
        
        if not config:
            self.stdout.write(
                self.style.ERROR('❌ No hay configuración de email activa')
            )
            return
        
        self.stdout.write(f'\n📋 Configuración encontrada:')
        self.stdout.write(f'   Nombre: {config.name}')
        self.stdout.write(f'   Proveedor: {config.provider}')
        self.stdout.write(f'   Servidor: {config.host}')
        self.stdout.write(f'   Puerto: {config.port}')
        self.stdout.write(f'   TLS: {"✅" if config.use_tls else "❌"}')
        self.stdout.write(f'   Usuario: {config.username}')
        self.stdout.write(f'   Email remitente: {config.from_email}')
        self.stdout.write(f'   Activo: {"✅" if config.is_active else "❌"}')
        self.stdout.write(f'   Por defecto: {"✅" if config.is_default else "❌"}')
        
        # Verificar configuración completa
        if config.is_configured:
            self.stdout.write(
                self.style.SUCCESS('\n✅ Configuración completa')
            )
        else:
            self.stdout.write(
                self.style.ERROR('\n❌ Configuración incompleta')
            )
            missing_fields = []
            if not config.host:
                missing_fields.append('Servidor SMTP')
            if not config.port:
                missing_fields.append('Puerto')
            if not config.username:
                missing_fields.append('Usuario')
            if not config.password:
                missing_fields.append('Contraseña')
            if not config.from_email:
                missing_fields.append('Email remitente')
            
            self.stdout.write(f'   Campos faltantes: {", ".join(missing_fields)}')
        
        # Verificaciones específicas por proveedor
        if config.provider == 'gmail':
            self.stdout.write(f'\n📧 Verificaciones específicas para Gmail:')
            
            # Verificar formato de contraseña
            if config.password and len(config.password.replace(' ', '')) == 16:
                self.stdout.write('   ✅ Contraseña parece ser de aplicación (16 caracteres)')
            else:
                self.stdout.write(
                    self.style.WARNING('   ⚠️ Contraseña no parece ser de aplicación')
                )
                self.stdout.write('   💡 Para Gmail necesitas:')
                self.stdout.write('      1. Verificación en dos pasos ACTIVADA')
                self.stdout.write('      2. Contraseña de aplicación de 16 caracteres')
                self.stdout.write('      3. NO usar contraseña normal')
            
            # Verificar servidor y puerto
            if config.host == 'smtp.gmail.com':
                self.stdout.write('   ✅ Servidor SMTP correcto')
            else:
                self.stdout.write(
                    self.style.ERROR('   ❌ Servidor SMTP incorrecto')
                )
            
            if config.port == 587:
                self.stdout.write('   ✅ Puerto correcto')
            else:
                self.stdout.write(
                    self.style.ERROR('   ❌ Puerto incorrecto (debe ser 587)')
                )
            
            if config.use_tls:
                self.stdout.write('   ✅ TLS habilitado')
            else:
                self.stdout.write(
                    self.style.ERROR('   ❌ TLS debe estar habilitado')
                )
        
        elif config.provider == 'outlook':
            self.stdout.write(f'\n📧 Verificaciones específicas para Outlook:')
            
            if config.host == 'smtp.office365.com':
                self.stdout.write('   ✅ Servidor SMTP correcto')
            else:
                self.stdout.write(
                    self.style.ERROR('   ❌ Servidor SMTP incorrecto')
                )
        
        # Recomendaciones
        self.stdout.write(f'\n💡 Recomendaciones:')
        self.stdout.write('   1. Verifica que la contraseña sea correcta')
        self.stdout.write('   2. Para Gmail: usa contraseña de aplicación')
        self.stdout.write('   3. Verifica que el email remitente sea válido')
        self.stdout.write('   4. Asegúrate de que TLS esté habilitado')
        self.stdout.write('   5. Verifica tu conexión a internet')
        
        self.stdout.write(f'\n🧪 Para probar la configuración:')
        self.stdout.write('   python manage.py test_email_config')
