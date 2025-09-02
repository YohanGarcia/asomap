from django.contrib import admin
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.utils.html import format_html
from .models import (
    Account, Loan, Card, Certificate, 
    AccountBenefit, CardBenefit, 
    CertificateBenefit, CertificateRate, CertificateDepositRate, CertificateFAQ
)

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


@admin.register(AccountBenefit)
class AccountBenefitAdmin(admin.ModelAdmin):
    list_display = ['account', 'icon', 'text']
    list_filter = ['account', 'icon']
    search_fields = ['text', 'account__title']
    ordering = ['account', 'id']
    
    fieldsets = (
        ('Información del Beneficio', {
            'fields': ('account', 'icon', 'text')
        }),
    )


@admin.register(CardBenefit)
class CardBenefitAdmin(admin.ModelAdmin):
    list_display = ['card', 'icon', 'text']
    list_filter = ['card', 'icon']
    search_fields = ['text', 'card__title']
    ordering = ['card', 'id']
    
    fieldsets = (
        ('Información del Beneficio', {
            'fields': ('card', 'icon', 'text')
        }),
    )


@admin.register(CertificateBenefit)
class CertificateBenefitAdmin(admin.ModelAdmin):
    list_display = ['certificate', 'title']
    list_filter = ['certificate']
    search_fields = ['title', 'description', 'certificate__title']
    ordering = ['certificate', 'id']
    
    fieldsets = (
        ('Información del Beneficio', {
            'fields': ('certificate', 'title', 'description')
        }),
    )


@admin.register(CertificateRate)
class CertificateRateAdmin(admin.ModelAdmin):
    list_display = ['certificate', 'label', 'value']
    list_filter = ['certificate']
    search_fields = ['label', 'value', 'certificate__title']
    ordering = ['certificate', 'id']
    
    fieldsets = (
        ('Información de la Tarifa', {
            'fields': ('certificate', 'label', 'value')
        }),
    )


@admin.register(CertificateDepositRate)
class CertificateDepositRateAdmin(admin.ModelAdmin):
    list_display = ['certificate', 'range', 'rate', 'term']
    list_filter = ['certificate']
    search_fields = ['range', 'rate', 'term', 'certificate__title']
    ordering = ['certificate', 'id']
    
    fieldsets = (
        ('Información de la Tasa de Depósito', {
            'fields': ('certificate', 'range', 'rate', 'term')
        }),
    )


@admin.register(CertificateFAQ)
class CertificateFAQAdmin(admin.ModelAdmin):
    list_display = ['certificate', 'question']
    list_filter = ['certificate']
    search_fields = ['question', 'answer', 'certificate__title']
    ordering = ['certificate', 'id']
    
    fieldsets = (
        ('Información de la FAQ', {
            'fields': ('certificate', 'question', 'answer')
        }),
    )


@admin.register(Account)
class AccountAdmin(BaseModelAdmin):
    list_display = ['title', 'category', 'is_active', 'created_at', 'updated_at']
    list_filter = ['is_active', 'created_at', 'category']
    search_fields = ['title', 'description', 'features', 'requirements']
    readonly_fields = ['created_at', 'updated_at']
    ordering = ['-created_at']
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('title', 'description', 'category')
        }),
        ('Imágenes', {
            'fields': ('banner_image', 'account_image'),
            'description': 'Imágenes para la cuenta'
        }),
        ('Características', {
            'fields': ('features',),
            'description': 'Características del producto separadas por comas'
        }),
        ('Requisitos', {
            'fields': ('requirements',),
            'description': 'Requisitos para abrir la cuenta separados por comas'
        }),
        ('Estado', {
            'fields': ('is_active',)
        }),
        ('Fechas', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

@admin.register(Loan)
class LoanAdmin(BaseModelAdmin):
    list_display = ['title', 'loan_type', 'is_active', 'created_at', 'updated_at']
    list_filter = ['is_active', 'created_at', 'loan_type']
    search_fields = ['title', 'description', 'details', 'requirements']
    readonly_fields = ['created_at', 'updated_at']
    ordering = ['-created_at']
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('title', 'description', 'loan_type')
        }),
        ('Detalles del Préstamo', {
            'fields': ('details',),
            'description': 'Detalles del préstamo separados por comas'
        }),
        ('Requisitos', {
            'fields': ('requirements_title', 'requirements'),
            'description': 'Título y requisitos del préstamo separados por comas'
        }),
        ('Estado', {
            'fields': ('is_active',)
        }),
        ('Fechas', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

@admin.register(Card)
class CardAdmin(BaseModelAdmin):
    list_display = ['title', 'card_type', 'is_active', 'created_at', 'updated_at']
    list_filter = ['is_active', 'created_at', 'card_type']
    search_fields = ['title', 'description', 'features', 'requirements']
    readonly_fields = ['created_at', 'updated_at']
    ordering = ['-created_at']
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('title', 'description', 'card_type')
        }),
        ('Imágenes', {
            'fields': ('banner_image', 'card_image'),
            'description': 'Imágenes para la tarjeta'
        }),
        ('Características', {
            'fields': ('features',),
            'description': 'Características de la tarjeta separadas por comas'
        }),
        ('Requisitos', {
            'fields': ('requirements',),
            'description': 'Requisitos para obtener la tarjeta separados por comas'
        }),
        ('Estado', {
            'fields': ('is_active',)
        }),
        ('Fechas', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

@admin.register(Certificate)
class CertificateAdmin(BaseModelAdmin):
    list_display = ['title', 'certificate_type', 'is_active', 'created_at', 'updated_at']
    list_filter = ['is_active', 'created_at', 'certificate_type']
    search_fields = ['title', 'subtitle', 'description', 'requirements']
    readonly_fields = ['created_at', 'updated_at']
    ordering = ['-created_at']
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('title', 'subtitle', 'description', 'certificate_type')
        }),
        ('Imágenes', {
            'fields': ('banner_image', 'certificate_image'),
            'description': 'Imágenes para el certificado'
        }),
        ('Call to Action', {
            'fields': ('cta_apply', 'cta_rates'),
            'description': 'Textos de los botones de acción'
        }),
        ('Beneficios', {
            'fields': ('benefits_title',),
            'description': 'Título de la sección de beneficios'
        }),
        ('Inversión', {
            'fields': ('investment_title', 'investment_subtitle', 'investment_details'),
            'description': 'Información de la inversión'
        }),
        ('Tarifas', {
            'fields': ('rates_title',),
            'description': 'Título de la sección de tarifas'
        }),
        ('Requisitos', {
            'fields': ('requirements_title', 'requirements'),
            'description': 'Título y requisitos del certificado'
        }),
        ('Tasas de Depósito', {
            'fields': ('deposit_rates_title', 'deposit_rates_valid_from'),
            'description': 'Información de tasas de depósito'
        }),
        ('Preguntas Frecuentes', {
            'fields': ('faq_title',),
            'description': 'Título de la sección de FAQ'
        }),
        ('Estado', {
            'fields': ('is_active',)
        }),
        ('Fechas', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
