from django.contrib import admin
from .models import (
    AccountType, AbandonedAccountsSection, YearlyDocument,
    ContractCategory, AccountContractsSection, Contract, ClaimRequest, FraudReport,
    RightsAndDutiesPage, RightsAndDutiesSection, RightsAndDutiesImage,
    ServiceRatesPage, ServiceCategory, ServiceRate, Province, SuggestionBox
)

# Configurar el orden de los modelos en el admin
admin.site.site_header = "Administración ASOMAP"
admin.site.site_title = "ASOMAP Admin"
admin.site.index_title = "Panel de Administración"


@admin.register(AccountType)
class AccountTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'label', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['id', 'label', 'description']
    list_editable = ['is_active']
    ordering = ['id']
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('label', 'description')
        }),
        ('Estado', {
            'fields': ('is_active',),
            'description': 'Control de visibilidad del tipo de cuenta'
        }),
        ('Fechas', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ['id', 'created_at', 'updated_at']


@admin.register(AbandonedAccountsSection)
class AbandonedAccountsSectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'account_types_count', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title', 'description']
    list_editable = ['is_active']
    ordering = ['-created_at']
    filter_horizontal = ['account_types']
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('title', 'description')
        }),
        ('Tipos de Cuenta', {
            'fields': ('account_types',),
            'description': 'Selecciona los tipos de cuenta que estarán disponibles en esta sección'
        }),
        ('Estado', {
            'fields': ('is_active',),
            'description': 'Control de visibilidad de la sección'
        }),
        ('Fechas', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ['created_at', 'updated_at']
    
    def account_types_count(self, obj):
        """Muestra el número de tipos de cuenta asociados"""
        return obj.account_types.count()
    account_types_count.short_description = 'Tipos de Cuenta'
    
    def has_add_permission(self, request):
        # Solo permitir crear si no hay secciones activas
        if AbandonedAccountsSection.objects.filter(is_active=True).exists():
            return False
        return super().has_add_permission(request)


@admin.register(YearlyDocument)
class YearlyDocumentAdmin(admin.ModelAdmin):
    list_display = ['title', 'year', 'account_type', 'type', 'date', 'is_active', 'created_at']
    list_filter = ['year', 'account_type', 'is_active', 'created_at', 'date']
    search_fields = ['title', 'year', 'account_type__label']
    list_editable = ['is_active']
    ordering = ['-year', 'account_type']
    date_hierarchy = 'date'
    
    fieldsets = (
        ('Información del Documento', {
            'fields': ('title', 'year', 'account_type', 'type', 'date')
        }),
        ('Archivo', {
            'fields': ('document',),
            'description': 'Sube el archivo PDF del documento (solo archivos .pdf)'
        }),
        ('Estado', {
            'fields': ('is_active',),
            'description': 'Control de visibilidad del documento'
        }),
        ('Fechas', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ['created_at', 'updated_at']
    
    def get_queryset(self, request):
        """Optimiza las consultas con select_related"""
        return super().get_queryset(request).select_related('account_type')
    
    def save_model(self, request, obj, form, change):
        """Validación adicional al guardar"""
        try:
            obj.save()
        except Exception as e:
            from django.contrib import messages
            messages.error(request, f'Error al guardar: {str(e)}')
            raise


@admin.register(ContractCategory)
class ContractCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['name']
    list_editable = ['is_active']
    ordering = ['name']
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('name',)
        }),
        ('Estado', {
            'fields': ('is_active',),
            'description': 'Control de visibilidad de la categoría'
        }),
        ('Fechas', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ['created_at', 'updated_at']


@admin.register(AccountContractsSection)
class AccountContractsSectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title', 'description']
    list_editable = ['is_active']
    ordering = ['-created_at']
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('title', 'description')
        }),
        ('Estado', {
            'fields': ('is_active',),
            'description': 'Control de visibilidad de la sección'
        }),
        ('Fechas', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ['created_at', 'updated_at']
    
    def has_add_permission(self, request):
        # Solo permitir crear si no hay secciones activas
        if AccountContractsSection.objects.filter(is_active=True).exists():
            return False
        return super().has_add_permission(request)


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'order', 'is_active', 'created_at']
    list_filter = ['category', 'is_active', 'created_at']
    search_fields = ['title', 'category__name']
    list_editable = ['order', 'is_active']
    ordering = ['category', 'order', 'title']
    
    fieldsets = (
        ('Información del Contrato', {
            'fields': ('title', 'category')
        }),
        ('Archivo', {
            'fields': ('document',),
            'description': 'Sube el archivo PDF del contrato (solo archivos .pdf)'
        }),
        ('Configuración', {
            'fields': ('order', 'is_active'),
            'description': 'Configuración de orden y estado'
        }),
        ('Fechas', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ['created_at', 'updated_at']
    
    def get_queryset(self, request):
        """Optimiza las consultas con select_related"""
        return super().get_queryset(request).select_related('category')





@admin.register(ClaimRequest)
class ClaimRequestAdmin(admin.ModelAdmin):
    """Admin para solicitudes de reclamos - Solo lectura y cambio de estado"""
    
    list_display = [
        'full_name', 'email', 'product_type', 'claim_type', 
        'status', 'email_status', 'created_at'
    ]
    
    list_filter = [
        'status', 'product_type', 'claim_type', 'distribution_channel',
        'created_at'
    ]
    
    search_fields = [
        'full_name', 'email', 'document', 'phone', 'message'
    ]
    
    readonly_fields = [
        'full_name', 'document', 'phone', 'email', 'product_type',
        'claim_type', 'distribution_channel', 'message', 'created_at',
        'updated_at', 'resolved_at'
    ]
    
    fieldsets = (
        ('Información Personal', {
            'fields': ('full_name', 'document', 'phone', 'email'),
            'classes': ('collapse',)
        }),
        ('Información del Reclamo', {
            'fields': ('product_type', 'claim_type', 'distribution_channel', 'message'),
            'classes': ('collapse',)
        }),
        ('Gestión del Reclamo', {
            'fields': ('status', 'internal_notes'),
            'description': 'Aquí puedes cambiar el estado y agregar notas internas'
        }),
        ('Información del Sistema', {
            'fields': ('created_at', 'updated_at', 'resolved_at'),
            'classes': ('collapse',)
        }),
    )
    
    list_editable = ['status']
    
    ordering = ['-created_at']
    
    def has_add_permission(self, request):
        """No permitir crear nuevos reclamos desde el admin"""
        return False
    
    def has_delete_permission(self, request, obj=None):
        """No permitir eliminar reclamos"""
        return False
    
    def email_status(self, obj):
        """Muestra el estado del email"""
        from .utils import get_email_status
        status = get_email_status(obj)
        
        if status == "Enviado recientemente":
            return "📧 Enviado recientemente"
        elif status == "Enviado":
            return "✅ Enviado"
        elif status == "Sin email":
            return "❌ Sin email"
        elif status == "Error":
            return "⚠️ Error"
        else:
            return "❓ Desconocido"
    
    email_status.short_description = "Estado Email"


@admin.register(FraudReport)
class FraudReportAdmin(admin.ModelAdmin):
    """Admin para reportes de fraude - Solo lectura y cambio de estado"""
    
    list_display = [
        'full_name', 'email', 'classification', 'status', 
        'email_status', 'created_at'
    ]
    
    list_filter = [
        'status', 'classification', 'created_at'
    ]
    
    search_fields = [
        'full_name', 'email', 'document', 'phone', 'message'
    ]
    
    readonly_fields = [
        'full_name', 'document', 'phone', 'email', 'classification',
        'message', 'file_url', 'created_at', 'updated_at', 'resolved_at'
    ]
    
    fieldsets = (
        ('Información Personal', {
            'fields': ('full_name', 'document', 'phone', 'email'),
            'classes': ('collapse',)
        }),
        ('Información del Fraude', {
            'fields': ('classification', 'message', 'file_url'),
            'classes': ('collapse',)
        }),
        ('Gestión del Reporte', {
            'fields': ('status', 'internal_notes'),
            'description': 'Aquí puedes cambiar el estado y agregar notas internas'
        }),
        ('Información del Sistema', {
            'fields': ('created_at', 'updated_at', 'resolved_at'),
            'classes': ('collapse',)
        }),
    )
    
    list_editable = ['status']
    
    ordering = ['-created_at']
    
    def has_add_permission(self, request):
        """No permitir crear nuevos reportes desde el admin"""
        return False
    
    def has_delete_permission(self, request, obj=None):
        """No permitir eliminar reportes"""
        return False
    
    def email_status(self, obj):
        """Muestra el estado del email"""
        from .utils import get_email_status
        status = get_email_status(obj)
        
        if status == "Enviado recientemente":
            return "📧 Enviado recientemente"
        elif status == "Enviado":
            return "✅ Enviado"
        elif status == "Sin email":
            return "❌ Sin email"
        elif status == "Error":
            return "⚠️ Error"
        else:
            return "❓ Desconocido"
    
    email_status.short_description = "Estado Email"


@admin.register(RightsAndDutiesPage)
class RightsAndDutiesPageAdmin(admin.ModelAdmin):
    """Admin para página de derechos y deberes"""
    
    list_display = [
        'page_title', 'is_active', 'created_at'
    ]
    
    list_filter = [
        'is_active', 'created_at'
    ]
    
    search_fields = [
        'page_title', 'page_description'
    ]
    
    readonly_fields = [
        'created_at', 'updated_at'
    ]
    
    fieldsets = (
        ('Información de la Página', {
            'fields': ('page_title', 'page_description')
        }),
        ('Estado', {
            'fields': ('is_active',)
        }),
        ('Información del Sistema', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    ordering = ['-created_at']
    
    def has_add_permission(self, request):
        """Solo permitir crear si no hay páginas activas"""
        from .models import RightsAndDutiesPage
        if RightsAndDutiesPage.objects.filter(is_active=True).exists():
            return False
        return super().has_add_permission(request)


@admin.register(RightsAndDutiesSection)
class RightsAndDutiesSectionAdmin(admin.ModelAdmin):
    """Admin para secciones de derechos y deberes"""
    
    list_display = [
        'title', 'section_id', 'order', 'is_active'
    ]
    
    list_filter = [
        'section_id', 'is_active', 'created_at'
    ]
    
    search_fields = [
        'title', 'description', 'button_text'
    ]
    
    list_editable = [
        'order', 'is_active'
    ]
    
    readonly_fields = [
        'created_at', 'updated_at'
    ]
    
    fieldsets = (
        ('Información de la Sección', {
            'fields': ('section_id', 'title', 'description')
        }),
        ('Configuración', {
            'fields': ('button_text', 'additional_info', 'order')
        }),
        ('Estado', {
            'fields': ('is_active',)
        }),
        ('Información del Sistema', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    ordering = ['order', 'title']
    
    def has_add_permission(self, request):
        # Permitir crear secciones normalmente, el modelo se encarga de la lógica de activación
        return super().has_add_permission(request)


@admin.register(RightsAndDutiesImage)
class RightsAndDutiesImageAdmin(admin.ModelAdmin):
    """Admin para imágenes de derechos y deberes"""
    
    list_display = [
        'alt_text', 'section', 'order', 'is_active', 'image_preview'
    ]
    
    list_filter = [
        'section', 'is_active', 'created_at'
    ]
    
    search_fields = [
        'alt_text', 'description', 'section__title'
    ]
    
    list_editable = [
        'order', 'is_active'
    ]
    
    readonly_fields = [
        'created_at', 'updated_at', 'image_preview'
    ]
    
    fieldsets = (
        ('Información de la Imagen', {
            'fields': ('section', 'image', 'alt_text', 'description')
        }),
        ('Configuración', {
            'fields': ('order',)
        }),
        ('Estado', {
            'fields': ('is_active',)
        }),
        ('Vista Previa', {
            'fields': ('image_preview',),
            'classes': ('collapse',)
        }),
        ('Información del Sistema', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    ordering = ['section', 'order', 'alt_text']
    
    def image_preview(self, obj):
        """Muestra una vista previa de la imagen"""
        if obj.image:
            return f'<img src="{obj.image.url}" style="max-height: 50px; max-width: 100px;" />'
        return 'Sin imagen'
    image_preview.short_description = 'Vista Previa'
    image_preview.allow_tags = True


@admin.register(ServiceRatesPage)
class ServiceRatesPageAdmin(admin.ModelAdmin):
    """Admin para página de tarifas de servicios"""
    
    list_display = [
        'title', 'is_active', 'created_at'
    ]
    
    list_filter = [
        'is_active', 'created_at'
    ]
    
    search_fields = [
        'title', 'description'
    ]
    
    readonly_fields = [
        'created_at', 'updated_at'
    ]
    
    fieldsets = (
        ('Información de la Página', {
            'fields': ('title', 'description')
        }),
        ('Estado', {
            'fields': ('is_active',)
        }),
        ('Información del Sistema', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    ordering = ['-created_at']
    
    def has_add_permission(self, request):
        """Solo permitir crear si no hay páginas activas"""
        from .models import ServiceRatesPage
        if ServiceRatesPage.objects.filter(is_active=True).exists():
            return False
        return super().has_add_permission(request)


@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    """Admin para categorías de servicios"""
    
    list_display = [
        'name', 'order', 'is_active'
    ]
    
    list_filter = [
        'is_active', 'created_at'
    ]
    
    search_fields = [
        'name'
    ]
    
    list_editable = [
        'order', 'is_active'
    ]
    
    readonly_fields = [
        'created_at', 'updated_at'
    ]
    
    fieldsets = (
        ('Información de la Categoría', {
            'fields': ('name',)
        }),
        ('Configuración', {
            'fields': ('order',)
        }),
        ('Estado', {
            'fields': ('is_active',)
        }),
        ('Información del Sistema', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    ordering = ['order', 'name']


@admin.register(ServiceRate)
class ServiceRateAdmin(admin.ModelAdmin):
    """Admin para tarifas de servicios"""
    
    list_display = [
        'service', 'rate', 'category', 'order', 'is_active'
    ]
    
    list_filter = [
        'category', 'is_active', 'created_at'
    ]
    
    search_fields = [
        'service', 'description', 'rate', 'category__name'
    ]
    
    list_editable = [
        'order', 'is_active'
    ]
    
    readonly_fields = [
        'created_at', 'updated_at'
    ]
    
    fieldsets = (
        ('Información del Servicio', {
            'fields': ('category', 'service', 'description', 'rate')
        }),
        ('Detalles', {
            'fields': ('details',),
            'description': 'Agregar detalles con formato rico usando el editor'
        }),
        ('Configuración', {
            'fields': ('order',)
        }),
        ('Estado', {
            'fields': ('is_active',)
        }),
        ('Información del Sistema', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    ordering = ['category', 'order', 'service']


@admin.register(Province)
class ProvinceAdmin(admin.ModelAdmin):
    """Admin para provincias"""
    
    list_display = [
        'name', 'is_active'
    ]
    
    list_filter = [
        'is_active', 'created_at'
    ]
    
    search_fields = [
        'name'
    ]
    
    list_editable = [
        'is_active'
    ]
    
    readonly_fields = [
        'created_at', 'updated_at'
    ]
    
    fieldsets = (
        ('Información de la Provincia', {
            'fields': ('name',)
        }),
        ('Estado', {
            'fields': ('is_active',)
        }),
        ('Información del Sistema', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    ordering = ['name']


@admin.register(SuggestionBox)
class SuggestionBoxAdmin(admin.ModelAdmin):
    """Admin para el buzón de sugerencias"""
    
    list_display = [
        'full_name', 'classification', 'province', 'status', 'created_at'
    ]
    
    list_filter = [
        'status', 'province', 'classification', 'created_at'
    ]
    
    search_fields = [
        'full_name', 'email', 'document', 'phone', 'message', 'classification'
    ]
    
    readonly_fields = [
        'full_name', 'document', 'phone', 'email', 'province',
        'classification', 'message', 'created_at', 'updated_at', 'resolved_at'
    ]
    
    fieldsets = (
        ('Información Personal', {
            'fields': ('full_name', 'document', 'phone', 'email', 'province'),
            'classes': ('collapse',)
        }),
        ('Sugerencia', {
            'fields': ('classification', 'message'),
            'classes': ('collapse',)
        }),
        ('Gestión de la Sugerencia', {
            'fields': ('status', 'internal_notes'),
            'description': 'Aquí puedes cambiar el estado y agregar notas internas'
        }),
        ('Información del Sistema', {
            'fields': ('created_at', 'updated_at', 'resolved_at'),
            'classes': ('collapse',)
        }),
    )
    
    list_editable = ['status']
    ordering = ['-created_at']
    
    def has_add_permission(self, request):
        """No permitir crear nuevas sugerencias desde el admin"""
        return False
    
    def has_delete_permission(self, request, obj=None):
        """No permitir eliminar sugerencias"""
        return False


# La configuración del orden del admin se maneja en admin_config.py
# y se ejecuta automáticamente desde apps.py cuando la app está lista