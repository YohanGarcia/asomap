from django.contrib import admin
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.utils.html import format_html
from .models import Navigation, ExchangeRate

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

@admin.register(Navigation)
class NavigationAdmin(BaseModelAdmin):
    list_display = ['navigation_type', 'is_active', 'created_at', 'updated_at']
    list_filter = ['is_active', 'created_at', 'navigation_type']
    search_fields = ['navigation_type']
    readonly_fields = ['created_at', 'updated_at']
    ordering = ['navigation_type']

@admin.register(ExchangeRate)
class ExchangeRateAdmin(BaseModelAdmin):
    list_display = ['currency_name', 'buy_rate', 'sell_rate', 'show_buy_rate', 'show_sell_rate', 'is_active', 'updated_at']
    list_filter = ['is_active', 'show_buy_rate', 'show_sell_rate', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']
    ordering = ['-updated_at']
    
    fieldsets = (
        ('Información de la Moneda', {
            'fields': ('currency_name', 'buy_rate', 'sell_rate')
        }),
        ('Configuración de Visualización', {
            'fields': ('show_buy_rate', 'show_sell_rate')
        }),
        ('Estado', {
            'fields': ('is_active',)
        }),
        ('Fechas', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def has_add_permission(self, request):
        # Solo permitir crear si no hay tasas activas
        if ExchangeRate.objects.filter(is_active=True).exists():
            return False
        return super().has_add_permission(request)
