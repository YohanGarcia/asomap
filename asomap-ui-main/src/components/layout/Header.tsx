import React, { useEffect } from 'react';
import { motion } from 'framer-motion';
import { FaDollarSign } from 'react-icons/fa';
import { Link } from 'react-router-dom';
import { useLayoutStore } from '@/store';
import { useQuery } from '@tanstack/react-query';
import { headerService } from '@/api';
import { NavigationResponse, ExchangeRateResponse } from '@/interfaces';

interface HeaderProps {
    isMobile: boolean;
}

export const Header: React.FC<HeaderProps> = () => {
    const { headerData, setHeaderData } = useLayoutStore();

    const { data: navigationData } = useQuery<NavigationResponse>({
        queryKey: ['navigation'],
        queryFn: headerService.getNavigation
    });

    const { data: exchangeData } = useQuery<ExchangeRateResponse>({
        queryKey: ['exchange'],
        queryFn: headerService.getExchangeRate
    });

    useEffect(() => {
        if (navigationData && exchangeData) {
            setHeaderData({
                navigation: navigationData,
                exchange: exchangeData
            });
        }
    }, [navigationData, exchangeData, setHeaderData]);

    return (
        <header className="fixed top-0 left-0 right-0 z-50 bg-gray-200 text-neutral-900 
            font-['Open_Sans'] text-xs font-light leading-[16.34px] h-8">
            <div className="container mx-auto px-3 sm:px-4 max-w-7xl h-full">
                <div className="flex items-center justify-between h-full">
                    <div className="flex space-x-4 items-center justify-start md:ml-[160px]">
                        <Link
                            to="/"
                            className="font-medium cursor-pointer text-xs hover:text-primary transition-colors duration-200 underline decoration-2 decoration-primary-accent hover:decoration-secondary"
                        >
                            {headerData.navigation.individual}
                        </Link>
                        <Link
                            to="/empresa"
                            className="cursor-pointer font-medium text-xs hover:text-primary transition-colors duration-200  decoration-neutral-900 hover:decoration-secondary"
                        >
                            {headerData.navigation.empresarial}
                        </Link>
                    </div>

                    <div className="flex items-center space-x-4">
                        {headerData.exchange && headerData.exchange.rates?.length > 0 && (
                            <div className="flex items-center space-x-2 text-white/90">
                                <span className="hidden md:block text-primary font-bold">{headerData.exchange.base}</span>
                                <motion.div
                                    whileHover={{ scale: 1.05 }}
                                    className="flex items-center px-1.5 py-0.5 md:px-2.5 md:py-1 font-bold text-neutral-100 rounded-full bg-white"
                                >
                                    <FaDollarSign className="w-2 h-2 md:w-3 md:h-3 mr-1 text-neutral-100" />
                                    <span className="text-xs">{headerData.exchange.rates[0].currency}</span>
                                </motion.div>
                                <div className="flex items-center space-x-1 sm:space-x-2">
                                    {headerData.exchange.showBuyRate && (
                                        <div className="flex items-center space-x-1">
                                            <span className="text-[10px] sm:text-[11px] text-neutral-100 font-semibold">Compra:</span>
                                            <span className="text-[10px] sm:text-[11px] font-bold text-neutral-100">
                                                {headerData.exchange.rates[0].buyRate.toFixed(2)}
                                            </span>
                                        </div>
                                    )}
                                    {headerData.exchange.showSellRate && (
                                        <div className="flex items-center space-x-1">
                                            <span className="text-[10px] sm:text-[11px] text-neutral-100 font-semibold">Venta:</span>
                                            <span className="text-[10px] sm:text-[11px] font-bold text-neutral-100">
                                                {headerData.exchange.rates[0].sellRate.toFixed(2)}
                                            </span>
                                        </div>
                                    )}
                                </div>
                            </div>
                        )}
                    </div>
                </div>
            </div>
        </header>
    );
};