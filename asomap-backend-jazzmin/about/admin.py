from django.contrib import admin
from django.utils.safestring import mark_safe
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
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('name', 'description')
        }),
        ('Icono', {
            'fields': ('icon',),
            'description': mark_safe('''
            <div style="background: #f8f9fa; padding: 15px; border-radius: 5px; margin: 10px 0; border-left: 4px solid #007bff;">
                <h4 style="margin-top: 0; color: #007bff;">📚 Guía de Iconos - React Icons</h4>
                <p><strong>Para encontrar el nombre correcto del icono:</strong></p>
                <ol>
                    <li>Visita: <a href="https://react-icons.github.io/react-icons/search/#q=fa" target="_blank" style="color: #007bff; text-decoration: none;">React Icons Library</a></li>
                    <li>Busca el icono que necesitas (ej: "heart", "star", "user")</li>
                    <li>Copia el nombre exacto del icono (ej: "FaHeart", "FaStar", "FaUser")</li>
                    <li>Pégalo en el campo "Icono" de arriba</li>
                </ol>
                <p><strong>Ejemplos de iconos populares:</strong></p>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 5px; margin: 10px 0;">
                    <div style="background: white; padding: 8px; border-radius: 3px; border: 1px solid #dee2e6;">
                        <code style="color: #e83e8c;">FaHeart</code> (corazón)
                    </div>
                    <div style="background: white; padding: 8px; border-radius: 3px; border: 1px solid #dee2e6;">
                        <code style="color: #e83e8c;">FaStar</code> (estrella)
                    </div>
                    <div style="background: white; padding: 8px; border-radius: 3px; border: 1px solid #dee2e6;">
                        <code style="color: #e83e8c;">FaUser</code> (usuario)
                    </div>
                    <div style="background: white; padding: 8px; border-radius: 3px; border: 1px solid #dee2e6;">
                        <code style="color: #e83e8c;">FaHome</code> (casa)
                    </div>
                    <div style="background: white; padding: 8px; border-radius: 3px; border: 1px solid #dee2e6;">
                        <code style="color: #e83e8c;">FaBook</code> (libro)
                    </div>
                    <div style="background: white; padding: 8px; border-radius: 3px; border: 1px solid #dee2e6;">
                        <code style="color: #e83e8c;">FaGraduationCap</code> (educación)
                    </div>
                    <div style="background: white; padding: 8px; border-radius: 3px; border: 1px solid #dee2e6;">
                        <code style="color: #e83e8c;">FaHandsHelping</code> (ayuda)
                    </div>
                    <div style="background: white; padding: 8px; border-radius: 3px; border: 1px solid #dee2e6;">
                        <code style="color: #e83e8c;">FaUsers</code> (grupo)
                    </div>
                    <div style="background: white; padding: 8px; border-radius: 3px; border: 1px solid #dee2e6;">
                        <code style="color: #e83e8c;">FaChild</code> (niño)
                    </div>
                    <div style="background: white; padding: 8px; border-radius: 3px; border: 1px solid #dee2e6;">
                        <code style="color: #e83e8c;">FaTree</code> (árbol)
                    </div>
                    <div style="background: white; padding: 8px; border-radius: 3px; border: 1px solid #dee2e6;">
                        <code style="color: #e83e8c;">FaGlobe</code> (mundo)
                    </div>
                    <div style="background: white; padding: 8px; border-radius: 3px; border: 1px solid #dee2e6;">
                        <code style="color: #e83e8c;">FaHandHoldingHeart</code> (solidaridad)
                    </div>
                </div>
                <div style="background: #d1ecf1; padding: 10px; border-radius: 3px; border-left: 4px solid #bee5eb; margin-top: 15px;">
                    <p style="margin: 0; font-size: 13px; color: #0c5460;">
                        💡 <strong>Tip:</strong> Los iconos de Font Awesome (Fa) son los más utilizados. 
                        Asegúrate de usar la nomenclatura exacta que aparece en la librería.
                    </p>
                </div>
            </div>
            ''')
        }),
        ('Estado', {
            'fields': ('is_active',)
        }),
        ('Fechas', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

@admin.register(CommunityInitiative)
class CommunityInitiativeAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'year', 'location', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at', 'category', 'year']
    search_fields = ['title', 'description', 'impact', 'location', 'beneficiaries']
    readonly_fields = ['created_at', 'updated_at']
    ordering = ['category', 'year', 'id']
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('title', 'description', 'impact')
        }),
        ('Detalles de la Iniciativa', {
            'fields': ('year', 'location', 'beneficiaries', 'category')
        }),
        ('Imagen', {
            'fields': ('image_src', 'image_alt'),
            'description': 'Imagen representativa de la iniciativa'
        }),
        ('Estado', {
            'fields': ('is_active',)
        }),
        ('Fechas', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

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