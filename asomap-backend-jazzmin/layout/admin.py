from django.contrib import admin
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from .models import Footer, SocialNetwork, Contact

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

@admin.register(SocialNetwork)
class SocialNetworkAdmin(BaseModelAdmin):
    list_display = ['name', 'url', 'icon', 'order', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['name', 'url']
    readonly_fields = ['created_at', 'updated_at']
    ordering = ['order', 'name']
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('name', 'url', 'icon')
        }),
        ('Configuración', {
            'fields': ('order', 'is_active')
        }),
        ('Fechas', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def get_fieldsets(self, request, obj=None):
        """Personalizar fieldsets para incluir guía de iconos"""
        fieldsets = super().get_fieldsets(request, obj)
        
        # Agregar guía de iconos al fieldset de información básica
        if fieldsets:
            # Modificar el primer fieldset para incluir la guía
            basic_info = fieldsets[0]
            if basic_info[0] == 'Información Básica':
                # Crear nuevo fieldset con guía
                new_fieldsets = [
                    ('Información Básica', {
                        'fields': ('name', 'url', 'icon'),
                        'description': mark_safe('''
                        <div style="background: #f8f9fa; padding: 15px; border-radius: 5px; margin: 10px 0; border-left: 4px solid #007bff;">
                            <h4>📱 Guía de Iconos - React Icons</h4>
                            <p><strong>Para encontrar el nombre correcto del icono:</strong></p>
                            <ol>
                                <li>Visita: <a href="https://react-icons.github.io/react-icons/search/#q=fa" target="_blank" style="color: #007bff; text-decoration: none;">React Icons Library</a></li>
                                <li>Busca el icono que necesitas (ej: "facebook", "instagram", "twitter")</li>
                                <li>Copia el nombre exacto del icono (ej: "FaFacebook", "FaInstagram", "FaTwitter")</li>
                                <li>Pégalo en el campo "Icono" de arriba</li>
                            </ol>
                            <p><strong>Ejemplos de iconos populares para redes sociales:</strong></p>
                            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 5px; margin: 10px 0;">
                                <div style="background: white; padding: 8px; border-radius: 3px; border: 1px solid #dee2e6;">
                                    <code style="color: #e83e8c;">FaFacebook</code> (Facebook)
                                </div>
                                <div style="background: white; padding: 8px; border-radius: 3px; border: 1px solid #dee2e6;">
                                    <code style="color: #e83e8c;">FaInstagram</code> (Instagram)
                                </div>
                                <div style="background: white; padding: 8px; border-radius: 3px; border: 1px solid #dee2e6;">
                                    <code style="color: #e83e8c;">FaTwitter</code> (Twitter)
                                </div>
                                <div style="background: white; padding: 8px; border-radius: 3px; border: 1px solid #dee2e6;">
                                    <code style="color: #e83e8c;">FaLinkedin</code> (LinkedIn)
                                </div>
                                <div style="background: white; padding: 8px; border-radius: 3px; border: 1px solid #dee2e6;">
                                    <code style="color: #e83e8c;">FaYoutube</code> (YouTube)
                                </div>
                                <div style="background: white; padding: 8px; border-radius: 3px; border: 1px solid #dee2e6;">
                                    <code style="color: #e83e8c;">FaWhatsapp</code> (WhatsApp)
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
                ] + list(fieldsets[1:])
                return new_fieldsets
        
        return fieldsets

@admin.register(Contact)
class ContactAdmin(BaseModelAdmin):
    list_display = ['name', 'url', 'icon', 'order', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['name', 'url']
    readonly_fields = ['created_at', 'updated_at']
    ordering = ['order', 'name']
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('name', 'url', 'icon')
        }),
        ('Configuración', {
            'fields': ('order', 'is_active')
        }),
        ('Fechas', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def get_fieldsets(self, request, obj=None):
        """Personalizar fieldsets para incluir guía de iconos"""
        fieldsets = super().get_fieldsets(request, obj)
        
        # Agregar guía de iconos al fieldset de información básica
        if fieldsets:
            # Modificar el primer fieldset para incluir la guía
            basic_info = fieldsets[0]
            if basic_info[0] == 'Información Básica':
                # Crear nuevo fieldset con guía
                new_fieldsets = [
                    ('Información Básica', {
                        'fields': ('name', 'url', 'icon'),
                        'description': mark_safe('''
                        <div style="background: #f8f9fa; padding: 15px; border-radius: 5px; margin: 10px 0; border-left: 4px solid #28a745;">
                            <h4>📞 Guía de Iconos - React Icons</h4>
                            <p><strong>Para encontrar el nombre correcto del icono:</strong></p>
                            <ol>
                                <li>Visita: <a href="https://react-icons.github.io/react-icons/search/#q=fa" target="_blank" style="color: #007bff; text-decoration: none;">React Icons Library</a></li>
                                <li>Busca el icono que necesitas (ej: "phone", "envelope", "whatsapp", "map")</li>
                                <li>Copia el nombre exacto del icono (ej: "FaPhone", "FaEnvelope", "FaWhatsapp", "FaMapMarkerAlt")</li>
                                <li>Pégalo en el campo "Icono" de arriba</li>
                            </ol>
                            <p><strong>Ejemplos de iconos populares para contacto:</strong></p>
                            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 5px; margin: 10px 0;">
                                <div style="background: white; padding: 8px; border-radius: 3px; border: 1px solid #dee2e6;">
                                    <code style="color: #e83e8c;">FaPhone</code> (Teléfono)
                                </div>
                                <div style="background: white; padding: 8px; border-radius: 3px; border: 1px solid #dee2e6;">
                                    <code style="color: #e83e8c;">FaEnvelope</code> (Email)
                                </div>
                                <div style="background: white; padding: 8px; border-radius: 3px; border: 1px solid #dee2e6;">
                                    <code style="color: #e83e8c;">FaWhatsapp</code> (WhatsApp)
                                </div>
                                <div style="background: white; padding: 8px; border-radius: 3px; border: 1px solid #dee2e6;">
                                    <code style="color: #e83e8c;">FaMapMarkerAlt</code> (Ubicación)
                                </div>
                                <div style="background: white; padding: 8px; border-radius: 3px; border: 1px solid #dee2e6;">
                                    <code style="color: #e83e8c;">FaClock</code> (Horarios)
                                </div>
                                <div style="background: white; padding: 8px; border-radius: 3px; border: 1px solid #dee2e6;">
                                    <code style="color: #e83e8c;">FaFax</code> (Fax)
                                </div>
                            </div>
                            <div style="background: #d1ecf1; padding: 10px; border-radius: 3px; border-left: 4px solid #bee5eb; margin-top: 15px;">
                                <p style="margin: 0; font-size: 13px; color: #0c5460;">
                                    💡 <strong>Tip:</strong> Para URLs de contacto, usa formatos como:
                                    <br>• <code>tel:+1234567890</code> para teléfonos
                                    <br>• <code>mailto:info@empresa.com</code> para emails
                                    <br>• <code>https://wa.me/1234567890</code> para WhatsApp
                                </p>
                            </div>
                        </div>
                        ''')
                    }),
                ] + list(fieldsets[1:])
                return new_fieldsets
        
        return fieldsets

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
