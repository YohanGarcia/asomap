from rest_framework import serializers
from .models import Account, Loan, Card, Certificate

class AccountSerializer(serializers.ModelSerializer):
    bannerImage = serializers.SerializerMethodField()
    accountImage = serializers.SerializerMethodField()
    features = serializers.SerializerMethodField()
    requirements = serializers.SerializerMethodField()
    benefits = serializers.SerializerMethodField()
    slug = serializers.SerializerMethodField()
    
    class Meta:
        model = Account
        fields = [
            'id', 'title', 'description', 'bannerImage', 'accountImage', 
            'category', 'features', 'requirements', 'benefits', 'slug',
            'is_active', 'created_at', 'updated_at'
        ]

    def get_bannerImage(self, obj):
        """Retorna la URL de la imagen de banner"""
        return obj.banner_image_url

    def get_accountImage(self, obj):
        """Retorna la URL de la imagen de la cuenta"""
        return obj.account_image_url

    def get_features(self, obj):
        """Retorna las características como lista"""
        return obj.features_list

    def get_requirements(self, obj):
        """Retorna los requisitos como lista"""
        return obj.requirements_list

    def get_benefits(self, obj):
        """Retorna los beneficios como lista"""
        return obj.benefits_list

    def get_slug(self, obj):
        """Retorna el slug del título"""
        return obj.slug

class LoanSerializer(serializers.ModelSerializer):
    details = serializers.SerializerMethodField()
    requirements = serializers.SerializerMethodField()
    
    class Meta:
        model = Loan
        fields = [
            'id', 'title', 'description', 'loan_type', 'details', 
            'requirements_title', 'requirements', 'is_active', 'created_at', 'updated_at'
        ]

    def get_details(self, obj):
        """Retorna los detalles como lista"""
        return obj.details_list

    def get_requirements(self, obj):
        """Retorna los requisitos como lista"""
        return obj.requirements_list

class CardSerializer(serializers.ModelSerializer):
    bannerImage = serializers.SerializerMethodField()
    cardImage = serializers.SerializerMethodField()
    features = serializers.SerializerMethodField()
    requirements = serializers.SerializerMethodField()
    benefits = serializers.SerializerMethodField()
    slug = serializers.SerializerMethodField()
    
    class Meta:
        model = Card
        fields = [
            'id', 'title', 'description', 'bannerImage', 'cardImage', 
            'card_type', 'features', 'requirements', 'benefits', 'slug',
            'is_active', 'created_at', 'updated_at'
        ]

    def get_bannerImage(self, obj):
        """Retorna la URL de la imagen de banner"""
        return obj.banner_image_url

    def get_cardImage(self, obj):
        """Retorna la URL de la imagen de la tarjeta"""
        return obj.card_image_url

    def get_features(self, obj):
        """Retorna las características como lista"""
        return obj.features_list

    def get_requirements(self, obj):
        """Retorna los requisitos como lista"""
        return obj.requirements_list

    def get_benefits(self, obj):
        """Retorna los beneficios como lista"""
        return obj.benefits_list

    def get_slug(self, obj):
        """Retorna el slug del título"""
        return obj.slug

class CertificateSerializer(serializers.ModelSerializer):
    bannerImage = serializers.SerializerMethodField()
    certificateImage = serializers.SerializerMethodField()
    benefits = serializers.SerializerMethodField()
    rates = serializers.SerializerMethodField()
    depositRates = serializers.SerializerMethodField()
    faq = serializers.SerializerMethodField()
    investment = serializers.SerializerMethodField()
    requirements = serializers.SerializerMethodField()
    slug = serializers.SerializerMethodField()
    
    class Meta:
        model = Certificate
        fields = [
            'id', 'title', 'subtitle', 'description', 'bannerImage', 'certificateImage',
            'certificate_type', 'cta_apply', 'cta_rates', 'benefits_title', 'benefits',
            'investment_title', 'investment_subtitle', 'investment', 'rates_title', 'rates',
            'requirements_title', 'requirements', 'deposit_rates_title', 'depositRates',
            'deposit_rates_valid_from', 'faq_title', 'faq', 'slug', 'is_active', 
            'created_at', 'updated_at'
        ]

    def get_bannerImage(self, obj):
        """Retorna la URL de la imagen de banner"""
        return obj.banner_image_url

    def get_certificateImage(self, obj):
        """Retorna la URL de la imagen del certificado"""
        return obj.certificate_image_url

    def get_benefits(self, obj):
        """Retorna los beneficios como objeto estructurado"""
        return {
            'title': obj.benefits_title,
            'items': obj.benefits_list
        }

    def get_rates(self, obj):
        """Retorna las tarifas como objeto estructurado"""
        return {
            'title': obj.rates_title,
            'items': obj.rates_list
        }

    def get_depositRates(self, obj):
        """Retorna las tasas de depósito como objeto estructurado"""
        return {
            'title': obj.deposit_rates_title,
            'items': obj.deposit_rates_list,
            'validFrom': obj.deposit_rates_valid_from
        }

    def get_faq(self, obj):
        """Retorna las preguntas frecuentes como objeto estructurado"""
        return {
            'title': obj.faq_title,
            'items': obj.faq_list
        }

    def get_investment(self, obj):
        """Retorna la información de inversión como objeto estructurado"""
        return {
            'title': obj.investment_title,
            'subtitle': obj.investment_subtitle,
            'details': obj.investment_details_list,
            'imageUrl': obj.certificate_image_url
        }

    def get_requirements(self, obj):
        """Retorna los requisitos como objeto estructurado"""
        return {
            'title': obj.requirements_title,
            'items': obj.requirements_list
        }

    def get_slug(self, obj):
        """Retorna el slug del título"""
        return obj.slug 