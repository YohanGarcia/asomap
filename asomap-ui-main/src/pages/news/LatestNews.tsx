import React, { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { useNavigate } from 'react-router-dom';
import { newsData } from '@/mocks';
import { newsService } from '@/api';
import type { INewsData } from '@/interfaces';
import 'swiper/css';
import 'swiper/css/pagination';
import 'swiper/css/autoplay';
import { Pagination, DynamicNewsBanner } from '@/components';

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

const gridVariants = {
  hidden: { opacity: 0 },
  visible: {
    opacity: 1,
    transition: {
      staggerChildren: 0.1,
      duration: 0.3,
    },
  },
};

const itemVariants = {
  hidden: { opacity: 0, y: 20 },
  visible: {
    opacity: 1,
    y: 0,
    transition: {
      duration: 0.5,
    },
  },
  exit: {
    opacity: 0,
    y: -20,
    transition: {
      duration: 0.3,
    },
  },
};

const ITEMS_PER_PAGE = 6;

const LatestNews: React.FC = () => {
  const navigate = useNavigate();
  const [currentPage, setCurrentPage] = useState(1);
  const [isChanging, setIsChanging] = useState(false);
  const [newsDataState, setNewsDataState] = useState<INewsData | null>(null);
  const [loading, setLoading] = useState(true);

  const handleNewsClick = (id: number) => {
    navigate(`/novedades/ultimas-noticias/${id}`);
  };

  useEffect(() => {
    const fetchNewsData = async () => {
      try {
        setLoading(true);
        const data = await newsService.getNews();
        setNewsDataState(data);
      } catch (error) {
        console.error('Error fetching news data:', error);
        setNewsDataState(newsData); // Fallback a mock data
      } finally {
        setLoading(false);
      }
    };

    fetchNewsData();
  }, []);

  if (loading || !newsDataState) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-gray-50">
        <div className="text-center">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-primary mx-auto mb-4"></div>
          <p className="text-gray-600">Cargando noticias...</p>
        </div>
      </div>
    );
  }

  // Calculate pagination
  const totalPages = Math.ceil(newsDataState.slides.length / ITEMS_PER_PAGE);
  const startIndex = (currentPage - 1) * ITEMS_PER_PAGE;
  const endIndex = startIndex + ITEMS_PER_PAGE;
  const currentNews = newsDataState.slides.slice(startIndex, endIndex);

  const handlePageChange = async (page: number) => {
    setIsChanging(true);
    await new Promise(resolve => setTimeout(resolve, 300)); // Wait for exit animations
    setCurrentPage(page);
    setIsChanging(false);
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  return (
    <motion.div
      initial="hidden"
      animate="visible"
      variants={sectionVariants}
      className="font-sans"
    >
      {/* Dynamic Banner Section */}
      <DynamicNewsBanner 
        news={newsDataState.slides} 
        autoSlideInterval={4000} // 4 segundos
      />

      {/* News Grid */}
      <div className="container mx-auto px-4 py-12">
        <AnimatePresence mode="wait">
          <motion.div
            key={currentPage}
            variants={gridVariants}
            initial="hidden"
            animate={isChanging ? "hidden" : "visible"}
            exit="hidden"
            className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8"
          >
            {currentNews.map((newsItem: any) => (
              <motion.div
                key={newsItem.id}
                variants={itemVariants}
                onClick={() => handleNewsClick(newsItem.id)}
                className="bg-white rounded-[20px] sm:rounded-[30px] lg:rounded-[50px] shadow-md hover:shadow-lg transition-all cursor-pointer group"
                layout
              >
                <div className="relative overflow-hidden rounded-[20px] sm:rounded-[30px] lg:rounded-[50px]">
                  <img
                    src={newsItem.image}
                    alt={String(newsItem.title)}
                    className="w-full h-48 object-cover transform group-hover:scale-105 transition-transform duration-300"
                  />
                  {newsItem.category && (
                    <span className="absolute top-4 right-4 bg-primary text-white px-3 py-1 rounded-full text-sm">
                      {newsItem.category}
                    </span>
                  )}
                </div>
                <div className="p-6">
                  <h3 className="text-xl font-semibold text-gray-900 mb-2 group-hover:text-primary transition-colors">
                    {newsItem.title}
                  </h3>
                  <p className="text-gray-600 mb-4">{newsItem.description}</p>
                  <div className="flex justify-between items-center text-sm text-gray-500">
                    <span>{newsItem.date}</span>
                    {newsItem.author && (
                      <span className="text-primary">
                        Por: {newsItem.author}
                      </span>
                    )}
                  </div>
                </div>
              </motion.div>
            ))}
          </motion.div>
        </AnimatePresence>

        {/* Pagination */}
        <div className="mt-12">
          <Pagination
            currentPage={currentPage}
            totalPages={totalPages}
            onPageChange={handlePageChange}
          />
        </div>
      </div>
    </motion.div>
  );
};

export default LatestNews;
