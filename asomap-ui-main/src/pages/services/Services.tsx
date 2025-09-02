import React, { useEffect, useState, useCallback } from 'react';
import { servicesService } from '@/api';
import type { IServicesPageData, IServiceInfoData } from '@/interfaces';
import { Button, Spinner } from '@/components/ui';
import { HiChevronRight, HiChevronDown } from 'react-icons/hi';
import { motion, AnimatePresence } from 'framer-motion';
import { FaSearch, FaFilePdf } from 'react-icons/fa';
import { PDFPreview } from '@/components';

const Services: React.FC = () => {
  const [servicesData, setServicesData] = useState<IServicesPageData | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [selectedService, setSelectedService] = useState<IServiceInfoData | null>(null);
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const [searchTerm, setSearchTerm] = useState('');
  const [showPreview, setShowPreview] = useState(false);

  const handleMouseEnter = useCallback(() => {
    setShowPreview(true);
  }, []);

  const handleMouseLeave = useCallback(() => {
    setShowPreview(false);
  }, []);

  useEffect(() => {
    window.scrollTo(0, 0);
    
    const fetchServicesData = async () => {
      try {
        setLoading(true);
        const data = await servicesService.getServicesPage();
        setServicesData(data);
      } catch (err) {
        setError(err instanceof Error ? err.message : 'Error al cargar los servicios');
      } finally {
        setLoading(false);
      }
    };

    fetchServicesData();
  }, []);

  if (loading) {
    return (
      <div className="min-h-screen bg-gradient-to-b from-white to-blue-50/30 flex items-center justify-center">
        <Spinner />
      </div>
    );
  }

  if (error || !servicesData) {
    return (
      <div className="min-h-screen bg-gradient-to-b from-white to-blue-50/30 flex items-center justify-center">
        <div className="text-center">
          <h2 className="text-xl font-semibold text-gray-800 mb-2">
            Error al cargar los servicios
          </h2>
          <p className="text-gray-600">{error}</p>
        </div>
      </div>
    );
  }

  const filteredServices = servicesData.items.filter((item, index) => {
    const service = servicesData.itemDetails[index];
    return (
      item.toLowerCase().includes(searchTerm.toLowerCase()) ||
      service.description.toLowerCase().includes(searchTerm.toLowerCase())
    );
  });

  const sectionVariants = {
    hidden: { opacity: 0 },
    visible: {
      opacity: 1,
      transition: { staggerChildren: 0.1 }
    }
  };

  const renderServiceContent = () => {
    if (!selectedService) {
      return (
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          exit={{ opacity: 0, y: -20 }}
          className="p-4 sm:p-6 lg:p-8"
        >
          <div className="text-center max-w-3xl mx-auto">
            <h2 className="text-2xl md:text-3xl lg:text-4xl font-bold text-primary mb-4 lg:mb-6 bg-gradient-to-r from-primary to-blue-600 bg-clip-text text-transparent">
              {servicesData.title}
            </h2>
            <p className="text-neutral-600 text-base lg:text-lg mb-6 lg:mb-8 leading-relaxed">
              {servicesData.subtitle}
            </p>
            <Button
              onClick={() => window.open(servicesData.internetBankingUrl, '_blank')}
              className="bg-primary hover:bg-primary-dark text-white font-semibold px-6 py-3 rounded-lg shadow-lg hover:shadow-xl transition-all duration-300 mb-8"
            >
              {servicesData.internetBankingButton}
            </Button>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 lg:gap-6 mt-8 lg:mt-12">
            {filteredServices.map((item, index) => (
              <motion.div
                key={index}
                whileHover={{ scale: 1.02 }}
                whileTap={{ scale: 0.98 }}
                className="bg-white rounded-xl shadow-lg hover:shadow-xl transition-all duration-300 overflow-hidden cursor-pointer"
                onClick={() => {
                  setSelectedService(servicesData.itemDetails[index]);
                  setIsMenuOpen(false);
                }}
              >
                <div className="p-4 lg:p-5">
                  <h3 className="text-lg lg:text-xl font-semibold text-primary mb-2 lg:mb-3">{item}</h3>
                  <p className="text-neutral-600 text-sm lg:text-base">
                    {servicesData.itemDetails[index].description.substring(0, 100)}...
                  </p>
                </div>
              </motion.div>
            ))}
          </div>
        </motion.div>
      );
    }

    return (
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        exit={{ opacity: 0, y: -20 }}
        className="p-4 sm:p-6 lg:p-8"
      >
        <div className="max-w-4xl mx-auto">
          <div className="bg-white rounded-xl shadow-lg p-4 lg:p-6">
            <h2 className="text-2xl lg:text-3xl font-bold text-primary mb-4">{selectedService.title}</h2>
            <p className="text-neutral-600 mb-6">{selectedService.description}</p>

            {selectedService.steps && (
              <div className="mb-6">
                <h3 className="text-lg font-semibold text-primary mb-3">Pasos a seguir:</h3>
                <div 
                  className="text-neutral-600"
                  dangerouslySetInnerHTML={{ __html: selectedService.steps }}
                />
              </div>
            )}

            {selectedService.imageUrl && (
              <div className="mt-6">
                <img
                  src={selectedService.imageUrl}
                  alt={selectedService.imageAlt || selectedService.title}
                  className="w-full h-auto rounded-lg shadow-md"
                />
              </div>
            )}

            {selectedService.pdfUrl && (
              <div className="mt-8 flex justify-center">
                <div
                  onClick={() => window.open(selectedService.pdfUrl!, '_blank')}
                  onMouseEnter={handleMouseEnter}
                  onMouseLeave={handleMouseLeave}
                  className="relative w-full max-w-2xl aspect-[4/3] cursor-pointer transition-all duration-300 group"
                >
                  {/* Paper effect */}
                  <div className="
                    absolute -inset-2 -skew-y-1
                    bg-gradient-to-br from-gray-100 to-gray-200
                    rounded-lg shadow-lg
                    transition-all duration-300
                    group-hover:shadow-xl group-hover:-skew-y-2
                    -z-10
                  "/>
                  <div className="
                    absolute -inset-1 skew-y-1
                    bg-gradient-to-br from-gray-50 to-gray-100
                    rounded-lg shadow-md
                    transition-all duration-300
                    group-hover:shadow-lg group-hover:skew-y-2
                    -z-[5]
                  "/>

                  {/* Main content */}
                  <div className="
                    bg-white
                    rounded-lg
                    p-4
                    shadow-sm
                    transition-all duration-300
                    group-hover:shadow-md
                    border border-gray-200
                    relative
                    h-full
                    overflow-hidden
                  ">
                    {/* Efecto de brillo */}
                    <motion.div
                      initial={{ x: '-100%' }}
                      animate={{ x: '200%' }}
                      transition={{
                        duration: 2,
                        repeat: Infinity,
                        repeatDelay: 3
                      }}
                      className="absolute inset-0 opacity-0 group-hover:opacity-100"
                    >
                      <div className="w-1/3 h-full bg-gradient-to-r from-transparent via-white/30 to-transparent transform -skew-x-12" />
                    </motion.div>

                    <div className="relative w-full h-full bg-gradient-to-br from-gray-50 to-white rounded-xl shadow-lg overflow-hidden">
                      {!showPreview ? (
                        <div className="w-full h-full flex items-center justify-center relative">
                          <FaFilePdf className="w-16 h-16 text-primary/30" />
                          <motion.div
                            initial={{ opacity: 0, y: 20 }}
                            animate={{
                              opacity: [0, 1, 1, 0],
                              y: [20, 0, 0, -20],
                              scale: [0.9, 1, 1, 0.9],
                            }}
                            transition={{
                              duration: 2,
                              repeat: Infinity,
                              repeatDelay: 1
                            }}
                            className="absolute bottom-8 right-8 text-primary/60"
                          >
                            <svg
                              className="w-8 h-8 transform -rotate-12"
                              fill="none"
                              viewBox="0 0 24 24"
                              stroke="currentColor"
                            >
                              <path
                                strokeLinecap="round"
                                strokeLinejoin="round"
                                strokeWidth={1.5}
                                d="M15.042 21.672L13.684 16.6m0 0l-2.51 2.225.569-9.47 5.227 7.917-3.286-.672zM12 2.25V4.5m5.834.166l-1.591 1.591M20.25 10.5H18M7.757 14.743l-1.59 1.59M6 10.5H3.75m4.007-4.243l-1.59-1.59"
                              />
                            </svg>
                          </motion.div>
                        </div>
                      ) : (
                        <motion.div
                          initial={{ opacity: 0 }}
                          animate={{ opacity: 1 }}
                          className="w-full h-full"
                        >
                          <PDFPreview
                            url={selectedService.pdfUrl!}
                            height="100%"
                            openButtonPosition="center"
                            showOpenButton={true}
                            customStyles={{
                              borderRadius: '0.75rem',
                            }}
                          />
                        </motion.div>
                      )}
                    </div>
                  </div>
                </div>
              </div>
            )}
          </div>
        </div>
      </motion.div>
    );
  };

  return (
    <div className="min-h-screen bg-gradient-to-b from-white to-blue-50/30">
      {/* Hero Banner */}
      <motion.div
        className={`relative -mt-[4.5rem] rounded-b-3xl`}
        style={{ backgroundColor: "#FBE3D2" }}
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ duration: 0.8 }}
      >
        <motion.div
          initial={{ opacity: 0, scale: 0.8 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ duration: 0.8 }}
          className="absolute inset-0 bg-gradient-to-b from-blue-50 to-blue-100/50"
        />
        <div className="container mx-auto px-4 sm:px-6 py-4 sm:py-6 h-full flex flex-col justify-center items-center text-center relative z-10">
          <div className="flex flex-col sm:flex-row items-center justify-between w-full max-w-6xl">
            <div className="flex-1 text-center sm:text-left mb-4 sm:mb-0">
              <motion.h1
                initial={{ opacity: 0, y: -20 }}
                animate={{ opacity: 1, y: 0 }}
                className="text-xl sm:text-2xl font-bold text-gray-900 mb-1 sm:mb-2"
              >
                {servicesData.title}
              </motion.h1>
              <motion.p
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                transition={{ delay: 0.2 }}
                className="text-sm sm:text-base text-gray-600"
              >
                {servicesData.subtitle}
              </motion.p>
            </div>
          </div>
        </div>
      </motion.div>

      <motion.div
        initial="hidden"
        animate="visible"
        variants={sectionVariants}
        className="container mx-auto px-4 sm:px-6"
      >
        {/* Search Bar */}
        <div className="relative -mt-4 mb-6 sm:mb-8">
          <div className="max-w-2xl mx-auto">
            <div className="relative">
              <FaSearch className="absolute left-4 top-1/2 transform -translate-y-1/2 text-gray-400" />
              <input
                type="text"
                placeholder={servicesData.searchPlaceholder}
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
                className="w-full pl-12 pr-4 py-2.5 sm:py-3 rounded-lg border border-gray-200 focus:border-blue-500 focus:ring-2 focus:ring-blue-200 transition-all text-sm shadow-lg"
              />
            </div>
          </div>
        </div>

        {/* Main Content */}
        <div className="bg-white rounded-2xl shadow-xl overflow-hidden">
          <div className="flex flex-col lg:flex-row">
            {/* Sidebar */}
            <div className="lg:w-1/4 bg-gradient-to-br from-blue-50 to-blue-100/50">
              <div className="sticky top-0 p-4 sm:p-6 max-h-[calc(100vh-4rem)] overflow-y-auto">
                <h2 className="text-lg sm:text-xl lg:text-2xl font-bold text-primary border-b border-blue-200 pb-2 mb-4">
                  Servicios
                </h2>
                <div className="lg:hidden mb-4">
                  <button
                    onClick={() => setIsMenuOpen(!isMenuOpen)}
                    className="flex items-center justify-between w-full bg-white/80 backdrop-blur-sm p-3 rounded-lg text-primary font-semibold shadow-sm hover:bg-white transition-all"
                  >
                    <span>Seleccionar Servicio</span>
                    {isMenuOpen ? <HiChevronDown size={20} /> : <HiChevronRight size={20} />}
                  </button>
                </div>
                <AnimatePresence>
                  {(isMenuOpen || !isMenuOpen) && (
                    <motion.ul
                      initial={{ opacity: 0, height: 0 }}
                      animate={{ opacity: 1, height: 'auto' }}
                      exit={{ opacity: 0, height: 0 }}
                      transition={{ duration: 0.2 }}
                      className={`space-y-2 ${isMenuOpen ? 'block' : 'hidden lg:block'}`}
                    >
                      <motion.li
                        whileHover={{ scale: 1.02 }}
                        whileTap={{ scale: 0.98 }}
                        className={`text-sm lg:text-base cursor-pointer transition-all duration-200 ease-in-out p-3 rounded-lg
                          ${!selectedService
                            ? 'bg-primary text-white font-semibold shadow-md'
                            : 'text-neutral-600 hover:bg-white/80 hover:shadow-sm'}`}
                        onClick={() => {
                          setSelectedService(null);
                          setIsMenuOpen(false);
                        }}
                      >
                        Inicio
                      </motion.li>
                      {filteredServices.map((item, index) => (
                        <motion.li
                          key={index}
                          whileHover={{ scale: 1.02 }}
                          whileTap={{ scale: 0.98 }}
                          className={`text-sm lg:text-base cursor-pointer transition-all duration-200 ease-in-out p-3 rounded-lg
                            ${selectedService?.title === item
                              ? 'bg-primary text-white font-semibold shadow-md'
                              : 'text-neutral-600 hover:bg-white/80 hover:shadow-sm'}`}
                          onClick={() => {
                            setSelectedService(servicesData.itemDetails[index]);
                            setIsMenuOpen(false);
                          }}
                        >
                          {item}
                        </motion.li>
                      ))}
                    </motion.ul>
                  )}
                </AnimatePresence>
              </div>
            </div>

            {/* Main Content Area */}
            <div className="lg:w-3/4 min-h-[calc(100vh-16rem)] lg:min-h-[calc(100vh-4rem)] overflow-y-auto">
              <AnimatePresence mode="wait">
                {renderServiceContent()}
              </AnimatePresence>
            </div>
          </div>
        </div>
      </motion.div>
    </div>
  );
};

export default Services;