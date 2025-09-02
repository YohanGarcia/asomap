import React from 'react';
import { motion } from 'framer-motion';
import { IDebitCardPromoProps } from '@interfaces';
import { Button } from '@/components/ui';

const DebitCardPromo: React.FC<IDebitCardPromoProps> = ({ data }) => {
    const containerVariants = {
        hidden: { opacity: 0 },
        visible: {
            opacity: 1,
            transition: {
                staggerChildren: 0.2
            }
        }
    };

    const itemVariants = {
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

    return (
        <motion.div 
            className="bg-gradient-to-br from-orange-50 to-orange-100/50 py-16 sm:py-20 md:py-24 px-4 sm:px-6 md:px-8 relative overflow-hidden z-0"
            initial="hidden"
            whileInView="visible"
            viewport={{ once: true, margin: "-100px" }}
            variants={containerVariants}
        >
            <motion.div 
                className="absolute inset-0 bg-gradient-to-r from-orange-400 to-primary opacity-5"
                animate={{
                    backgroundPosition: ["0% 0%", "100% 100%"],
                }}
                transition={{
                    duration: 20,
                    ease: "linear",
                    repeat: Infinity,
                }}
            />
            
            <div className="container mx-auto flex flex-col lg:flex-row items-center justify-between relative z-10">
                <motion.div 
                    className="w-full lg:w-1/2 mb-12 lg:mb-0 text-center lg:text-left"
                    variants={itemVariants}
                >
                    <motion.h2 
                        className="text-3xl sm:text-4xl md:text-5xl font-bold mb-6 sm:mb-8"
                        variants={itemVariants}
                    >
                        {data.title}
                        <motion.span 
                            className="text-orange-500 block mt-2"
                            variants={itemVariants}
                        >
                            {data.highlighted_title}
                        </motion.span>
                    </motion.h2>
                    <motion.p 
                        className="mb-8 sm:mb-10 text-neutral-100 text-lg sm:text-xl leading-relaxed"
                        variants={itemVariants}
                    >
                        {data.description}
                    </motion.p>
                    <motion.div 
                        className="flex flex-col sm:flex-row justify-center lg:justify-start space-y-4 sm:space-y-0 sm:space-x-6"
                        variants={itemVariants}
                    >
                        <Button 
                            className="bg-orange-400 text-white px-8 py-3 rounded-lg hover:bg-primary transition-all duration-300 text-base font-medium transform hover:scale-105 hover:shadow-lg"
                        >
                            {data.primary_button_text}
                        </Button>
                        <Button 
                            className="bg-primary text-white px-8 py-3 rounded-lg hover:bg-orange-400 transition-all duration-300 text-base font-medium transform hover:scale-105 hover:shadow-lg"
                        >
                            {data.secondary_button_text}
                        </Button>
                    </motion.div>
                </motion.div>

                <motion.div 
                    className="w-full lg:w-3/4 flex justify-center lg:justify-end relative"
                    variants={itemVariants}
                >
                    <motion.div
                        className="relative w-full max-w-2xl"
                        whileHover={{ scale: 1.02 }}
                        transition={{ duration: 0.3 }}
                    >
                        <motion.div
                            className="absolute -inset-1 bg-gradient-to-r from-orange-400 to-primary rounded-2xl blur opacity-30"
                            animate={{
                                opacity: [0.3, 0.5, 0.3],
                            }}
                            transition={{
                                duration: 2,
                                repeat: Infinity,
                            }}
                        />
                        <img
                                                    src={data.image_url}
                        alt={data.image_alt}
                            className="relative rounded-xl shadow-2xl w-full transform transition-transform duration-300"
                        />
                    </motion.div>
                </motion.div>
            </div>
        </motion.div>
    );
};

export default DebitCardPromo;
