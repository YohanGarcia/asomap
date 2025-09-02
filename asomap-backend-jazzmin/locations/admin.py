from django.contrib import admin
from .models import Location, Schedule, Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['name', 'description']
    readonly_fields = ['created_at', 'updated_at']
    ordering = ['name']
    
    fieldsets = (
        ('Información del Servicio', {
            'fields': ('name', 'description')
        }),
        ('Estado', {
            'fields': ('is_active',)
        }),
        ('Fechas', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['name', 'opening_time', 'closing_time', 'is_24_7', 'is_active']
    list_filter = ['is_24_7', 'is_active', 'created_at']
    search_fields = ['name']
    readonly_fields = ['created_at', 'updated_at']
    ordering = ['name']
    
    fieldsets = (
        ('Información del Horario', {
            'fields': ('name', 'is_24_7')
        }),
        ('Horarios', {
            'fields': ('opening_time', 'closing_time')
        }),
        ('Estado', {
            'fields': ('is_active',)
        }),
        ('Fechas', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'address', 'schedule', 'services_count', 'is_open', 'is_active', 'created_at']
    list_filter = ['type', 'is_open', 'is_active', 'schedule', 'services', 'created_at']
    search_fields = ['name', 'address', 'phone']
    readonly_fields = ['created_at', 'updated_at']
    ordering = ['type', 'name']
    filter_horizontal = ['services']
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('type', 'name', 'address', 'phone')
        }),
        ('Ubicación', {
            'fields': ('latitude', 'longitude')
        }),
        ('Horarios', {
            'fields': ('schedule',)
        }),
        ('Servicios', {
            'fields': ('services',)
        }),
        ('Estado', {
            'fields': ('is_open', 'is_active')
        }),
        ('Fechas', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def services_count(self, obj):
        """Muestra el número de servicios en la lista"""
        return obj.services.count()
    services_count.short_description = 'Servicios'
