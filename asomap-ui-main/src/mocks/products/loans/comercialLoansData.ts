import { ICommercialLoansData } from '@interfaces';
import ImageComercial from '@assets/images/loans/ImageComercial.png'
import ImageFinancialLoans from '@assets/images/loans/FinancialLoans.png';
import ImageCard from '@assets/images/loans/ImageCard.png'

export const commercialLoansData: ICommercialLoansData = {
    bannerData: {
        title: 'Préstamos Comercial',
        imageUrl: ImageComercial,
    },
    title: 'Préstamos Comercial',
    description: 'Accede a la solución de financiamiento de capital de trabajo o inversión, que tu negocio necesita.',
    buttons: {
        primary: 'Solicitar',
        secondary: 'Tarifario'
    },
    benefitsTitle: 'Beneficios de nuestro Préstamos Comerciales',
    benefitsDescription: 'Impulsa tu negocio. Descubre la solución de financiamiento estratégico para ti.',
    benefits: [
        {
            title: "Financiamiento estratégico",
            description: "Gestiona el capital necesario para el crecimiento de tu empresa, adquisición de inventario o equipos.",
            image: ImageFinancialLoans,
        },
        {
            title: "Garantías",
            description: "Contamos con garantías que se ajustan a tus necesidades de financiamiento.",
            image: ImageFinancialLoans,
        },
        {
            title: "Competitividad",
            description: "Accede a tasas de interés competitivas que se ajustan al perfil de tu empresa y plazo de tu necesidad.",
            image: ImageFinancialLoans,
        },
        {
            title: "Respaldo y cobertura",
            description: "Cuenta con respaldo en todo momento. Estamos a tu servicio y presentes en todo el país.",
            image: ImageFinancialLoans,
        }
    ],
    requirements: {
        image: ImageFinancialLoans,
        title: "Para adquirir un Préstamos Comercial",
        items: [
            "2 años de actividad comercial y económica para personas jurídicas",
            "1 año para personas naturales",
            "Sin días de atraso en el último mes"
        ]
    },
    familyImageUrl: ImageCard,
    subtitle: undefined,
    banner: undefined
};