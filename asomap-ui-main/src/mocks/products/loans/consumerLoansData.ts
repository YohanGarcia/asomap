import { IConsumerLoanData } from '@interfaces';

import ImageConsumerLoans from '@assets/images/loans/ImageConsumeLoans.png';
import ImageFinancialLoans from '@assets/images/loans/FinancialLoans.png';
import ImageCardLoans from '@assets/images/loans/ImageCard.png';

export const consumerLoansData: IConsumerLoanData = {
    banner: {
        title: "Préstamos de Consumo",
        imageUrl: ImageConsumerLoans,
    },
    subtitle: "¡Solicita ahora nuestro producto de financiamiento, el momento de cumplir tus sueños!",
    benefits: [
        {
            title: "Altamente adaptable",
            description: "Ofrece montos y plazos ajustados a sus necesidades.",
            iconUrl: ImageFinancialLoans,
        },
        {
            title: "Ágil y flexible",
            description: "Obtén tu préstamo de manera rápida y flexible para ganar tiempo.",
            iconUrl: ImageFinancialLoans,
        },
        {
            title: "Competitivo",
            description: "Accede a una tasa de interés altamente competitiva.",
            iconUrl: ImageFinancialLoans,
        },
        {
            title: "Respaldo y cobertura",
            description: "Cuenta con cobertura del seguro de vida sobre saldo deudor.",
            iconUrl: ImageFinancialLoans,
        }
    ],
    requirements: {
        title: "Adquiere un Préstamos de Consumo Requisitos",
        items: [
            { text: "Cédula de identidad y electoral o pasaporte (para extranjeros)." },
            { text: "Carta de trabajo." },
            { text: "Tres últimos volantes de pago." }
        ],
        imageUrl: ImageCardLoans,
    }
};