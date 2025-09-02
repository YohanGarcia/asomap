import React, { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { useNavigate } from 'react-router-dom';
import { FiChevronDown, FiUser, FiMapPin, FiCreditCard, FiPhone, FiBook, FiHelpCircle, FiInfo } from 'react-icons/fi';
import { RiBankLine } from "react-icons/ri";
import { MobileMenuProps, MainNavItem, SubNavItem } from '@interfaces';
import { Button } from '@components/ui';
import { buttonLink } from '@/mocks';

export const MobileMenu: React.FC<MobileMenuProps> = ({
  isOpen,
  onClose,
  aboutItems,
  productItems,
  newsItems,
  financialGuidanceItems,
  userSupportItems
}) => {
  const [activeSection, setActiveSection] = useState<string | null>(null);
  const navigate = useNavigate();

  const menuSections = [
    { title: "Nosotros", items: aboutItems, icon: RiBankLine },
    { title: "Productos", items: productItems, icon: FiCreditCard },
    {
      title: "Servicios",
      items: [
        {
          text: "Pagos de Servicios",
          icon: FiPhone,
          to: "/servicios"
        }
      ],
      icon: FiBook
    },
    { title: "Novedades", items: newsItems, icon: FiInfo },
    { title: "Orientación", items: financialGuidanceItems, icon: FiUser },
    { title: "Prousuario", items: userSupportItems, icon: FiHelpCircle }
  ];

  const MenuSection: React.FC<{ section: typeof menuSections[0] }> = ({ section }) => {
    const isActive = activeSection === section.title;
    const Icon = section.icon;

    return (
      <motion.div
        initial={false}
        animate={{ backgroundColor: isActive ? 'rgba(249, 250, 251, 0.8)' : 'transparent' }}
        className="w-full"
      >
        <motion.button
          whileTap={{ scale: 0.98 }}
          className="w-full py-4 px-4 flex items-center justify-between text-left hover:bg-gray-50/30 transition-colors duration-200"
          onClick={() => setActiveSection(isActive ? null : section.title)}
        >
          <div className="flex items-center space-x-3">
            <Icon className="w-5 h-5 text-primary/90" />
            <span className="text-sm font-medium text-gray-800/90">{section.title}</span>
          </div>
          <motion.div
            animate={{ rotate: isActive ? 180 : 0 }}
            transition={{ duration: 0.2 }}
          >
            <FiChevronDown className="w-5 h-5 text-gray-400/90" />
          </motion.div>
        </motion.button>
        <AnimatePresence>
          {isActive && section.items.length > 0 && (
            <motion.div
              initial={{ height: 0, opacity: 0 }}
              animate={{ height: 'auto', opacity: 1 }}
              exit={{ height: 0, opacity: 0 }}
              transition={{ duration: 0.2 }}
              className="bg-gray-50/30"
            >
              {section.items.map((item: MainNavItem, itemIndex: number) => (
                <MenuItem key={itemIndex} item={item} />
              ))}
            </motion.div>
          )}
        </AnimatePresence>
      </motion.div>
    );
  };

  const handlePaymentClick = () => {
    window.open(buttonLink.appLink, '_blank', 'noopener,noreferrer');
  };

  const handleNavigation = (href: string, isExternal: boolean = false) => {
    if (href) {
      if (isExternal) {
        window.open(href, '_blank', 'noopener,noreferrer');
      } else {
        navigate(href);
      }
      onClose();
    }
  };

  const MenuItem: React.FC<{ item: MainNavItem }> = ({ item }) => {
    const [isSubMenuOpen, setIsSubMenuOpen] = useState(false);
    const IconComponent = item.icon;

    const hasSubItems = item.subItems && item.subItems.length > 0;
    const hasMainLink = item.to;

    return (
      <div className="py-1">
        <div className="flex items-center w-full">
          <motion.button
            whileTap={{ scale: 0.98 }}
            className={`flex items-center space-x-3 py-3 px-6 text-left transition-colors duration-200 hover:bg-white/30 ${hasSubItems ? 'flex-1' : 'w-full'}`}
            onClick={() => {
              if (hasMainLink) {
                if (item.isExternalLink) {
                  window.open(item.to!, '_blank', 'noopener,noreferrer');
                  onClose();
                } else {
                  handleNavigation(item.to!);
                }
              }
            }}
          >
            {IconComponent && <IconComponent className="w-5 h-5 text-primary/80" />}
            <span className="text-sm text-gray-700/90">{item.text}</span>
          </motion.button>
          {hasSubItems && (
            <motion.button
              whileTap={{ scale: 0.9 }}
              onClick={() => setIsSubMenuOpen(!isSubMenuOpen)}
              className="p-3 mr-3 hover:bg-gray-50/30 rounded-full transition-colors duration-200"
              aria-label={isSubMenuOpen ? 'Cerrar submenú' : 'Abrir submenú'}
            >
              <motion.div
                animate={{ rotate: isSubMenuOpen ? 180 : 0 }}
                transition={{ duration: 0.2 }}
              >
                <FiChevronDown className="w-4 h-4 text-gray-400/90" />
              </motion.div>
            </motion.button>
          )}
        </div>
        <AnimatePresence>
          {isSubMenuOpen && hasSubItems && (
            <motion.div
              initial={{ height: 0, opacity: 0 }}
              animate={{ height: 'auto', opacity: 1 }}
              exit={{ height: 0, opacity: 0 }}
              transition={{ duration: 0.2 }}
              className="bg-white/30"
            >
              {item.subItems!.map((subItem: SubNavItem, subIndex: number) => (
                <motion.button
                  key={subIndex}
                  whileTap={{ scale: 0.98 }}
                  onClick={() => handleNavigation(subItem.href)}
                  className="w-full py-2.5 px-14 text-left text-sm text-gray-600/90 hover:text-gray-900 hover:bg-gray-50/30 transition-colors duration-200"
                >
                  {subItem.text}
                </motion.button>
              ))}
            </motion.div>
          )}
        </AnimatePresence>
      </div>
    );
  };

  return (
    <AnimatePresence>
      {isOpen && (
        <>
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 0.5 }}
            exit={{ opacity: 0 }}
            onClick={onClose}
            className="fixed top-[80px] inset-x-0 bottom-0 bg-black z-40"
          />
          <motion.div
            initial={{ x: "100%" }}
            animate={{ x: 0 }}
            exit={{ x: "100%" }}
            transition={{ type: "spring", damping: 25, stiffness: 200 }}
            className="fixed top-[80px] right-0 w-[75%] h-[calc(100vh-80px)] bg-gradient-to-b from-white via-white/98 to-white/95 backdrop-blur-sm z-50 overflow-y-auto shadow-lg border-t border-gray-100/50"
          >
            <div className="flex flex-col h-full">
              <div className="flex-1 overflow-y-auto py-6 px-4">
                <motion.div
                  initial={{ y: -10, opacity: 0 }}
                  animate={{ y: 0, opacity: 1 }}
                  transition={{ delay: 0.1 }}
                  className="px-4 pt-3"
                >
                </motion.div>
                <div className="mt-2 divide-y divide-gray-50/50">
                  {menuSections.map((section, index) => (
                    <MenuSection key={index} section={section} />
                  ))}
                </div>
              </div>
              <motion.div
                initial={{ y: 20, opacity: 0 }}
                animate={{ y: 0, opacity: 1 }}
                transition={{ delay: 0.2 }}
                className="sticky bottom-0 p-4 bg-white/90 backdrop-blur-sm space-y-3"
              >
                <motion.div whileHover={{ scale: 1.02 }} whileTap={{ scale: 0.98 }}>
                  <Button
                    className="w-full px-4 py-3 text-sm font-medium text-white bg-orange-400 hover:bg-primary rounded-full flex items-center justify-center space-x-2 transition-colors duration-300"
                    onClick={handlePaymentClick}
                  >
                    <span>Asomap Banking</span>
                  </Button>
                </motion.div>
                <motion.button
                  whileHover={{ scale: 1.02 }}
                  whileTap={{ scale: 0.98 }}
                  onClick={() => handleNavigation('/locations/map')}
                  className="w-full px-4 py-3 text-sm font-medium text-gray-700/90 bg-gray-50/50 hover:bg-gray-100/50 rounded-full flex items-center justify-center space-x-2 transition-colors duration-200"
                >
                  <FiMapPin className="w-4 h-4" />
                  <span>Ubicaciones</span>
                </motion.button>
              </motion.div>
            </div>
          </motion.div>
        </>
      )}
    </AnimatePresence>
  );
};