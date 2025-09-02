import React, { useState, useEffect, useRef } from 'react';
import { FiSearch, FiX } from 'react-icons/fi';
import { useNavigate } from 'react-router-dom';
import { motion, AnimatePresence } from 'framer-motion';
import {
    aboutItems,
    productItems,
    newsItems,
    financialGuidanceItems,
    userSupportItems,
} from '@/mocks';

interface ISearchBarProps {
    isOpen: boolean;
    onToggle: () => void;
    isMobile: boolean;
    className?: string;
}

interface ISearchItem {
    text: string;
    href: string;
    category?: string;
}

const searchCategories = {
    PRODUCTS: 'Productos',
    NEWS: 'Noticias',
    GUIDANCE: 'Orientación Financiera',
    SUPPORT: 'Soporte',
};

export const SearchBar: React.FC<ISearchBarProps> = ({ isOpen, onToggle, isMobile, className = '' }) => {
    const [searchTerm, setSearchTerm] = useState('');
    const [searchResults, setSearchResults] = useState<ISearchItem[]>([]);
    const [showResults, setShowResults] = useState(false);
    const [selectedCategory, setSelectedCategory] = useState<string | null>(null);
    const navigate = useNavigate();
    const searchRef = useRef<HTMLDivElement>(null);
    const inputRef = useRef<HTMLInputElement>(null);

    // Prepare all searchable items
    const allItems: ISearchItem[] = [
        // About
        ...aboutItems.flatMap(item =>
            item.subItems
                ? item.subItems.map(subItem => ({
                    text: subItem.text,
                    href: subItem.href || '',
                    category: searchCategories.PRODUCTS
                }))
                : [{
                    text: item.text,
                    href: item.to || '',
                    category: searchCategories.PRODUCTS
                }]
        ),
        // Products
        ...productItems.flatMap(item =>
            item.subItems
                ? item.subItems.map(subItem => ({
                    text: subItem.text,
                    href: subItem.href || '',
                    category: searchCategories.PRODUCTS
                }))
                : [{
                    text: item.text,
                    href: item.to || '',
                    category: searchCategories.PRODUCTS
                }]
        ),
        // Services
        {
            text: 'Pagos de Servicios',
            href: '/servicios'
        },
        // News
        ...newsItems.flatMap(item =>
            item.subItems
                ? item.subItems.map(subItem => ({
                    text: subItem.text,
                    href: subItem.href || '',
                    category: searchCategories.NEWS
                }))
                : [{
                    text: item.text,
                    href: item.to || '',
                    category: searchCategories.NEWS
                }]
        ),
        // Financial Guidance
        ...financialGuidanceItems.flatMap(item =>
            item.subItems
                ? item.subItems.map(subItem => ({
                    text: subItem.text,
                    href: subItem.href || '',
                    category: searchCategories.GUIDANCE
                }))
                : [{
                    text: item.text,
                    href: item.to || '',
                    category: searchCategories.GUIDANCE
                }]
        ),
        // Support
        ...userSupportItems.flatMap(item =>
            item.subItems
                ? item.subItems.map(subItem => ({
                    text: subItem.text,
                    href: subItem.href || '',
                    category: searchCategories.SUPPORT
                }))
                : [{
                    text: item.text,
                    href: item.to || '',
                    category: searchCategories.SUPPORT
                }]
        )
    ].filter(item => item.href !== '');

    useEffect(() => {
        const handleClickOutside = (event: MouseEvent) => {
            if (searchRef.current && !searchRef.current.contains(event.target as Node)) {
                setShowResults(false);
            }
        };

        document.addEventListener('mousedown', handleClickOutside);
        return () => {
            document.removeEventListener('mousedown', handleClickOutside);
        };
    }, []);

    useEffect(() => {
        if (isOpen && inputRef.current) {
            inputRef.current.focus();
        }
    }, [isOpen]);

    const handleSearch = (e: React.ChangeEvent<HTMLInputElement>) => {
        const term = e.target.value;
        setSearchTerm(term);

        if (term.length > 0) {
            const filteredResults = allItems.filter(item => {
                const matchesSearch = item.text.toLowerCase().includes(term.toLowerCase());
                return selectedCategory
                    ? matchesSearch && item.category === selectedCategory
                    : matchesSearch;
            });

            // Sort results by relevance
            filteredResults.sort((a, b) => {
                const aStartsWith = a.text.toLowerCase().startsWith(term.toLowerCase());
                const bStartsWith = b.text.toLowerCase().startsWith(term.toLowerCase());
                if (aStartsWith && !bStartsWith) return -1;
                if (!aStartsWith && bStartsWith) return 1;
                return 0;
            });

            setSearchResults(filteredResults);
            setShowResults(true);
        } else {
            setSearchResults([]);
            setShowResults(false);
        }
    };

    const handleResultClick = (href: string) => {
        navigate(href);
        setShowResults(false);
        setSearchTerm('');
        if (isMobile) {
            onToggle();
        }
    };

    const handleKeyDown = (e: React.KeyboardEvent<HTMLInputElement>) => {
        if (e.key === 'Escape') {
            setShowResults(false);
            setSearchTerm('');
            if (isMobile) {
                onToggle();
            }
        }
    };

    const handleCategoryClick = (category: string) => {
        setSelectedCategory(category === selectedCategory ? null : category);
    };

    return (
        <div ref={searchRef} className={`relative ${isMobile ? 'w-full' : ''} ${className}`}>
            <AnimatePresence>
                {(!isMobile || (isMobile && isOpen)) && (
                    <motion.div
                        initial={{ opacity: 0, y: -10 }}
                        animate={{ opacity: 1, y: 0 }}
                        exit={{ opacity: 0, y: -10 }}
                        transition={{ duration: 0.2 }}
                        className={`relative ${isMobile ? 'w-full' : 'w-auto'}`}
                    >
                        <input
                            ref={inputRef}
                            type="text"
                            placeholder="Buscar en toda la página..."
                            value={searchTerm}
                            onChange={handleSearch}
                            onKeyDown={handleKeyDown}
                            className={`
                                py-0.5 xs:py-1 sm:py-1.5 pl-6 xs:pl-7 sm:pl-8 pr-2 xs:pr-2.5 sm:pr-3
                                text-[10px] xs:text-[11px] sm:text-xs
                                border border-gray-200 rounded-full
                                focus:outline-none focus:ring-2 focus:ring-primary-accent focus:border-transparent
                                transition-all duration-200 ease-in-out
                                ${isMobile ? 'w-full' : 'w-24 xs:w-28 sm:w-32 md:w-36 lg:w-40 xl:w-44 2xl:w-48'}
                                ${showResults ? 'rounded-b-none' : ''}
                                bg-white/90 backdrop-blur-sm
                            `}
                        />
                        <FiSearch className="absolute w-3 h-3 xs:w-3.5 xs:h-3.5 sm:w-4 sm:h-4 text-gray-400 transform -translate-y-1/2 left-1.5 xs:left-2 sm:left-2.5 top-1/2" />
                        {searchTerm && (
                            <button
                                onClick={() => {
                                    setSearchTerm('');
                                    setShowResults(false);
                                }}
                                className="absolute right-1.5 xs:right-2 sm:right-2.5 top-1/2 transform -translate-y-1/2 hover:text-primary-accent transition-colors"
                            >
                                <FiX className="w-3 h-3 xs:w-3.5 xs:h-3.5 sm:w-4 sm:h-4 text-gray-400" />
                            </button>
                        )}
                    </motion.div>
                )}
            </AnimatePresence>

            {!isMobile && !isOpen && (
                <button
                    className="lg:hidden text-neutral-200 hover:text-primary-accent transition-colors"
                    onClick={onToggle}
                    aria-label="Buscar..."
                >
                    <FiSearch className="w-5 h-5" />
                </button>
            )}

            <AnimatePresence>
                {showResults && searchResults.length > 0 && (
                    <motion.div
                        initial={{ opacity: 0, y: -10 }}
                        animate={{ opacity: 1, y: 0 }}
                        exit={{ opacity: 0 }}
                        transition={{ duration: 0.2 }}
                        className={`
                            absolute z-[60] bg-white rounded-b-lg shadow-lg
                            ${isMobile ? 'w-full' : 'w-full min-w-[200px] xs:min-w-[220px] sm:min-w-[240px] md:min-w-[260px] lg:min-w-[280px] xl:min-w-[300px]'}
                            max-h-[45vh] xs:max-h-[50vh] sm:max-h-[55vh] md:max-h-[60vh] lg:max-h-[65vh] overflow-y-auto
                            border border-t-0 border-gray-200
                        `}
                    >
                        <div className="sticky top-0 bg-white border-b border-gray-100 p-1 xs:p-1.5 sm:p-2 flex flex-wrap gap-1 xs:gap-1.5 sm:gap-2">
                            {Object.entries(searchCategories).map(([key, value]) => (
                                <button
                                    key={key}
                                    onClick={() => handleCategoryClick(value)}
                                    className={`
                                        px-1 xs:px-1.5 sm:px-2 py-0.5 text-[8px] xs:text-[9px] sm:text-[10px] rounded-full transition-all
                                        ${selectedCategory === value
                                            ? 'bg-primary text-white'
                                            : 'bg-gray-100 text-gray-600 hover:bg-gray-200'
                                        }
                                    `}
                                >
                                    {value}
                                </button>
                            ))}
                        </div>

                        {searchResults.map((item, index) => (
                            <motion.div
                                key={index}
                                initial={{ opacity: 0 }}
                                animate={{ opacity: 1 }}
                                transition={{ delay: index * 0.05 }}
                                className="group"
                            >
                                <button
                                    className="w-full px-2 xs:px-3 sm:px-4 py-1.5 xs:py-2 sm:py-3 text-left cursor-pointer hover:bg-gray-50 transition-colors"
                                    onClick={() => handleResultClick(item.href)}
                                >
                                    <div className="flex flex-col">
                                        <span className="text-[11px] xs:text-xs sm:text-sm font-medium text-gray-700 group-hover:text-primary-accent transition-colors">
                                            {item.text}
                                        </span>
                                        <span className="text-[9px] xs:text-[10px] sm:text-xs text-primary-accent/70 mt-0.5 sm:mt-1">
                                            {item.category}
                                        </span>
                                    </div>
                                </button>
                                {index < searchResults.length - 1 && (
                                    <div className="mx-4 border-b border-gray-100" />
                                )}
                            </motion.div>
                        ))}
                    </motion.div>
                )}
            </AnimatePresence>
        </div>
    );
};

export default SearchBar;