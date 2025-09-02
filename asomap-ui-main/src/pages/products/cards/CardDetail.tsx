import React, { useEffect, useState } from 'react';
import { motion } from 'framer-motion';
import { useParams, useNavigate } from 'react-router-dom';
import { cardsService } from '@/api';
import { getIconComponent } from '@/utils/iconMapper';
import type { ICardData } from '@/interfaces';

const CardDetail: React.FC = () => {
  const { slug } = useParams<{ slug: string }>();
  const [cardData, setCardData] = useState<ICardData | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const navigate = useNavigate();

  useEffect(() => {
    const fetchCardData = async () => {
      try {
        setLoading(true);
        setError(null);
        
        if (slug) {
          const card = await cardsService.getCardBySlug(slug);
          if (card) {
            setCardData(card);
          } else {
            setError('Tarjeta no encontrada');
          }
        }
      } catch (err) {
        console.error('Error fetching card data:', err);
        setError('Error al cargar los datos de la tarjeta');
      } finally {
        setLoading(false);
      }
    };

    if (slug) {
      fetchCardData();
    }
  }, [slug]);

  useEffect(() => {
    window.scrollTo(0, 0);
  }, []);

  const sectionVariants = {
    hidden: { opacity: 0, y: 20 },
    visible: {
      opacity: 1,
      y: 0,
      transition: {
        duration: 0.6,
        ease: "easeOut"
      }
    }
  };

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-gray-50">
        <div className="text-center">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-primary mx-auto mb-4"></div>
          <p className="text-gray-600">Cargando tarjeta...</p>
        </div>
      </div>
    );
  }

  if (error || !cardData) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-gray-50">
        <div className="text-center">
          <div className="text-red-500 text-6xl mb-4">⚠️</div>
          <h2 className="text-xl font-semibold text-gray-800 mb-2">Error</h2>
          <p className="text-gray-600 mb-4">{error || 'No se pudieron cargar los datos'}</p>
          <button
            onClick={() => navigate('/productos')}
            className="bg-primary text-white px-4 py-2 rounded-lg hover:bg-primary/80 transition-colors"
          >
            Volver a Productos
          </button>
        </div>
      </div>
    );
  }

  const { bannerImage, cardImage, title, description, features, requirements, benefits } = cardData;

  return (
    <motion.div
      initial="hidden"
      animate="visible"
      variants={sectionVariants}
      className="relative -mt-[80px]"
    >
      <div className="font-sans bg-gradient-to-b from-white to-blue-50/30">
        {/* Hero Section */}
        <div className="relative h-[360px] sm:h-[400px] md:h-[450px] lg:h-[500px]">
          <img
            src={bannerImage}
            alt={`${title} Banner`}
            className="w-full h-full object-cover rounded-b-[20px] sm:rounded-b-[30px] lg:rounded-b-[50px]"
          />
        </div>

        {/* Description Section */}
        <div className="bg-white py-8 sm:py-12 md:py-16">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div className="text-center">
              <h1 className="text-3xl sm:text-4xl font-bold text-primary mb-4">{title}</h1>
              <p className="mt-3 text-sm sm:text-base text-gray-700">{description}</p>
            </div>
          </div>
        </div>

        {/* Benefits Section */}
        <div className="bg-gray-50 py-16 sm:py-24">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div className="text-center mb-12">
              <h2 className="text-3xl font-bold text-primary sm:text-4xl">Beneficios</h2>
            </div>

            <div className="grid grid-cols-1 gap-8 sm:grid-cols-2 lg:grid-cols-3">
              {benefits.map((benefit, index) => {
                const IconComponent = getIconComponent(benefit.icon);
                return (
                  <div key={index} className="flex justify-center">
                    <div className="w-full max-w-[420px] bg-indigo-200 rounded-xl shadow-lg flex flex-col items-center p-6">
                      <div className="mb-4">
                        <span className="inline-flex items-center justify-center p-6 bg-indigo-100 rounded-md shadow-lg">
                          <IconComponent className="h-10 w-10 text-neutral-100" />
                        </span>
                      </div>
                      <h3 className="text-lg font-medium text-center text-gray-800 mt-2">
                        {benefit.text}
                      </h3>
                    </div>
                  </div>
                );
              })}
            </div>
          </div>
        </div>

        {/* Características y Requisitos Section */}
        <div className="bg-white py-12 sm:py-16 md:py-24">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div className="lg:flex lg:items-start lg:justify-between">
              <div className="lg:w-1/2 pr-0 lg:pr-8 mb-8 lg:mb-0">
                {/* Sección de Requisitos */}
                <div className="mb-8 sm:mb-12">
                  <h2 className="text-2xl sm:text-3xl font-bold text-primary mb-4 sm:mb-6">Requisitos</h2>
                  <ul className="space-y-2 sm:space-y-4">
                    {requirements.map((req, index) => (
                      <li key={index} className="flex items-start">
                        <span className="text-blue-700 mr-2">•</span>
                        <p className="text-sm sm:text-base leading-6 text-gray-700">{req}</p>
                      </li>
                    ))}
                  </ul>
                </div>

                {/* Sección de Características */}
                <div>
                  <h2 className="text-2xl sm:text-3xl font-bold text-primary mb-4 sm:mb-6">Características</h2>
                  <ul className="space-y-2 sm:space-y-4">
                    {features.map((feature, index) => (
                      <li key={index} className="flex items-start">
                        <span className="text-blue-700 mr-2">•</span>
                        <p className="text-sm sm:text-base leading-6 text-gray-700">{feature}</p>
                      </li>
                    ))}
                  </ul>
                </div>
              </div>

              {/* Imagen a la derecha */}
              <div className="lg:w-1/2 flex justify-center lg:justify-end">
                <img
                  className="w-full max-w-[300px] sm:max-w-[400px] md:max-w-[500px] lg:max-w-[570px] h-auto object-contain"
                  src={cardImage}
                  alt={title}
                />
              </div>
            </div>
          </div>
        </div>
      </div>
    </motion.div>
  );
};

export default CardDetail;
