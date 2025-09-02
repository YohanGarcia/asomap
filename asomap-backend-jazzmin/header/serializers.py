from rest_framework import serializers
from .models import Navigation, ExchangeRate

class NavigationSerializer(serializers.ModelSerializer):
    menu_items = serializers.SerializerMethodField()
    
    class Meta:
        model = Navigation
        fields = '__all__'

    def get_menu_items(self, obj):
        """Retorna los elementos del menú como lista"""
        return obj.menu_items_list

class ExchangeRateSerializer(serializers.ModelSerializer):
    """
    Serializer para las tasas de cambio que cumple con la estructura del frontend
    """
    lastUpdated = serializers.SerializerMethodField()
    showBuyRate = serializers.BooleanField(source='show_buy_rate')
    showSellRate = serializers.BooleanField(source='show_sell_rate')
    rates = serializers.SerializerMethodField()
    
    class Meta:
        model = ExchangeRate
        fields = [
            'id', 'rates', 'showBuyRate', 'showSellRate', 
            'lastUpdated', 'is_active', 'created_at', 'updated_at'
        ]
    
    def get_lastUpdated(self, obj):
        """
        Retorna la fecha de actualización en formato ISO para el frontend
        """
        return obj.last_updated_iso
    
    def get_rates(self, obj):
        """
        Retorna las tasas en el formato que espera el frontend
        """
        return obj.rates_for_frontend

class HeaderCompleteSerializer(serializers.Serializer):
    """
    Serializer para la respuesta completa del header
    que coincide con la estructura del frontend
    """
    navigation = serializers.DictField()
    exchange = serializers.DictField() 