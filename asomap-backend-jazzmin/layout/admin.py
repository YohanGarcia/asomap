from django.contrib import admin
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.utils.html import format_html
from .models import Footer

class BaseModelAdmin(admin.ModelAdmin):
    """Clase base para limpiar formularios después de guardar"""
    
    class Media:
        css = {
            'all': ('admin/css/cards-admin.css',)
        }
        js = ('admin/js/clear_form.js', 'admin/js/cards-view.js')
    
    def get_form(self, request, obj=None, **kwargs):
        """Obtener el formulario y limpiar datos de sesión si es necesario"""
        form = super().get_form(request, obj, **kwargs)
        
        # Si estamos agregando un nuevo objeto (no editando)
        if obj is None:
            # Limpiar datos de sesión que puedan estar causando el problema
            if hasattr(request, 'session'):
                # Limpiar cualquier dato de formulario almacenado en sesión
                session_keys_to_clean = [
                    f'admin:{self.model._meta.app_label}:{self.model._meta.model_name}:add',
                    f'admin:{self.model._meta.app_label}:{self.model._meta.model_name}:change'
                ]
                for key in session_keys_to_clean:
                    if key in request.session:
                        del request.session[key]
        
        return form
    
    def response_add(self, request, obj, post_url_continue=None):
        """Redirigir después de agregar exitosamente"""
        if '_addanother' in request.POST:
            # Limpiar la sesión antes de redirigir
            if hasattr(request, 'session'):
                # Limpiar datos de formulario de la sesión
                session_keys_to_clean = [
                    f'admin:{self.model._meta.app_label}:{self.model._meta.model_name}:add',
                    f'admin:{self.model._meta.app_label}:{self.model._meta.model_name}:change'
                ]
                for key in session_keys_to_clean:
                    if key in request.session:
                        del request.session[key]
            
            # Redirigir a un formulario limpio
            return HttpResponseRedirect(request.path + 'add/')
        return super().response_add(request, obj, post_url_continue)
    
    def response_change(self, request, obj):
        """Redirigir después de cambiar exitosamente"""
        if '_addanother' in request.POST:
            # Limpiar la sesión antes de redirigir
            if hasattr(request, 'session'):
                session_keys_to_clean = [
                    f'admin:{self.model._meta.app_label}:{self.model._meta.model_name}:add',
                    f'admin:{self.model._meta.app_label}:{self.model._meta.model_name}:change'
                ]
                for key in session_keys_to_clean:
                    if key in request.session:
                        del request.session[key]
            
            # Redirigir a un formulario limpio
            return HttpResponseRedirect(request.path.replace(f'{obj.pk}/change/', 'add/'))
        return super().response_change(request, obj)
    
    def add_view(self, request, form_url='', extra_context=None):
        """Vista personalizada para agregar que limpia el formulario"""
        # Limpiar datos de sesión al cargar la vista de agregar
        if hasattr(request, 'session'):
            session_keys_to_clean = [
                f'admin:{self.model._meta.app_label}:{self.model._meta.model_name}:add',
                f'admin:{self.model._meta.app_label}:{self.model._meta.model_name}:change'
            ]
            for key in session_keys_to_clean:
                if key in request.session:
                    del request.session[key]
        
        return super().add_view(request, form_url, extra_context)

@admin.register(Footer)
class FooterAdmin(BaseModelAdmin):
    list_display = ['company_name', 'location_city', 'is_active', 'created_at', 'updated_at']
    list_filter = ['is_active', 'location_city', 'created_at']
    search_fields = ['company_name', 'location_city', 'sections']
    readonly_fields = ['created_at', 'updated_at']
    ordering = ['-created_at']
    
    fieldsets = (
        ('Secciones del Footer', {
            'fields': ('sections',)
        }),
        ('Información de la Empresa', {
            'fields': ('company_name', 'company_description', 'company_phone', 'company_email')
        }),
        ('Información de Ubicación', {
            'fields': ('location_address', 'location_city', 'location_country')
        }),
        ('Estado', {
            'fields': ('is_active',)
        }),
        ('Fechas', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
