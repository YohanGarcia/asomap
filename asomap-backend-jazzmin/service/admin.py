from django.contrib import admin
from .models import ServicesPage, ServiceInfo


@admin.register(ServicesPage)
class ServicesPageAdmin(admin.ModelAdmin):
    """Admin para páginas de servicios"""
    
    list_display = [
        'title', 'subtitle', 'is_active', 'created_at'
    ]
    
    list_filter = [
        'is_active', 'created_at'
    ]
    
    search_fields = [
        'title', 'subtitle'
    ]
    
    readonly_fields = [
        'created_at', 'updated_at'
    ]
    
    fieldsets = (
        ('Información Principal', {
            'fields': ('title', 'subtitle')
        }),
        ('Configuración de Búsqueda', {
            'fields': ('search_placeholder', 'no_results_text')
        }),

        ('Banca en Línea', {
            'fields': ('internet_banking_url', 'internet_banking_button')
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
        from .models import ServicesPage
        if ServicesPage.objects.filter(is_active=True).exists():
            return False
        return super().has_add_permission(request)


@admin.register(ServiceInfo)
class ServiceInfoAdmin(admin.ModelAdmin):
    """Admin para información de servicios"""
    
    list_display = [
        'title', 'services_page', 'order', 'is_active'
    ]
    
    list_filter = [
        'services_page', 'is_active', 'created_at'
    ]
    
    search_fields = [
        'title', 'description'
    ]
    
    list_editable = [
        'order', 'is_active'
    ]
    
    readonly_fields = [
        'created_at', 'updated_at'
    ]
    
    fieldsets = (
        ('Información del Servicio', {
            'fields': ('services_page', 'title', 'description')
        }),
        ('Pasos del Servicio', {
            'fields': ('steps',),
            'description': 'Editor de texto rico para agregar pasos. Puedes usar listas con viñetas o numeradas.'
        }),
        ('Multimedia', {
            'fields': ('image', 'image_alt', 'pdf_file', 'pdf_url')
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
    
    ordering = ['services_page', 'order', 'title']
