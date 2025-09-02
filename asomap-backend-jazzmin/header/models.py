from django.db import models

class Navigation(models.Model):
    NAVIGATION_TYPE_CHOICES = [
        ('individual', 'Individual'),
        ('empresarial', 'Empresarial'),
    ]
    
    navigation_type = models.CharField(max_length=20, choices=NAVIGATION_TYPE_CHOICES)
    menu_items = models.TextField(
        blank=True,
        verbose_name="Elementos del menú",
        help_text="Elementos del menú separados por comas (ej: Inicio, Productos, Servicios, Contacto)"
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Navigation"
        verbose_name_plural = "Navigations"
        ordering = ['navigation_type']

    def __str__(self):
        return f"Navigation - {self.get_navigation_type_display()}"

    @property
    def menu_items_list(self):
        """
        Retorna los elementos del menú como lista para el frontend
        """
        if self.menu_items:
            return [item.strip() for item in self.menu_items.split(',') if item.strip()]
        return []

class ExchangeRate(models.Model):
    """
    Modelo para las tasas de cambio que cumple con la estructura del frontend
    """
    # Configuración de visualización
    show_buy_rate = models.BooleanField(
        default=True,
        verbose_name="Mostrar tasa de compra",
        help_text="Indica si se debe mostrar la tasa de compra"
    )
    show_sell_rate = models.BooleanField(
        default=False,
        verbose_name="Mostrar tasa de venta", 
        help_text="Indica si se debe mostrar la tasa de venta"
    )
    
    # Tasas de cambio - Campos individuales para mayor claridad
    currency_name = models.CharField(
        max_length=50,
        default="US DOLAR",
        verbose_name="Nombre de la moneda",
        help_text="Nombre de la moneda (ej: US DOLAR, EURO)"
    )
    buy_rate = models.DecimalField(
        max_digits=10,
        decimal_places=4,
        default=55.50,
        verbose_name="Tasa de compra",
        help_text="Tasa de compra de la moneda"
    )
    sell_rate = models.DecimalField(
        max_digits=10,
        decimal_places=4,
        default=56.50,
        verbose_name="Tasa de venta",
        help_text="Tasa de venta de la moneda"
    )
    
    # Campos de control
    is_active = models.BooleanField(
        default=True,
        verbose_name="Activo",
        help_text="Indica si la tasa de cambio está activa"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Fecha de creación"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Última actualización"
    )

    class Meta:
        verbose_name = "Tasa de Cambio"
        verbose_name_plural = "Tasas de Cambio"
        ordering = ['-updated_at']

    def __str__(self):
        return f"{self.currency_name} - Compra: {self.buy_rate} | Venta: {self.sell_rate}"

    def save(self, *args, **kwargs):
        # Asegurar que solo haya una tasa de cambio activa
        if self.is_active:
            ExchangeRate.objects.exclude(pk=self.pk).update(is_active=False)
        super().save(*args, **kwargs)

    @property
    def last_updated_iso(self):
        """
        Retorna la fecha de actualización en formato ISO para el frontend
        """
        return self.updated_at.isoformat()

    @property
    def rates_for_frontend(self):
        """
        Retorna las tasas en el formato que espera el frontend
        """
        return [{
            'currency': self.currency_name,
            'buyRate': float(self.buy_rate),
            'sellRate': float(self.sell_rate)
        }] 