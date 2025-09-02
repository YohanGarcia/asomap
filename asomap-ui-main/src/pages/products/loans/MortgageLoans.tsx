import React, { useEffect } from 'react';
import { motion } from 'framer-motion';
import { mortgageLoansData } from '@/mocks';

const MortgageLoans: React.FC = () => {
  const {
    loansData: loanOptions,
    requirements,
  } = mortgageLoansData;

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
            src={mortgageLoansData.bannerData.imageUrl}
            alt="Mortgage Loans Banner"
            className="w-full h-full object-cover rounded-b-[30px] sm:rounded-b-[50px] lg:rounded-b-[80px]"
          />
          <div className="absolute inset-0 bg-gradient-to-t from-black/50 to-transparent rounded-b-[30px] sm:rounded-b-[50px] lg:rounded-b-[80px]" />
        </div>

        <div className="container mx-auto px-4 py-8">
          <h2 className="text-3xl font-bold text-center text-primary mb-4">Préstamos Hipotecario</h2>
          <p className="text-center text-neutral-100 text-lg mb-8">
            Financia la construcción, compra o ampliación de tu nueva casa
          </p>

          <div className="flex justify-center space-x-4 mb-12">
            <button className="bg-orange-500 text-white px-6 py-2 rounded-full hover:bg-primary transition-colors">
              Solicitar
            </button>
            <button className="bg-primary text-white px-6 py-2 rounded-full hover:bg-primary-accent transition-colors">
              Tarifario
            </button>
          </div>

          <div className="space-y-12">
            {loanOptions.map((loan, index) => (
              <div
                key={index}
                className={`flex flex-col md:flex-row ${index % 2 === 0 ? 'md:flex-row-reverse' : ''}
                                  items-center ${index % 2 === 1 ? 'bg-white' : 'bg-[#FFF5F0]'} rounded-xl  overflow-hidden`}
              >
                <div className="w-full md:w-1/3 p-6">
                  <img
                    src={loan.image}
                    alt={loan.title}
                    className="w-40 h-40 mx-auto rounded-full object-cover "
                  />
                </div>
                <div className="w-full md:w-2/3 p-6">
                  <h3 className="text-2xl font-bold text-primary mb-4">{loan.title}</h3>
                  <ul className="space-y-2">
                    {loan.details.map((detail, idx) => (
                      <li key={idx} className="flex items-start">
                        <span className="text-primary mr-2 text-lg flex-shrink-0">•</span>
                        <span className="text-sm text-neutral-100">{detail}</span>
                      </li>
                    ))}
                  </ul>
                </div>
              </div>
            ))}

            {/* Requisitos Section */}
            <div className="flex flex-col md:flex-row items-center bg-[#FFF5F0] rounded-xl  overflow-hidden">
              <div className="w-full md:w-1/3 p-6">
                <img
                  src={requirements.image}
                  alt="Requisitos"
                  className="w-40 h-40 mx-auto rounded-full object-cover "
                />
              </div>
              <div className="w-full md:w-2/3 p-6">
                <h3 className="text-2xl font-bold text-primary mb-4">Requisitos</h3>
                <ul className="space-y-2">
                  {requirements.items.map((req, index) => (
                    <li key={index} className="flex items-start">
                      <span className="text-neutral-100 mr-2 text-lg flex-shrink-0">•</span>
                      <span className="text-sm text-neutral-100">{req}</span>
                    </li>
                  ))}
                </ul>
              </div>
            </div>
          </div>
        </div>
      </div>
    </motion.div>
  );
};

export default MortgageLoans;