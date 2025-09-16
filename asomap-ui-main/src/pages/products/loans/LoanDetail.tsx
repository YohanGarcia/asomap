import React, { useEffect, useState } from 'react';
import { motion } from 'framer-motion';
import { useParams, useNavigate } from 'react-router-dom';
import { loansService } from '@/api';
import type { ILoanData } from '@/interfaces';
import BannerComponent from './BannerComponet';

const LoanDetail: React.FC = () => {
  const { slug } = useParams<{ slug: string }>();
  const [loanData, setLoanData] = useState<ILoanData | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const navigate = useNavigate();

  console.log(loanData, 'loanData');

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

  const { title, description, details, requirementsTitle, requirements, bannerImage } = loanData;

  // Función para obtener el color según el tipo de préstamo


  // Función para obtener el nombre legible del tipo de préstamo
  

  return (
    <motion.div
      initial="hidden"
      animate="visible"
      variants={sectionVariants}
      className="relative -mt-[80px]"
    >
      <div className="font-sans bg-white">
        {/* Hero Section */}
        <div className="relative h-[360px] sm:h-[400px] md:h-[450px] lg:h-[500px] -mt-[80px]">
          {bannerImage ? (
            <img
              src={bannerImage}
              alt={`${title} Banner`}
              className="w-full h-full object-cover rounded-b-[30px] sm:rounded-b-[50px] lg:rounded-b-[80px]"
            />
          ) : (
            <div className="w-full h-full bg-gradient-to-r from-orange-500 to-blue-600 rounded-b-[30px] sm:rounded-b-[50px] lg:rounded-b-[80px] flex items-center justify-center">
              <div className="text-white text-center">
                <h1 className="text-4xl font-bold mb-4">{title}</h1>
                <p className="text-xl opacity-90">Imagen no disponible</p>
              </div>
            </div>
          )}
          <div className=" absolute inset-0 bg-gradient-to-r from-orange-600/50  to-blue-600/60 rounded-b-[30px] sm:rounded-b-[50px] lg:rounded-b-[80px]">
              <div className="absolute bottom-6 right-6 w-[500px] h-[80px]">
                <div className="bg-blue-900/60 px-6 py-4 w-full h-full flex items-center justify-center">
                  <h1 className="text-2xl sm:text-3xl font-bold text-white">{title}</h1>
                </div>
            </div>
          </div>
        </div>
        <div className="container mx-auto px-4 py-8">
        {/* Details Section */}
        <div className="bg-white ">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div className="text-center mb-12">
              <h2 className="text-3xl font-bold text-primary sm:text-4xl mb-4">{title}</h2>
              <p className="text-lg text-gray-600">{description}</p>
            </div>


            <h2 className="text-2xl font-bold text-center text-primary mt-8">
            Beneficios
          </h2>


            <div className="grid grid-cols-1 gap-8 sm:grid-cols-2 lg:grid-cols-3 my-16">
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
                {/* Requirements Section */}
        
          </div>
        </div>

        <div className="bg-[#FFF5F0] rounded-lg p-8 flex items-center">
          <div className="w-1/3">
              {bannerImage ? (
                <img
                  src={bannerImage}
                  alt="Familia feliz"
                  className="rounded-full w-48 h-48 object-cover"
                />
              ) : (
                <div className="rounded-full w-48 h-48 bg-gradient-to-r from-orange-500 to-blue-600 flex items-center justify-center">
                  <span className="text-white text-2xl font-bold">📋</span>
                </div>
              )}
            </div>
            <div className="w-2/3">
              <h3 className="text-2xl font-bold text-primary mb-4">{requirementsTitle}</h3>
              <h4 className="text-md font-semibold text-primary mb-2">
                Asegúrate de cumplir con todos los requisitos necesarios
              </h4>
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

        <BannerComponent />
    

       
      </div>
      </div>
    </motion.div>
  );
};

export default LoanDetail;
