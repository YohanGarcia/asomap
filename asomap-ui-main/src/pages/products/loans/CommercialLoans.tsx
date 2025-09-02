import React, { useEffect } from 'react';
import { motion } from 'framer-motion';
import { commercialLoansData } from '@/mocks';

const CommercialLoans: React.FC = () => {
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

  useEffect(() => {
    window.scrollTo(0, 0);
  }, []);

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
          <img
            src={commercialLoansData.bannerData.imageUrl}
            alt="Commercial Loans Banner"
            className="w-full h-full object-cover rounded-b-[30px] sm:rounded-b-[50px] lg:rounded-b-[80px]"
          />
          <div className="absolute inset-0 bg-gradient-to-t from-black/50 to-transparent rounded-b-[30px] sm:rounded-b-[50px] lg:rounded-b-[80px]" />
        </div>

        <div className="container mx-auto px-4 py-8">
          <h1 className="text-3xl font-bold text-center text-primary mb-4">
            {commercialLoansData.bannerData.title}
          </h1>
          <p className="text-center text-lg mb-8">
            {commercialLoansData.subtitle}
          </p>

          <div className="flex justify-center space-x-4 mb-12">
            <button className="bg-primary-accent text-white px-6 py-2 rounded-full hover:bg-primary transition-colors">
              Solicitar
            </button>
            <button className="bg-primary text-white px-6 py-2 rounded-full hover:bg-primary-accent transition-colors">
              Tarifario
            </button>
          </div>

          <h2 className="text-2xl font-bold text-center text-primary mb-8">
            Beneficios
          </h2>

          <div className="container mx-auto px-4 sm:px-6 lg:px-8 my-16">
            <div className="grid grid-cols-1 md:grid-cols-2 gap-8 max-w-4xl mx-auto">
              {commercialLoansData.benefits.map((benefit, index) => (
                <div
                  key={index}
                  className="bg-white p-6 rounded-lg shadow-md flex flex-col items-center text-center h-[240px] justify-between"
                >
                  <img src={benefit.image} alt={benefit.title} className="w-25 h-20 object-contain mb-4" />
                  <div className="px-4">
                    <h3 className="font-semibold text-primary text-lg mb-3">{benefit.title}</h3>
                    <p className="text-sm text-neutral-100">{benefit.description}</p>
                  </div>
                </div>
              ))}
            </div>
          </div>

          <div className="bg-[#FFF5F0] rounded-lg p-8 flex items-center">
            <div className="w-1/3">
              <img
                src={commercialLoansData.requirements.image}
                alt="Familia feliz"
                className="rounded-full w-48 h-48 object-cover"
              />
            </div>
            <div className="w-2/3">
              <h3 className="text-2xl font-bold text-primary mb-4">Requisitos</h3>
              <h4 className="text-md font-semibold text-primary mb-2">
                {commercialLoansData.requirements.title}
              </h4>
              <ul className="list-disc list-inside text-neutral-100">
                {commercialLoansData.requirements.items.map((item, index) => (
                  <li key={index}>{item}</li>
                ))}
              </ul>
            </div>
          </div>
        </div>
      </div>
    </motion.div>
  );
};

export default CommercialLoans;