import { IconType } from 'react-icons';

// Interfaz para los subelementos de navegación
export interface SubNavItem {
    text: string;
    href: string;
    icon?: IconType;
    image?: string;
}

// Interfaz para los elementos principales de la barra de navegación
export interface MainNavItem {
    text: string;
    icon: IconType;
    to?: string;
    subItems?: SubNavItem[];
    image?: string;
    isExternalLink?: boolean;
}

// Interfaz para las props del componente NavItem
export interface NavItemProps {
    text: string;
    to?: string;
    className?: string;
    hasDropdown?: boolean;
    icon?: React.ReactNode;
    dropdownItems?: MainNavItem[];
    onLinkClick: () => void;
    isExternalLink?: boolean;
}

// Interfaz para las props del componente NavBar
export interface NavbarProps {
    isMenuOpen: boolean;
    setIsMenuOpen: React.Dispatch<React.SetStateAction<boolean>>;
    aboutItems: MainNavItem[];
    productItems: MainNavItem[];
    newsItems: MainNavItem[];
    financialGuidanceItems: MainNavItem[];
    userSupportItems: MainNavItem[];
    buttonLink: IButtonLink;
}

// Interfaz para las props del componente MobileMenu
export interface MobileMenuProps {
    isOpen: boolean;
    onClose: () => void;
    aboutItems: MainNavItem[];
    productItems: MainNavItem[];
    newsItems: MainNavItem[];
    financialGuidanceItems: MainNavItem[];
    userSupportItems: MainNavItem[];
    buttonLink: IButtonLink;
}

export interface IButtonLink {
    appLink?: string;
}


export interface MenuItem {
    text: string;
    to?: string;
    href?: string;
    subItems?: MenuItem[];
}

export interface MenuResponse {
    aboutItems: MenuItem[];
    productItems: MenuItem[];
    newsItems: MenuItem[];
    financialGuidanceItems: MenuItem[];
    userSupportItems: MenuItem[];
}
