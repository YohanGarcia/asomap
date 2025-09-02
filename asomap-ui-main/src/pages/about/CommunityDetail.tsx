import React, { useEffect, useState } from 'react';
import { motion } from 'framer-motion';
import { useParams, useNavigate } from 'react-router-dom';
import { communityService } from '@/api';
import type { CommunitySupportResponse } from '@/interfaces';
import { FaArrowLeft, FaCalendarAlt, FaMapMarkerAlt, FaUsers } from 'react-icons/fa';

const sectionVariants = {
  hidden: { opacity: 0, y: 20 },
  visible: {
    opacity: 1,
    y: 0,
    transition: {
      duration: 0.5,
    },
  },
};

const cardVariants = {
  hidden: { opacity: 0, scale: 0.95 },
  visible: {
    opacity: 1,
    scale: 1,
    transition: {
      duration: 0.3,
    },
  },
};

const RelatedInitiatives: React.FC<{ initiatives: CommunitySupportResponse['data']['initiatives'] }> = ({ initiatives }) => {
  const navigate = useNavigate();

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mt-8">
      {initiatives.map((initiative) => (
        <motion.div
          key={initiative.id}
          variants={cardVariants}
          whileHover={{ scale: 1.02 }}
          className="bg-white rounded-xl shadow-md overflow-hidden cursor-pointer hover:shadow-xl transition-all duration-300"
          onClick={() => navigate(`/nosotros/iniciativa/${initiative.id}`)}
        >
          <div className="relative h-48 overflow-hidden">
            <img
              src={initiative.imageUrl}
              alt={initiative.title}
              className="w-full h-full object-cover transition-transform duration-300 group-hover:scale-105"
            />
            <div className="absolute inset-0 bg-gradient-to-t from-black/30 to-transparent" />
          </div>
          <div className="p-6">
            <h3 className="text-lg font-bold text-[#2B4BA9] mb-2">{initiative.title}</h3>
            <p className="text-gray-600 text-sm line-clamp-2">{initiative.description}</p>
          </div>
        </motion.div>
      ))}
    </div>
  );
};

