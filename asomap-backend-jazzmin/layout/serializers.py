from rest_framework import serializers
from .models import Footer, SocialNetwork, Contact

class FooterSerializer(serializers.ModelSerializer):
    sections = serializers.SerializerMethodField()
    company = serializers.SerializerMethodField()
    location = serializers.SerializerMethodField()
    
    class Meta:
        model = Footer
        fields = '__all__'

    def get_sections(self, obj):
        """Retorna las secciones como lista"""
        return obj.sections_list

    def get_company(self, obj):
        """Retorna la información de la empresa como diccionario"""
        return obj.company_dict

    def get_location(self, obj):
        """Retorna la información de ubicación como diccionario"""
        return obj.location_dict

class SocialNetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialNetwork
        fields = [
            'id', 'name', 'url', 'icon', 'order', 'is_active', 
            'created_at', 'updated_at'
        ]

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = [
            'id', 'name', 'url', 'icon', 'order', 'is_active', 
            'created_at', 'updated_at'
        ]