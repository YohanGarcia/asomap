import React from 'react';
import { motion } from 'framer-motion';
import { RiMenu3Line, RiCloseLine } from 'react-icons/ri';

interface MenuToggleProps {
    isOpen: boolean;
    onToggle: () => void;
    className?: string;
}

export const MenuToggle: React.FC<MenuToggleProps> = ({ isOpen, onToggle, className }) => {
    return (
        <motion.button
            className={`relative flex items-center justify-center w-10 h-10 ${className || ''}`}
            onClick={onToggle}
            whileTap={{ scale: 0.95 }}
            aria-label={isOpen ? 'Cerrar menú' : 'Abrir menú'}
            aria-expanded={isOpen}
        >
            {isOpen ? (
                <RiCloseLine className="w-7 h-7" />
            ) : (
                <RiMenu3Line className="w-7 h-7" />
            )}
        </motion.button>
    );
};