const CommunityDetail: React.FC = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const [data, setData] = useState<CommunitySupportResponse | null>(null);

  useEffect(() => {
    const fetchData = async () => {
      const response = await communityService.getCommunitySupport();
      setData(response);
    };
    fetchData();
  }, []);

  useEffect(() => {
    window.scrollTo(0, 0);
  }, []);

  if (!data) return null;

  const initiative = data.data.initiatives.find(
    (initiative) => initiative.id === id
  );

  const category = initiative
    ? data.data.categories.find(cat => cat.id === initiative.category)
    : null;

  if (!initiative) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          className="text-center"
        >
          <h1 className="text-2xl font-bold text-[#2B4BA9] mb-4">Iniciativa no encontrada</h1>
          <button
            onClick={() => navigate('/nosotros/apoyo-comunitario')}
            className="text-[#2B4BA9] hover:underline flex items-center gap-2 justify-center"
          >
            <FaArrowLeft /> Volver a Apoyo a la Comunidad
          </button>
        </motion.div>
      </div>
    );
  }

  // Get related initiatives from the same category
  const relatedInitiatives = data.data.initiatives
    .filter(item => item.id !== initiative.id && item.category === initiative.category)
    .slice(0, 3);

  return (
    <motion.div
      initial="hidden"
      animate="visible"
      variants={sectionVariants}
      className="min-h-screen bg-gray-50"
    >
      {/* Banner Section */}
      <div className="relative h-[300px] sm:h-[400px] md:h-[500px] -mt-[80px] rounded-b-[30px] sm:rounded-b-[50px] lg:rounded-b-[80px] overflow-hidden">
        <img
          src={initiative.imageUrl}
          alt={initiative.title}
          className="w-full h-full object-cover"
        />
        <div className="absolute inset-0 bg-gradient-to-t from-black/70 via-black/30 to-transparent rounded-b-[30px] sm:rounded-b-[50px] lg:rounded-b-[80px]" />
        <div className="absolute bottom-0 left-0 right-0 container mx-auto px-4 sm:px-6 pb-6 sm:pb-8 md:pb-12">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.2 }}
          >
            <button
              onClick={() => navigate('/nosotros/apoyo-comunitario')}
              className="text-white hover:text-[#2B4BA9] bg-white/10 hover:bg-white backdrop-blur-sm px-4 py-2 rounded-full flex items-center gap-2 mb-4 sm:mb-6 transition-all duration-300 text-sm sm:text-base"
            >
              <FaArrowLeft /> Volver a Apoyo a la Comunidad
            </button>
            <div className="flex items-center gap-4 mb-3 sm:mb-4">
              {category && (
                <span className="bg-[#2B4BA9] px-4 sm:px-6 py-1.5 sm:py-2 rounded-full text-sm sm:text-base font-medium text-white">
                  {category.name}
                </span>
              )}
            </div>
            <h1 className="text-3xl sm:text-4xl md:text-5xl font-bold text-white">{initiative.title}</h1>
          </motion.div>
        </div>
      </div>

      <div className="container mx-auto px-4 sm:px-6 py-8 sm:py-12 md:py-16">
        <motion.div
          variants={cardVariants}
          className="bg-white rounded-2xl shadow-xl overflow-hidden max-w-5xl mx-auto"
        >
          <div className="p-6 sm:p-8 md:p-12">
            <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6 sm:gap-8 mb-8 sm:mb-12">
              <div className="flex items-center gap-4">
                <div className="bg-[#2B4BA9]/10 p-3 rounded-full">
                  <FaCalendarAlt className="text-lg sm:text-xl text-[#2B4BA9]" />
                </div>
                <div>
                  <p className="text-sm text-gray-500">Fecha</p>
                  <p className="font-medium text-sm sm:text-base">2025</p>
                </div>
              </div>
              <div className="flex items-center gap-4">
                <div className="bg-[#2B4BA9]/10 p-3 rounded-full">
                  <FaMapMarkerAlt className="text-lg sm:text-xl text-[#2B4BA9]" />
                </div>
                <div>
                  <p className="text-sm text-gray-500">Ubicación</p>
                  <p className="font-medium text-sm sm:text-base">Santo Domingo</p>
                </div>
              </div>
              <div className="flex items-center gap-4">
                <div className="bg-[#2B4BA9]/10 p-3 rounded-full">
                  <FaUsers className="text-lg sm:text-xl text-[#2B4BA9]" />
                </div>
                <div>
                  <p className="text-sm text-gray-500">Beneficiarios</p>
                  <p className="font-medium text-sm sm:text-base">Comunidad Local</p>
                </div>
              </div>
            </div>

            <div className="space-y-6 sm:space-y-8">
              <div>
                <h2 className="text-xl sm:text-2xl font-bold text-[#2B4BA9] mb-3 sm:mb-4">Descripción</h2>
                <p className="text-gray-600 leading-relaxed text-base sm:text-lg">{initiative.description}</p>
              </div>

              <div>
                <h2 className="text-xl sm:text-2xl font-bold text-[#2B4BA9] mb-3 sm:mb-4">Impacto</h2>
                <div className="bg-[#2B4BA9]/5 p-4 sm:p-6 rounded-xl">
                  <p className="text-[#2B4BA9] leading-relaxed text-base sm:text-lg">{initiative.impact}</p>
                </div>
              </div>
            </div>

            {relatedInitiatives.length > 0 && (
              <motion.div
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: 0.4 }}
                className="mt-12 sm:mt-16"
              >
                <h2 className="text-xl sm:text-2xl font-bold text-[#2B4BA9] mb-6 sm:mb-8">Iniciativas Relacionadas</h2>
                <RelatedInitiatives initiatives={relatedInitiatives} />
              </motion.div>
            )}
          </div>
        </motion.div>
      </div>
    </motion.div>
  );
};

export default CommunityDetail;
