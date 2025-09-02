import React, { CSSProperties, useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';

interface PDFPreviewProps {
  url: string;
  className?: string;
  height?: string;
  showOpenButton?: boolean;
  openButtonPosition?: 'top-right' | 'bottom-right' | 'center';
  customStyles?: CSSProperties;
}

export const PDFPreview: React.FC<PDFPreviewProps> = ({ 
  url, 
  className = '',
  height = '400px',
  showOpenButton = true,
  openButtonPosition = 'top-right',
  customStyles = {}
}) => {
  const [isLoading, setIsLoading] = useState(true);
  const [isHovered, setIsHovered] = useState(false);
  const [hasLoaded, setHasLoaded] = useState(false);
  const [isLoadingPreview, setIsLoadingPreview] = useState(false);

  const styles: { [key: string]: CSSProperties } = {
    container: {
      height,
      ...customStyles
    },
    customScrollbar: {
      '&::-webkit-scrollbar': {
        width: '4px',
        height: '4px',
      } as CSSProperties,
      '&::-webkit-scrollbar-track': {
        background: 'transparent',
      } as CSSProperties,
      '&::-webkit-scrollbar-thumb': {
        background: `rgba(43, 75, 169, 0.1)`,
        borderRadius: '2px',
      } as CSSProperties,
      '&::-webkit-scrollbar-thumb:hover': {
        background: `rgba(43, 75, 169, 0.2)`,
      } as CSSProperties,
    } as CSSProperties,
  };

  const getOpenButtonPosition = (): CSSProperties => {
    switch (openButtonPosition) {
      case 'bottom-right':
        return { bottom: '8px', right: '8px' };
      case 'center':
        return { 
          top: '50%', 
          left: '50%', 
          transform: 'translate(-50%, -50%)' 
        };
      default:
        return { top: '8px', right: '8px' };
    }
  };

  const handleIframeLoad = () => {
    setIsLoading(false);
    setHasLoaded(true);
    setIsLoadingPreview(false);
  };

  const handleMouseEnter = () => {
    setIsHovered(true);
    if (!hasLoaded) {
      setIsLoadingPreview(true);
    }
  };

  const handleMouseLeave = () => {
    setIsHovered(false);
  };

  return (
    <div 
      className={`relative w-full bg-white rounded-xl overflow-hidden shadow-sm hover:shadow-md transition-shadow duration-300 ${className}`}
      style={styles.container}
      onMouseEnter={handleMouseEnter}
      onMouseLeave={handleMouseLeave}
    >
      <AnimatePresence>
        {(!hasLoaded || isLoading) && (
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            className="absolute inset-0 flex items-center justify-center bg-gradient-to-br from-gray-50/80 to-white/90 backdrop-blur-[2px] z-20"
          >
            <div className="w-full max-w-[80%] space-y-2 sm:space-y-3">
              <div className="h-1.5 sm:h-2 bg-gray-200 rounded-full animate-pulse"></div>
              <div className="h-1.5 sm:h-2 bg-gray-200 rounded-full animate-pulse"></div>
              <div className="h-1.5 sm:h-2 bg-gray-200 rounded-full animate-pulse w-3/4"></div>
              <div className="h-1.5 sm:h-2 bg-gray-200 rounded-full animate-pulse w-1/2"></div>
            </div>
          </motion.div>
        )}

        {isLoadingPreview && !hasLoaded && (
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            className="absolute inset-0 flex flex-col items-center justify-center bg-gradient-to-br from-gray-50/95 to-white/95 backdrop-blur-[2px] z-30"
          >
            <div className="relative w-8 h-8 sm:w-10 sm:h-10">
              <div className="absolute w-full h-full border-2 sm:border-3 border-[#2B4BA9]/20 rounded-full"></div>
              <div className="absolute w-full h-full border-2 sm:border-3 border-[#2B4BA9] rounded-full animate-spin border-t-transparent"></div>
            </div>
            <p className="mt-3 text-xs sm:text-sm text-gray-500 font-medium">
              Cargando PDF...
            </p>
          </motion.div>
        )}
      </AnimatePresence>

      {showOpenButton && (
        <motion.button
          initial={{ opacity: 0, scale: 0.9 }}
          animate={{ 
            opacity: isHovered ? 1 : 0,
            scale: isHovered ? 1 : 0.9,
          }}
          transition={{ duration: 0.2 }}
          onClick={() => window.open(url, '_blank')}
          className="absolute p-1.5 sm:p-2.5 bg-white hover:bg-[#2B4BA9] text-[#2B4BA9] hover:text-white rounded-lg shadow-lg backdrop-blur-[2px] z-10 transition-all duration-300"
          style={getOpenButtonPosition()}
          title="Abrir en nueva pestaña"
        >
          <svg 
            className="w-3 h-3 sm:w-4 sm:h-4" 
            fill="none" 
            viewBox="0 0 24 24" 
            stroke="currentColor"
          >
            <path 
              strokeLinecap="round" 
              strokeLinejoin="round" 
              strokeWidth={2} 
              d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" 
            />
          </svg>
        </motion.button>
      )}

      <div 
        className="w-full h-full overflow-auto bg-gradient-to-br from-gray-50/30 to-white/30"
        style={styles.customScrollbar}
      >
        {(isHovered || hasLoaded) && (
          <iframe
            src={`https://docs.google.com/gview?url=${encodeURIComponent(url)}&embedded=true`}
            className="w-full h-full"
            style={{ border: 'none', background: 'transparent' }}
            onLoad={handleIframeLoad}
            title="Vista previa del PDF"
          />
        )}
        {!isHovered && !hasLoaded && (
          <div className="w-full h-full flex items-center justify-center text-gray-400">
            <svg 
              className="w-8 h-8 sm:w-12 sm:h-12 opacity-50" 
              fill="none" 
              viewBox="0 0 24 24" 
              stroke="currentColor"
            >
              <path 
                strokeLinecap="round" 
                strokeLinejoin="round" 
                strokeWidth={1.5} 
                d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" 
              />
            </svg>
          </div>
        )}
      </div>
    </div>
  );
};
