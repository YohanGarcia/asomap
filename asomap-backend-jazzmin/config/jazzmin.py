"""
Configuración avanzada de Jazzmin para ASOMAP
"""

# Configuración principal de Jazzmin
JAZZMIN_SETTINGS = {
    # Información del sitio
    "site_title": "ASOMAP",  # Título corto para el área del logo
    "site_header": "",  # Sin texto, solo logo
    "site_brand": "",  # Sin texto, solo logo
    "site_logo": "admin/images/logo.png",  # Logo de ASOMAP
    "site_logo_classes": "img-fluid",  # Responsive
    "site_icon": "admin/images/logo.png",  # Favicon
    "welcome_sign": "Bienvenido al Panel de Administración ASOMAP",
    "copyright": "Asociación Mocana de Ahorros y Préstamos",
    "site_url": "/",  # URL principal del sitio
    
    # Colores y tema - Basados en la identidad visual de ASOMAP
    "brand_colour": "info",  # Azul ASOMAP (#2f4495)
    "accent": "accent-warning",  # Acento naranja (#ff9900)
    "navbar": "navbar-info",  # Navbar azul
    "no_navbar_border": False,
    "navbar_fixed": False,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": False,
    "sidebar": "sidebar-dark-info",  # Sidebar azul oscuro
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "cosmo",  # Tema que funciona bien con azules
    "dark_mode_theme": None,
    
    # CSS personalizado para colores ASOMAP
    "custom_css": "admin/css/asomap-jazzmin.css",
    
    # Configuración de archivos estáticos
    "show_ui_builder": False,  # Deshabilitar UI builder para evitar problemas
    "changeform_format": "horizontal_tabs",
    
    # Botones - Colores ASOMAP
    "button_classes": {
        "primary": "btn-info",  # Azul principal ASOMAP (#2f4495)
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-warning",  # Naranja ASOMAP (#ff9900)
        "danger": "btn-danger",
        "success": "btn-warning"  # Naranja para acciones positivas
    },
    
    # Barra lateral
    "show_sidebar": True,
    "navigation_expanded": True,
    
    # Iconos personalizados para cada modelo
    "icons": {
        # Auth
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        
        # About
        "about.Hero": "fas fa-star",
        "about.QuienesSomos": "fas fa-info-circle",
        "about.NuestraHistoria": "fas fa-history",
        "about.Mision": "fas fa-bullseye",
        "about.Vision": "fas fa-eye",
        "about.Valor": "fas fa-heart",
        "about.Director": "fas fa-user-tie",
        "about.CommunitySupport": "fas fa-hands-helping",
        "about.CommunityCategory": "fas fa-tags",
        "about.CommunityInitiative": "fas fa-lightbulb",
        "about.FinancialDocument": "fas fa-file-pdf",
        "about.FinancialStatementsConfig": "fas fa-chart-line",
        "about.MemoryDocument": "fas fa-file-pdf",
        "about.MemoryConfig": "fas fa-book",
        "about.PolicyDocument": "fas fa-file-pdf",
        "about.PolicyCategory": "fas fa-folder",
        "about.PolicyConfig": "fas fa-file-alt",
        
        # Home
        "home.DebitCardPromo": "fas fa-credit-card",
        "home.EducationItem": "fas fa-graduation-cap",
        "home.EducationSection": "fas fa-chalkboard-teacher",
        
        # News
        "news.News": "fas fa-newspaper",
        "news.Promotion": "fas fa-gift",
        
        # Products
        "products.Account": "fas fa-piggy-bank",
        "products.Loan": "fas fa-hand-holding-usd",
        "products.Card": "fas fa-credit-card",
        "products.Certificate": "fas fa-certificate",
        
        # Header
        "header.Navigation": "fas fa-bars",
        "header.ExchangeRate": "fas fa-exchange-alt",
        
        # Layout
        "layout.Footer": "fas fa-shoe-prints",
    },
    
    # Enlaces personalizados
    "custom_links": {
        "about": [{
            "name": "Dashboard",
            "url": "admin:index",
            "icon": "fas fa-tachometer-alt",
        }],
    },
    
    # Configuración de formularios
    "show_ui_builder": True,
    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {
        "auth.user": "collapsible",
        "auth.group": "vertical_tabs",
    },
    
    # Búsqueda
    "search_model": ["auth.User", "about.Hero"],
    
    # Idioma
    "language_chooser": False,
    
    # Notificaciones
    "show_fullsidebar": True,
    
    # Orden de aplicaciones
    "order_with_respect_to": [
        "auth",
        "about",
        "news", 
        "products",
        "header",
        "layout",
    ],
    
    # Configuración de aplicaciones
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "about": "fas fa-info-circle",
        "news": "fas fa-newspaper",
        "products": "fas fa-shopping-cart",
        "header": "fas fa-header",
        "layout": "fas fa-th-large",
    },
    
    # Configuración de modelos específicos
    "related_modal_active": True,
    
    # Configuración de permisos
    "permissions": {
        "auth.user": ["view", "change"],
        "auth.group": ["view", "change"],
    },
}

# Configuración de la UI - Colores ASOMAP
JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": "navbar-info",  # Azul ASOMAP (#2f4495)
    "accent": "accent-warning",  # Acento naranja (#ff9900)
    "navbar": "navbar-info",  # Navbar azul
    "no_navbar_border": False,
    "navbar_fixed": False,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": False,
    "sidebar": "sidebar-dark-info",  # Sidebar azul oscuro
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "cosmo",  # Tema que complementa los azules
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-info",  # Azul principal ASOMAP (#2f4495)
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-warning",  # Naranja ASOMAP (#ff9900)
        "danger": "btn-danger",
        "success": "btn-warning"  # Naranja para acciones positivas
    }
}
