from django.contrib import admin
from .models import News, Promotion, NewsMedia


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'fecha_publicacion', 'is_active', 'created_at']
    list_filter = ['is_active', 'category', 'created_at', 'fecha_publicacion']
    search_fields = ['title', 'description', 'author', 'category']
    readonly_fields = ['created_at', 'updated_at']
    ordering = ['-fecha_publicacion']
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('title', 'description', 'image')
        }),
        ('Metadatos', {
            'fields': ('author', 'category', 'tags')
        }),
        ('Publicación', {
            'fields': ('fecha_publicacion',)
        }),
        ('Contenido Completo', {
            'fields': ('full_content',),
            'description': 'Editor de texto enriquecido para el contenido completo de la noticia'
        }),
        ('📁 Archivos de Media', {
            'fields': (),
            'classes': ('collapse',),
            'description': '💡 Para agregar archivos de media (imágenes, videos, documentos), ve a "News > Archivos de Media" después de guardar esta noticia. El nuevo sistema permite subir archivos reales con descripciones y orden personalizado.'
        }),
        ('Media Adicional (DEPRECADO)', {
            'fields': ('media_urls',),
            'classes': ('collapse',),
            'description': '⚠️ DEPRECADO: Usa "Archivos de Media" en su lugar. URLs de imágenes/videos separadas por comas (solo para compatibilidad)'
        }),
        ('Enlaces Relacionados', {
            'fields': ('related_links',),
            'classes': ('collapse',),
            'description': 'URLs de enlaces relacionados separadas por comas'
        }),
        ('Estado', {
            'fields': ('is_active',)
        }),
        ('Fechas', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'fecha_inicio', 'fecha_fin', 'is_active', 'created_at']
    list_filter = ['is_active', 'category', 'created_at', 'fecha_inicio', 'fecha_fin']
    search_fields = ['title', 'description', 'category', 'tags', 'terms']
    readonly_fields = ['created_at', 'updated_at']
    ordering = ['-fecha_inicio']
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('title', 'description', 'image')
        }),
        ('Metadatos', {
            'fields': ('category', 'tags')
        }),
        ('Período', {
            'fields': ('fecha_inicio', 'fecha_fin')
        }),
        ('Contenido Completo', {
            'fields': ('full_content',),
            'description': 'Editor de texto enriquecido para el contenido completo de la promoción'
        }),
        ('Términos y Condiciones', {
            'fields': ('terms',),
            'description': 'Términos y condiciones separados por comas'
        }),
        ('Media Adicional', {
            'fields': ('media_urls',),
            'classes': ('collapse',),
            'description': 'URLs de imágenes/videos adicionales separadas por comas'
        }),
        ('Enlaces Relacionados', {
            'fields': ('related_links',),
            'classes': ('collapse',),
            'description': 'URLs de enlaces relacionados separadas por comas'
        }),
        ('Estado', {
            'fields': ('is_active',)
        }),
        ('Fechas', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(NewsMedia)
class NewsMediaAdmin(admin.ModelAdmin):
    list_display = ["news", "media_type", "caption", "order", "is_active", "created_at"]
    list_filter = ["media_type", "is_active", "created_at"]
    search_fields = ["news__title", "caption"]
    readonly_fields = ["created_at", "updated_at"]
    ordering = ["news", "order", "created_at"]
    
    fieldsets = (
        ("Archivo", {
            "fields": ("news", "file", "media_type", "caption")
        }),
        ("Configuración", {
            "fields": ("order", "is_active")
        }),
        ("Fechas", {
            "fields": ("created_at", "updated_at"),
            "classes": ("collapse",)
        }),
    )
