from django.contrib import admin
from .models import SavingTip, SliderSlide, FAQItem


@admin.register(SavingTip)
class SavingTipAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title', 'description', 'content']
    list_editable = ['order', 'is_active']
    ordering = ['order', 'id']
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('title', 'description', 'content', 'link')
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


@admin.register(SliderSlide)
class SliderSlideAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title', 'description']
    list_editable = ['order', 'is_active']
    ordering = ['order', 'id']
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('title', 'description')
        }),
        ('Imagen', {
            'fields': ('image',),
            'description': 'Imagen del slide'
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


@admin.register(FAQItem)
class FAQItemAdmin(admin.ModelAdmin):
    list_display = ['question', 'order', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['question', 'answer']
    list_editable = ['order', 'is_active']
    ordering = ['order', 'id']
    
    fieldsets = (
        ('Contenido', {
            'fields': ('question', 'answer'),
            'description': 'Pregunta y respuesta de la FAQ'
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
