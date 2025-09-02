import React, { useEffect } from 'react';
import { motion } from 'framer-motion';
import {
  debitCardFeatures,
  debitCardBenefits,
  debitCardRequirements,
  debitCardData
} from '@/mocks';

const DebitCard: React.FC = () => {
  const { bannerImage, cardImage, title, description } = debitCardData;

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
            src={bannerImage}
            alt="Debit Card Banner"
            className="w-full h-full object-cover rounded-b-[30px] sm:rounded-b-[50px] lg:rounded-b-[80px]"
          />
          <div className="absolute inset-0 bg-gradient-to-t from-black/50 to-transparent rounded-b-[30px] sm:rounded-b-[50px] lg:rounded-b-[80px]" />
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
        <div className="bg-gray-50 py-16 sm:py-24 my-4">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div className="text-center mb-12">
              <h2 className="text-3xl font-bold text-primary sm:text-4xl">Beneficios</h2>
            </div>

            <div className="grid grid-cols-1 gap-8 sm:grid-cols-2 lg:grid-cols-3">
              {debitCardFeatures.map((benefit, index) => (
                <div key={index} className="flex justify-center">
                  <div className="w-full max-w-[420px] bg-indigo-200 rounded-xl shadow-lg flex flex-col items-center p-6">
                    <div className="mb-4">
                      <span className="inline-flex items-center justify-center p-6 bg-indigo-100 rounded-md shadow-lg">
                        <benefit.icon className="h-10 w-10 text-neutral-100" />
                      </span>
                    </div>
                    <h3 className="text-lg font-medium text-center text-neutral-100 mt-2">
                      {benefit.title}
                    </h3>
                    <h4 className="text-sm font-medium text-center text-neutral-100 mt-2">
                      {benefit.description}
                    </h4>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>

        {/* Benefits and Requirements Section */}
        <div className="bg-white py-16 sm:py-24">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div className="lg:flex lg:items-center lg:justify-between">
              <div className="lg:w-1/2 pr-0 lg:pr-8 mb-8 lg:mb-0">
                {/* Benefits Section */}
                <h2 className="text-3xl font-bold text-primary mb-6">Beneficios</h2>
                <ul className="space-y-4">
                  {debitCardBenefits.map((benefit, index) => (
                    <li key={index} className="flex items-start">
                      <span className="text-primary mr-2">•</span>
                      <p className="text-base text-neutral-100">{benefit}</p>
                    </li>
                  ))}
                </ul>

                {/* Requirements Section */}
                <h2 className="text-3xl font-bold text-primary mt-12 mb-6">Requisitos</h2>
                <ul className="space-y-4">
                  {debitCardRequirements.map((req, index) => (
                    <li key={index} className="flex items-start">
                      <span className="text-primary mr-2">•</span>
                      <p className="text-base text-neutral-100">{req}</p>
                    </li>
                  ))}
                </ul>
              </div>

              {/* Card Image */}
              <div className="lg:w-1/2 flex justify-center lg:justify-end">
                <img
                  className="w-full max-w-[300px] sm:max-w-[400px] md:max-w-[500px] lg:max-w-[570px] h-auto object-contain rounded-lg shadow-xl"
                  src={cardImage}
                  alt="Debit Card"
                />
              </div>
            </div>
          </div>
        </div>
      </div>
    </motion.div>
  );
};

export default DebitCard;