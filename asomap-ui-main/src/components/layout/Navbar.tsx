import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import { NavbarProps } from '@interfaces';
import { NavItem } from './NavItem';
import { SearchBar } from './SearchBar';
import { MenuToggle } from './MenuToggle';
import { MobileMenu } from './MobileMenu';
import { Button } from '@components/ui';
import Logo from '@assets/Logo.svg';
import { IoLocationOutline } from 'react-icons/io5';
import { motion } from 'framer-motion';
import { menuItems, buttonLink } from '@mocks';

export const SimpleNavItem: React.FC<{ text: string; to: string; className?: string }> = ({ text, to, className }) => (
  <Link
    to={to}
    className={`flex items-center cursor-pointer text-neutral-200 hover:text-primary-accent transition-colors duration-200 ${className}`}
  >
    <span>{text}</span>
  </Link>
);

export const Navbar: React.FC<NavbarProps> = ({
  isMenuOpen,
  setIsMenuOpen,
  aboutItems = menuItems.aboutItems,
  productItems = menuItems.productItems,
  newsItems,
  financialGuidanceItems = menuItems.financialGuidanceItems,
  userSupportItems,
}) => {
  const [isSearchOpen, setIsSearchOpen] = useState(false);

  const handlePaymentClick = () => {
    window.open(buttonLink.appLink, '_blank', 'noopener,noreferrer');
  };

  return (
    <>
      <nav className="fixed top-[32px] left-0 right-0 z-40 bg-gradient-to-b from-white to-white/98 backdrop-blur-sm h-[48px]">
        <div className="container mx-auto px-3 sm:px-4 max-w-7xl h-full">
          <div className="flex items-center justify-between h-full">
            {/* Logo */}
            <Link
              to="/"
              className="flex items-center"
              onClick={() => {
                window.scrollTo({ top: 0, behavior: 'smooth' });
              }}
              aria-label="Asomap Logo - Ir a inicio"
            >
              <img
                src={Logo}
                alt="Asomap Logo"
                className="w-[100px] h-[30px] sm:w-[120px] sm:h-[34px] lg:w-[140px] lg:h-[38px] transition-all duration-200"
              />
            </Link>

            {/* Desktop Menu */}
            <div className="hidden lg:flex lg:items-center">
              <div className="flex items-center text-neutral-100">
                <NavItem
                  text="Sobre Nosotros"
                  hasDropdown
                  dropdownItems={aboutItems}
                  onLinkClick={() => { }}
                  className="hover:text-primary-accent text-[11px] text-[12px] text-[13px] 2xl:text-base transition-all duration-200 px-1 lg:px-1.5 xl:px-2"
                />
                <NavItem
                  text="Productos"
                  hasDropdown
                  dropdownItems={productItems}
                  onLinkClick={() => { }}
                  className="hover:text-primary-accent text-[11px] text-[12px] text-[13px] 2xl:text-base transition-all duration-200 px-1 lg:px-1.5 xl:px-2"
                />
                <SimpleNavItem
                  text="Servicios"
                  to="/servicios"
                  className="text-[11px] text-[12px] text-[13px] 2xl:text-base hover:text-primary-accent px-1 lg:px-1.5 xl:px-2"
                />
                <NavItem
                  text="Novedades"
                  hasDropdown
                  dropdownItems={newsItems}
                  onLinkClick={() => { }}
                  className="hover:text-primary-accent text-[11px] text-[12px] text-[13px] 2xl:text-base transition-all duration-200 px-1 lg:px-1.5 xl:px-2"
                />
                <NavItem
                  text="Orientación Financiera"
                  hasDropdown
                  dropdownItems={financialGuidanceItems}
                  onLinkClick={() => { }}
                  className="hover:text-primary-accent text-[11px] text-[12px] text-[13px] 2xl:text-base transition-all duration-200 px-1 lg:px-1.5 xl:px-2"
                />
                <NavItem
                  text="Prousuario"
                  hasDropdown
                  dropdownItems={userSupportItems.map(item => ({
                    ...item,
                    isExternalLink: item.isExternalLink
                  }))}
                  onLinkClick={() => { }}
                  className="hover:text-primary-accent text-[11px] text-[12px] text-[13px] 2xl:text-base transition-all duration-200 px-1 lg:px-1.5 xl:px-2"
                />
              </div>

              {/* Desktop Search Bar */}
              <div className="hidden lg:block pl-1 lg:pl-1.5 xl:pl-2">
                <SearchBar
                  isOpen={isSearchOpen}
                  onToggle={() => setIsSearchOpen(!isSearchOpen)}
                  isMobile={false}
                  className="scale-90 lg:scale-95 xl:scale-100"
                />
              </div>

              {/* Desktop Action Buttons */}
              <div className="hidden lg:flex pl-1 lg:pl-1.5 xl:pl-2">
                <motion.div whileHover={{ scale: 1.05 }} whileTap={{ scale: 0.95 }}>
                  <Button
                    className="px-2.5 py-1 xs:py-1.5 sm:py-1.5 text-[11px] xs:text-xs sm:text-xs text-white bg-orange-400 hover:bg-primary rounded-full transition-colors duration-300"
                    onClick={handlePaymentClick}
                  >
                    Asomap Banking
                  </Button>
                </motion.div>

                <motion.div
                  whileHover={{
                    scale: 1.1,
                    rotate: [0, 10, -10, 0],
                    transition: {
                      rotate: {
                        repeat: Infinity,
                        duration: 1,
                        ease: "easeInOut"
                      }
                    }
                  }}
                  whileTap={{ scale: 0.9 }}
                  animate={{
                    y: [-2, 2, -2],
                    scale: [1, 1.05, 1],
                    transition: {
                      y: {
                        repeat: Infinity,
                        duration: 1.5,
                        ease: "easeInOut"
                      },
                      scale: {
                        repeat: Infinity,
                        duration: 2,
                        ease: "easeInOut"
                      }
                    }
                  }}
                  className="ml-1 lg:ml-1.5 xl:ml-2 relative"
                >
                  <div className="absolute inset-0 rounded-full bg-primary-accent/20 animate-ping"></div>
                  <Link
                    to="/locations/map"
                    className="flex items-center justify-center w-6 h-6 lg:w-7 lg:h-7 xl:w-8 xl:h-8 text-gray-600 transition-colors hover:text-primary rounded-full hover:bg-gray-100/50 group relative"
                  >
                    <IoLocationOutline className="w-3 h-3 lg:w-4 lg:h-4 xl:w-5 xl:h-5 text-primary-accent group-hover:text-primary transition-colors" />
                  </Link>
                </motion.div>
              </div>
            </div>

            {/* Mobile Menu Toggle */}
            <div className="flex items-center space-x-2 lg:hidden">
              <SearchBar
                isOpen={isSearchOpen}
                onToggle={() => setIsSearchOpen(!isSearchOpen)}
                isMobile={true}
                className="scale-90"
              />
              <motion.div whileTap={{ scale: 0.95 }}>
                <MenuToggle
                  isOpen={isMenuOpen}
                  onToggle={() => setIsMenuOpen(!isMenuOpen)}
                  className="text-neutral-100 hover:text-primary-accent transition-colors duration-200"
                />
              </motion.div>
            </div>
          </div>
        </div>
      </nav>
      {/* Spacer to push content below navbar */}
      <div className="h-[80px]" />
      {/* Mobile Menu */}
      <MobileMenu
        isOpen={isMenuOpen}
        onClose={() => setIsMenuOpen(false)}
        aboutItems={aboutItems}
        productItems={productItems}
        newsItems={newsItems}
        financialGuidanceItems={financialGuidanceItems}
        userSupportItems={userSupportItems}
        buttonLink={buttonLink}
      />
    </>
  );
};