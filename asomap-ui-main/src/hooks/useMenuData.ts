import { useState, useEffect } from 'react';
import { menuService } from '@/api/services/layout/menu';
import { getMenuIconComponent } from '@/utils/menuIconMapper';
// import type { MenuSection } from '@/api/services/layout/menu';
import { IconType } from 'react-icons';

export interface MenuItemWithIcon {
  text: string;
  href: string;
  image: string;
  category: string;
  icon?: IconType;
}

export interface MenuSectionWithIcons {
  text: string;
  icon: IconType;
  subItems: MenuItemWithIcon[];
  image: string;
}

export const useMenuData = () => {
  const [menuData, setMenuData] = useState<MenuSectionWithIcons[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchMenuData = async () => {
      try {
        setLoading(true);
        setError(null);
        
        const menuSections = await menuService.getProductMenuItems();
        
        // Transformar los datos para incluir los iconos
        const menuWithIcons: MenuSectionWithIcons[] = menuSections.map(section => ({
          text: section.text,
          icon: getMenuIconComponent(section.icon),
          subItems: section.subItems,
          image: section.image
        }));

        setMenuData(menuWithIcons);
      } catch (err) {
        console.error('Error fetching menu data:', err);
        setError('Error al cargar el menú');
        // Usar datos por defecto en caso de error
        setMenuData([]);
      } finally {
        setLoading(false);
      }
    };

    fetchMenuData();
  }, []);

  return {
    menuData,
    loading,
    error
  };
};
