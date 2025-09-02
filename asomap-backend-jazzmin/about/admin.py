from django.contrib import admin
from .models import (
    Hero, QuienesSomos, NuestraHistoria, 
    Mision, Vision, Valor, Director,
    CommunitySupport, CommunityCategory, CommunityInitiative,
    FinancialDocument, FinancialStatementsConfig, MemoryDocument, MemoryConfig,
    PolicyDocument, PolicyCategory, PolicyConfig
)

# Registrar con el admin por defecto de Django
@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'created_at', 'updated_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title', 'description']
    readonly_fields = ['created_at', 'updated_at']
    ordering = ['-created_at']

@admin.register(QuienesSomos)
class QuienesSomosAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'created_at', 'updated_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title']
    readonly_fields = ['created_at', 'updated_at']

@admin.register(NuestraHistoria)
class NuestraHistoriaAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'created_at', 'updated_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title']
    readonly_fields = ['created_at', 'updated_at']

@admin.register(Mision)
class MisionAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'created_at', 'updated_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title']
    readonly_fields = ['created_at', 'updated_at']

@admin.register(Vision)
class VisionAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'created_at', 'updated_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title']
    readonly_fields = ['created_at', 'updated_at']

@admin.register(Valor)
class ValorAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'created_at', 'updated_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title', 'description']
    readonly_fields = ['created_at', 'updated_at']

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'is_active', 'created_at', 'updated_at']
    list_filter = ['is_active', 'created_at', 'position']
    search_fields = ['name', 'position']
    readonly_fields = ['created_at', 'updated_at']

@admin.register(CommunityCategory)
class CommunityCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon', 'is_active', 'created_at', 'updated_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['name', 'description']
    readonly_fields = ['created_at', 'updated_at']
    ordering = ['id']

@admin.register(CommunityInitiative)
class CommunityInitiativeAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'is_active', 'created_at', 'updated_at']
    list_filter = ['is_active', 'created_at', 'category']
    search_fields = ['title', 'description', 'impact']
    readonly_fields = ['created_at', 'updated_at']
    ordering = ['category', 'id']

@admin.register(CommunitySupport)
class CommunitySupportAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'created_at', 'updated_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title', 'description']
    readonly_fields = ['created_at', 'updated_at']

@admin.register(FinancialDocument)
class FinancialDocumentAdmin(admin.ModelAdmin):
    list_display = ['title', 'year', 'document_type', 'quarter', 'is_active']
    list_filter = ['is_active', 'created_at', 'document_type', 'quarter', 'year']
    search_fields = ['title', 'year']
    readonly_fields = ['created_at', 'updated_at']
    ordering = ['-year', 'document_type', 'quarter']
    list_editable = ['is_active']
    fieldsets = (
        ('Información del Documento', {
            'fields': ('title', 'file', 'document_type', 'year', 'quarter')
        }),
        ('Estado', {
            'fields': ('is_active',)
        }),
        ('Fechas', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

@admin.register(FinancialStatementsConfig)
class FinancialStatementsConfigAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'created_at', 'updated_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title', 'description']
    readonly_fields = ['created_at', 'updated_at']
    ordering = ['-created_at']
    
    def has_add_permission(self, request):
        # Solo permitir crear si no hay configuraciones activas
        if FinancialStatementsConfig.objects.filter(is_active=True).exists():
            return False
        return super().has_add_permission(request)

@admin.register(MemoryDocument)
class MemoryDocumentAdmin(admin.ModelAdmin):
    list_display = ['year', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at', 'year']
    search_fields = ['year']
    readonly_fields = ['created_at', 'updated_at']
    ordering = ['-year']
    list_editable = ['is_active']
    fieldsets = (
        ('Información del Documento', {
            'fields': ('file', 'year')
        }),
        ('Estado', {
            'fields': ('is_active',)
        }),
        ('Fechas', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

@admin.register(MemoryConfig)
class MemoryConfigAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'created_at', 'updated_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title', 'description']
    readonly_fields = ['created_at', 'updated_at']
    ordering = ['-created_at']
    
    def has_add_permission(self, request):
        # Solo permitir crear si no hay configuraciones activas
        if MemoryConfig.objects.filter(is_active=True).exists():
            return False
        return super().has_add_permission(request)

@admin.register(PolicyDocument)
class PolicyDocumentAdmin(admin.ModelAdmin):
    list_display = ['title', 'last_update', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at', 'last_update']
    search_fields = ['title', 'description']
    readonly_fields = ['created_at', 'updated_at']
    ordering = ['-last_update']
    list_editable = ['is_active']
    fieldsets = (
        ('Información del Documento', {
            'fields': ('title', 'description', 'file', 'last_update')
        }),
        ('Estado', {
            'fields': ('is_active',)
        }),
        ('Fechas', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

@admin.register(PolicyCategory)
class PolicyCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'icon', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title', 'description']
    readonly_fields = ['created_at', 'updated_at']
    ordering = ['title']
    filter_horizontal = ['documents']

@admin.register(PolicyConfig)
class PolicyConfigAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'created_at', 'updated_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title', 'description']
    readonly_fields = ['created_at', 'updated_at']
    ordering = ['-created_at']
    
    def has_add_permission(self, request):
        # Solo permitir crear si no hay configuraciones activas
        if PolicyConfig.objects.filter(is_active=True).exists():
            return False
        return super().has_add_permission(request) 