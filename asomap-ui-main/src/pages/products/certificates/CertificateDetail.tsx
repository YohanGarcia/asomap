import React, { useEffect, useState } from 'react';
import { motion } from 'framer-motion';
import { useParams, useNavigate } from 'react-router-dom';
import { certificatesService } from '@/api';
import type { ICertificateData } from '@/interfaces';

const CertificateDetail: React.FC = () => {
  const { slug } = useParams<{ slug: string }>();
  const [certificateData, setCertificateData] = useState<ICertificateData | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const navigate = useNavigate();

  useEffect(() => {
    const fetchCertificateData = async () => {
      try {
        setLoading(true);
        setError(null);
        
        if (slug) {
          const certificate = await certificatesService.getCertificateBySlug(slug);
          if (certificate) {
            setCertificateData(certificate);
          } else {
            setError('Certificado no encontrado');
          }
        }
      } catch (err) {
        console.error('Error fetching certificate data:', err);
        setError('Error al cargar los datos del certificado');
      } finally {
        setLoading(false);
      }
    };

    if (slug) {
      fetchCertificateData();
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
          <p className="text-gray-600">Cargando certificado...</p>
        </div>
      </div>
    );
  }

  if (error || !certificateData) {
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

  const { 
    bannerImage, 
    certificateImage, 
    title, 
    subtitle, 
    description, 
    benefits, 
    investment, 
    rates, 
    requirements, 
    depositRates, 
    faq 
  } = certificateData;

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
              <h2 className="text-xl sm:text-2xl text-gray-600 mb-4">{subtitle}</h2>
              <p className="mt-3 text-sm sm:text-base text-gray-700">{description}</p>
            </div>
          </div>
        </div>

        {/* Benefits Section */}
        <div className="bg-gray-50 py-16 sm:py-24">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div className="text-center mb-12">
              <h2 className="text-3xl font-bold text-primary sm:text-4xl">{benefits.title}</h2>
            </div>

            <div className="grid grid-cols-1 gap-8 sm:grid-cols-2 lg:grid-cols-4">
              {benefits.items.map((benefit, index) => (
                <div key={index} className="flex justify-center">
                  <div className="w-full max-w-[280px] bg-white rounded-xl shadow-lg flex flex-col items-center p-6">
                    <h3 className="text-lg font-medium text-center text-gray-800 mb-2">
                      {benefit.title}
                    </h3>
                    <p className="text-sm text-center text-gray-600">
                      {benefit.description}
                    </p>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>

        {/* Investment Section */}
        <div className="bg-white py-12 sm:py-16 md:py-24">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div className="lg:flex lg:items-start lg:justify-between">
              <div className="lg:w-1/2 pr-0 lg:pr-8 mb-8 lg:mb-0">
                <h2 className="text-2xl sm:text-3xl font-bold text-primary mb-4 sm:mb-6">{investment.title}</h2>
                <p className="text-gray-600 mb-6">{investment.subtitle}</p>
                <ul className="space-y-2 sm:space-y-4">
                  {investment.details.map((detail, index) => (
                    <li key={index} className="flex items-start">
                      <span className="text-blue-700 mr-2">•</span>
                      <p className="text-sm sm:text-base leading-6 text-gray-700">{detail}</p>
                    </li>
                  ))}
                </ul>
              </div>

              {/* Imagen a la derecha */}
              <div className="lg:w-1/2 flex justify-center lg:justify-end">
                <img
                  className="w-full max-w-[300px] sm:max-w-[400px] md:max-w-[500px] lg:max-w-[570px] h-auto object-contain"
                  src={certificateImage}
                  alt={title}
                />
              </div>
            </div>
          </div>
        </div>

        {/* Rates Section */}
        <div className="bg-gray-50 py-16 sm:py-24">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div className="text-center mb-12">
              <h2 className="text-3xl font-bold text-primary sm:text-4xl">{rates.title}</h2>
            </div>

            <div className="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3">
              {rates.items.map((rate, index) => (
                <div key={index} className="bg-white rounded-lg shadow-md p-6">
                  <h3 className="text-lg font-medium text-gray-800 mb-2">{rate.label}</h3>
                  <p className="text-2xl font-bold text-primary">{rate.value}</p>
                </div>
              ))}
            </div>
          </div>
        </div>

        {/* Requirements Section */}
        <div className="bg-white py-12 sm:py-16 md:py-24">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div className="text-center mb-12">
              <h2 className="text-3xl font-bold text-primary sm:text-4xl">{requirements.title}</h2>
            </div>

            <div className="max-w-4xl mx-auto">
              <ul className="space-y-4">
                {requirements.items.map((req, index) => (
                  <li key={index} className="flex items-start">
                    <span className="text-blue-700 mr-3 text-xl">•</span>
                    <p className="text-lg text-gray-700">{req}</p>
                  </li>
                ))}
              </ul>
            </div>
          </div>
        </div>

        {/* Deposit Rates Section */}
        <div className="bg-gray-50 py-16 sm:py-24">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div className="text-center mb-12">
              <h2 className="text-3xl font-bold text-primary sm:text-4xl">{depositRates.title}</h2>
              <p className="text-gray-600 mt-2">{depositRates.validFrom}</p>
            </div>

            <div className="overflow-x-auto">
              <table className="w-full bg-white rounded-lg shadow-lg">
                <thead className="bg-primary text-white">
                  <tr>
                    <th className="px-6 py-4 text-left">Rango</th>
                    <th className="px-6 py-4 text-center">Tasa</th>
                    <th className="px-6 py-4 text-center">Plazo</th>
                  </tr>
                </thead>
                <tbody>
                  {depositRates.items.map((item, index) => (
                    <tr key={index} className="border-b border-gray-200">
                      <td className="px-6 py-4 text-gray-800">{item.range}</td>
                      <td className="px-6 py-4 text-center font-bold text-primary">{item.rate}</td>
                      <td className="px-6 py-4 text-center text-gray-600">{item.term}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        </div>

        {/* FAQ Section */}
        <div className="bg-white py-12 sm:py-16 md:py-24">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div className="text-center mb-12">
              <h2 className="text-3xl font-bold text-primary sm:text-4xl">{faq.title}</h2>
            </div>

            <div className="max-w-4xl mx-auto space-y-6">
              {faq.items.map((item, index) => (
                <div key={index} className="bg-gray-50 rounded-lg p-6">
                  <h3 className="text-lg font-semibold text-gray-800 mb-3">{item.question}</h3>
                  <p className="text-gray-600">{item.answer}</p>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>
    </motion.div>
  );
};

export default CertificateDetail;
