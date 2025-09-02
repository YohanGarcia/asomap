import { IconType } from 'react-icons';
import { 
  FiDollarSign, 
  FiCreditCard, 
  FiTrendingUp, 
  FiAward,
  FiHome,
  FiUsers,
  FiFileText,
  FiSettings
} from 'react-icons/fi';

const iconMap: Record<string, IconType> = {
  FiDollarSign,
  FiCreditCard,
  FiTrendingUp,
  FiAward,
  FiHome,
  FiUsers,
  FiFileText,
  FiSettings
};

export const getMenuIconComponent = (iconName: string): IconType => {
  return iconMap[iconName] || FiDollarSign;
};

export const isValidMenuIcon = (iconName: string): boolean => {
  return iconName in iconMap;
};

export const getAvailableMenuIcons = (): string[] => {
  return Object.keys(iconMap);
};
