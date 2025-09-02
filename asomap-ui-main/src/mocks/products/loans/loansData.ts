import { ILoan, IPersonLoan, IBanner, IWhyLoan } from '@interfaces';
import ImageBannerLoans from '@assets/images/loans/ImageLoans.png';
import ImagePersonal from '@assets/images/loans/personal.png';
import ImageCar from '@assets/images/loans/car.png';
import ImageHome from '@assets/images/loans/home.png';
import ImageCard from '@assets/images/loans/ImageCard.png';
import ImageHouse from '@assets/images/loans/BuyHouse.png';

export const bannerData: IBanner = {
    title: "Préstamos",
    subtitle: "Alcancemos la meta juntos",
    imageUrl: ImageBannerLoans,
};

export const loansData: ILoan[] = [
    { type: 'consumer', title: 'Préstamo Consumo', image: ImagePersonal },
    { type: 'comercial', title: 'Préstamo Comercial', image: ImageCar },
    { type: 'mortgage', title: 'Préstamo Hipotecario', image: ImageHome },
];

export const personLoansData: IPersonLoan[] = [
    { title: 'Mi Préstamo de Consumo', description: 'Simulá y cotizá ahora tu préstamo de consumo', image: ImageCard },
    { title: 'Mi Préstamo Comercial', description: 'Simulá y cotizá ahora tu préstamo comercial', image: ImageCard },
    { title: 'Mi Préstamo Hipotecario', description: 'Simulá y cotizá ahora tu préstamo hipotecario', image: ImageCard },
];

export const whyLoanData: IWhyLoan = {
    title: "¿Por qué adquirir un Préstamo en Banco ASOMAP?",
    reasons: [
        "Nuestras soluciones crediticias son las más competitivas del mercado.",
        "Contamos con facilidades que te ayudarán a alcanzar tus metas más rápido. Los abonos y precancelación de nuestros créditos, no contemplan penalización.",
        "Buscamos ser tu mejor aliado. Nuestros productos crediticios, cuentan con: financiamiento de gastos legales, seguro de vida y seguro de desgravamen."
    ],
    existingLoanTitle: "¿Ya cuentas con un Préstamo?",
    existingLoanDescription: "Conoce más de tu Crédito Hipotecario y disfruta de sus beneficios",
    image: ImageHouse
};