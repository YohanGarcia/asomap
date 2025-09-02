import React, { useEffect, useState } from 'react';
import { motion } from 'framer-motion';
import { useParams, useNavigate } from 'react-router-dom';
import { loansService } from '@/api';
import type { ILoanData } from '@/interfaces';

const LoanDetail: React.FC = () => {
  const { slug } = useParams<{ slug: string }>();
  const [loanData, setLoanData] = useState<ILoanData | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const navigate = useNavigate();

  useEffect(() => {
    const fetchLoanData = async () => {
      try {
        setLoading(true);
        setError(null);
        
        if (slug) {
          const loan = await loansService.getLoanBySlug(slug);
          if (loan) {
            setLoanData(loan);
          } else {
            setError('Préstamo no encontrado');
          }
        }
      } catch (err) {
        console.error('Error fetching loan data:', err);
        setError('Error al cargar los datos del préstamo');
      } finally {
        setLoading(false);
      }
    };

    if (slug) {
      fetchLoanData();
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
          <p className="text-gray-600">Cargando préstamo...</p>
        </div>
      </div>
    );
  }

  if (error || !loanData) {
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

  const { title, description, details, requirementsTitle, requirements, loanType, bannerImage } = loanData;

  // Función para obtener el color según el tipo de préstamo
  const getLoanTypeColor = (type: string) => {
    switch (type) {
      case 'consumer':
        return 'bg-blue-100 text-blue-800';
      case 'commercial':
        return 'bg-green-100 text-green-800';
      case 'home_purchase':
      case 'construction':
      case 'remodelation':
      case 'land_purchase':
        return 'bg-purple-100 text-purple-800';
      default:
        return 'bg-gray-100 text-gray-800';
    }
  };

  // Función para obtener el nombre legible del tipo de préstamo
  const getLoanTypeName = (type: string) => {
    switch (type) {
      case 'consumer':
        return 'Consumo';
      case 'commercial':
        return 'Comercial';
      case 'home_purchase':
        return 'Compra de Vivienda';
      case 'construction':
        return 'Construcción';
      case 'remodelation':
        return 'Ampliación/Remodelación';
      case 'land_purchase':
        return 'Compra de Terreno';
      default:
        return type;
    }
  };

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
          <div className="absolute inset-0 bg-black/40"></div>
          <div className="absolute inset-0 flex items-center justify-center">
            <div className="text-center text-white px-4">
              <span className={`inline-block px-3 py-1 rounded-full text-sm font-medium mb-4 ${getLoanTypeColor(loanType)}`}>
                {getLoanTypeName(loanType)}
              </span>
              <h1 className="text-4xl sm:text-5xl font-bold mb-4">{title}</h1>
              <p className="text-xl sm:text-2xl opacity-90 max-w-3xl mx-auto">{description}</p>
            </div>
          </div>
        </div>

        {/* Details Section */}
        <div className="bg-white py-16 sm:py-24">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div className="text-center mb-12">
              <h2 className="text-3xl font-bold text-primary sm:text-4xl mb-4">Características del Préstamo</h2>
              <p className="text-lg text-gray-600">Conoce todos los beneficios y detalles de este producto financiero</p>
            </div>

            <div className="grid grid-cols-1 gap-8 sm:grid-cols-2 lg:grid-cols-3">
              {details.map((detail, index) => (
                <div key={index} className="bg-gray-50 rounded-lg p-6 hover:shadow-lg transition-shadow">
                  <div className="flex items-start">
                    <div className="flex-shrink-0">
                      <div className="w-8 h-8 bg-primary rounded-full flex items-center justify-center">
                        <span className="text-white font-bold text-sm">{index + 1}</span>
                      </div>
                    </div>
                    <div className="ml-4">
                      <p className="text-gray-700 leading-relaxed">{detail}</p>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>

        {/* Requirements Section */}
        <div className="bg-gray-50 py-16 sm:py-24">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div className="text-center mb-12">
              <h2 className="text-3xl font-bold text-primary sm:text-4xl mb-4">{requirementsTitle}</h2>
              <p className="text-lg text-gray-600">Asegúrate de cumplir con todos los requisitos necesarios</p>
            </div>

            <div className="max-w-4xl mx-auto">
              <div className="bg-white rounded-lg shadow-lg p-8">
                <ul className="space-y-4">
                  {requirements.map((requirement, index) => (
                    <li key={index} className="flex items-start">
                      <div className="flex-shrink-0 w-6 h-6 bg-primary rounded-full flex items-center justify-center mr-4 mt-1">
                        <svg className="w-4 h-4 text-white" fill="currentColor" viewBox="0 0 20 20">
                          <path fillRule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clipRule="evenodd" />
                        </svg>
                      </div>
                      <p className="text-lg text-gray-700">{requirement}</p>
                    </li>
                  ))}
                </ul>
              </div>
            </div>
          </div>
        </div>

        {/* CTA Section */}
        <div className="bg-primary py-16 sm:py-24">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
            <h2 className="text-3xl font-bold text-white sm:text-4xl mb-4">
              ¿Listo para solicitar tu préstamo?
            </h2>
            <p className="text-xl text-blue-100 mb-8 max-w-3xl mx-auto">
              Nuestro equipo está listo para ayudarte a hacer realidad tus proyectos financieros
            </p>
            <div className="flex flex-col sm:flex-row gap-4 justify-center">
              <button className="bg-white text-primary px-8 py-3 rounded-lg font-semibold hover:bg-gray-100 transition-colors">
                Solicitar Préstamo
              </button>
              <button 
                onClick={() => navigate('/productos')}
                className="border-2 border-white text-white px-8 py-3 rounded-lg font-semibold hover:bg-white hover:text-primary transition-colors"
              >
                Ver Otros Productos
              </button>
            </div>
          </div>
        </div>
      </div>
    </motion.div>
  );
};

export default LoanDetail;
