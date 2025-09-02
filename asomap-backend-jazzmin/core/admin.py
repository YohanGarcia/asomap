from django.contrib import admin
from .models import EmailConfiguration, EmailLog


@admin.register(EmailConfiguration)
class EmailConfigurationAdmin(admin.ModelAdmin):
    """Admin para configuración de email"""
    
    list_display = [
        'name', 'provider', 'host', 'port', 'username', 
        'is_active', 'is_default', 'is_configured'
    ]
    
    list_filter = [
        'provider', 'is_active', 'is_default', 'use_tls', 'created_at'
    ]
    
    search_fields = ['name', 'host', 'username', 'from_email']
    
    list_editable = ['is_active', 'is_default']
    
    ordering = ['-is_default', '-is_active', 'name']
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('name', 'provider')
        }),
        ('Configuración del Servidor', {
            'fields': ('host', 'port', 'use_tls'),
            'description': 'Configuración del servidor SMTP'
        }),
        ('Credenciales', {
            'fields': ('username', 'password'),
            'description': 'Credenciales de autenticación'
        }),
        ('Configuración de Envío', {
            'fields': ('from_email',),
            'description': 'Email que aparecerá como remitente'
        }),
        ('Estado', {
            'fields': ('is_active', 'is_default'),
            'description': 'Control de activación y configuración por defecto'
        }),
        ('Información del Sistema', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ['created_at', 'updated_at', 'is_configured']
    
    def get_queryset(self, request):
        """Optimiza las consultas"""
        return super().get_queryset(request)
    
    def save_model(self, request, obj, form, change):
        """Validación adicional al guardar"""
        try:
            obj.save()
        except Exception as e:
            from django.contrib import messages
            messages.error(request, f'Error al guardar: {str(e)}')
            raise
    
    actions = ['test_configuration']
    
    def test_configuration(self, request, queryset):
        """Probar la configuración de email seleccionada"""
        from core.email_utils import test_email_configuration
        
        for config in queryset:
            success, message = test_email_configuration(config.id)
            
            if success:
                self.message_user(
                    request,
                    f'✅ Configuración "{config.name}": {message}',
                    level='SUCCESS'
                )
            else:
                self.message_user(
                    request,
                    f'❌ Configuración "{config.name}": {message}',
                    level='ERROR'
                )
    
    test_configuration.short_description = "Probar configuración de email"


@admin.register(EmailLog)
class EmailLogAdmin(admin.ModelAdmin):
    """Admin para historial de emails enviados - Solo lectura"""
    
    list_display = [
        'email_type', 'subject', 'to_email', 'status', 
        'created_at', 'is_successful', 'claim_request_link'
    ]
    
    list_filter = [
        'email_type', 'status', 'created_at', 'email_config'
    ]
    
    search_fields = [
        'subject', 'to_email', 'from_email', 'message'
    ]
    
    readonly_fields = [
        'email_type', 'subject', 'from_email', 'to_email', 'message', 
        'html_message', 'status', 'error_message', 'claim_request', 
        'fraud_report', 'email_config', 'created_at', 'sent_at', 
        'delivery_time', 'is_successful'
    ]
    
    fieldsets = (
        ('Información del Email', {
            'fields': ('email_type', 'subject', 'from_email', 'to_email')
        }),
        ('Contenido', {
            'fields': ('message', 'html_message'),
            'classes': ('collapse',)
        }),
        ('Estado y Seguimiento', {
            'fields': ('status', 'error_message', 'created_at', 'sent_at')
        }),
        ('Relaciones', {
            'fields': ('claim_request', 'fraud_report', 'email_config'),
            'classes': ('collapse',)
        }),
    )
    
    ordering = ['-created_at']
    
    def has_add_permission(self, request):
        """No permitir crear registros de email desde el admin"""
        return False
    
    def has_delete_permission(self, request, obj=None):
        """No permitir eliminar registros de email desde el admin"""
        return False
    
    def has_change_permission(self, request, obj=None):
        """No permitir editar registros de email desde el admin"""
        return False
    
    def claim_request_link(self, obj):
        """Muestra enlace al reclamo o reporte de fraude relacionado"""
        if obj.claim_request:
            return f'<a href="/admin/prousuario/claimrequest/{obj.claim_request.id}/change/">Reclamo #{obj.claim_request.id}</a>'
        elif obj.fraud_report:
            return f'<a href="/admin/prousuario/fraudreport/{obj.fraud_report.id}/change/">Fraude #{obj.fraud_report.id}</a>'
        return '-'
    claim_request_link.short_description = 'Relacionado'
    claim_request_link.allow_tags = True
    
    def delivery_time(self, obj):
        """Muestra el tiempo de entrega"""
        if obj.delivery_time:
            return f"{obj.delivery_time.total_seconds():.2f} segundos"
        return '-'
    delivery_time.short_description = 'Tiempo de Entrega'
    
    def is_successful(self, obj):
        """Muestra si el envío fue exitoso"""
        if obj.is_successful:
            return '✅'
        return '❌'
    is_successful.short_description = 'Exitoso'
    
    actions = ['resend_failed_emails', 'export_email_logs']
    
    def resend_failed_emails(self, request, queryset):
        """Reenviar emails fallidos"""
        failed_emails = queryset.filter(status='failed')
        count = 0
        
        for email_log in failed_emails:
            try:
                # Intentar reenviar
                from core.email_utils import send_email_with_db_config
                result = send_email_with_db_config(
                    subject=email_log.subject,
                    message=email_log.message,
                    recipient_list=[email_log.to_email],
                    html_message=email_log.html_message,
                    fail_silently=True
                )
                
                if result:
                    email_log.status = 'sent'
                    email_log.save()
                    count += 1
                    
            except Exception as e:
                email_log.error_message = str(e)
                email_log.save()
        
        self.message_user(
            request,
            f'✅ {count} emails reenviados exitosamente de {failed_emails.count()} fallidos'
        )
    
    resend_failed_emails.short_description = "Reenviar emails fallidos"
    
    def export_email_logs(self, request, queryset):
        """Exportar logs de email"""
        import csv
        from django.http import HttpResponse
        
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="email_logs.csv"'
        
        writer = csv.writer(response)
        writer.writerow([
            'Tipo', 'Asunto', 'Destinatario', 'Estado', 'Fecha', 'Error'
        ])
        
        for email_log in queryset:
            writer.writerow([
                email_log.get_email_type_display(),
                email_log.subject,
                email_log.to_email,
                email_log.get_status_display(),
                email_log.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                email_log.error_message or ''
            ])
        
        return response
    
    export_email_logs.short_description = "Exportar logs a CSV"


# Configurar orden personalizado para los modelos de core
def organize_core_admin_models():
    """Organiza los modelos del admin de core con numeración"""
    model_order = [
        (EmailConfiguration, "1. ⚙️ Configuraciones de Email"),
        (EmailLog, "2. 📧 Registros de Emails"),
    ]
    
    for model, name in model_order:
        try:
            if model in admin.site._registry:
                admin.site._registry[model].model._meta.verbose_name_plural = name
        except (KeyError, AttributeError):
            continue

organize_core_admin_models()
