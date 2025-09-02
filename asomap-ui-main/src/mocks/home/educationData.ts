import { IEducationSectionProps } from '@interfaces';
import Image1 from '@assets/images/educations/prevenir-fraudes-online.jpg';
import Image2 from '@assets/images/educations/gestión-financiera-inteligente.jpg';
import Image3 from '@assets/images/educations/phishing.jpg';
import Image4 from '@assets/images/educations/seguridad-pagos-electronicos.jpg';

export const educationSectionData: IEducationSectionProps['data'] = {
    title: "Educación",
    subtitle: "Aprendiendo con Asomap",
    educationItems: [
        {
            image: Image1,
            alt: "Cómo prevenir fraudes Online",
            description: "¿Cómo prevenir fraudes online?"
        },
        {
            image: Image2,
            alt: "Gestión Financiera Inteligente",
            description: "Gestión Financiera Inteligente"
        },
        {
            image: Image3,
            alt: "Qué es el phishing",
            description: "Qué es el phishing"
        },
        {
            image: Image4,
            alt: "Seguridad en Pagos Electronicos",
            description: "Seguridad en Pagos Electronicos"
        }
    ],
    footerText: "Ir a ..",
};