import React, { useState } from 'react';
import { useLocation } from 'react-router-dom';
import CalculatorModal from './CalculatorModal';
import { FaCalculator } from 'react-icons/fa';
import { motion } from 'framer-motion';

const SideNav: React.FC = () => {
    const [isCalculatorOpen, setIsCalculatorOpen] = useState(false);
    const location = useLocation();

    // No mostrar en la página de ubicaciones
    if (location.pathname === '/locations/map') {
        return null;
    }

    return (
        <>
            <motion.div
                className="fixed left-0 bottom-16 z-30 sm:bottom-20"
                initial={{ x: -32 }}
                animate={{ x: -24 }}
                whileHover={{ x: 0 }}
                transition={{ type: "spring", stiffness: 400, damping: 25 }}
            >
                <motion.button
                    type="button"
                    className="group relative w-14 h-10 sm:w-16 sm:h-12 p-0 rounded-r-2xl overflow-hidden shadow-lg"
                    whileTap={{ scale: 0.95 }}
                    onClick={() => setIsCalculatorOpen(true)}
                    aria-label="Abrir calculadora"
                >
                    <div className="absolute inset-0 bg-gradient-to-br from-primary via-primary to-primary-dark transition-all duration-500 group-hover:scale-105" />
                    <div className="absolute inset-0 opacity-0 group-hover:opacity-100 bg-gradient-to-tl from-primary-dark via-primary to-primary-dark transition-all duration-500" />
                    <div className="absolute inset-0 bg-black/5 rounded-r-2xl backdrop-blur-[1px]" />

                    {/* Efecto de brillo */}
                    <div className="absolute inset-0 opacity-0 group-hover:opacity-100">
                        <div className="absolute inset-y-0 -inset-x-full animate-[shimmer_2s_infinite] bg-gradient-to-r from-transparent via-white/10 to-transparent" />
                    </div>

                    {/* Contenedor del icono */}
                    <div className="relative w-full h-full flex items-center justify-end pr-3 sm:pr-4">
                        <motion.div
                            initial={{ rotate: 0 }}
                            whileHover={{ rotate: 360 }}
                            transition={{ duration: 0.5 }}
                            className="relative z-10"
                        >
                            <FaCalculator className="w-4 h-4 sm:w-5 sm:h-5 text-white drop-shadow-lg transition-transform duration-300 group-hover:scale-110" />
                        </motion.div>
                    </div>
                </motion.button>
            </motion.div>

            <CalculatorModal isOpen={isCalculatorOpen} closeModal={() => setIsCalculatorOpen(false)} />
        </>
    );
};

export default SideNav;