// financialCertificateData.ts

import { FinancialCertificateData } from '@interfaces';
import BannerImage from '@assets/images/financialCertificate/ImageFinancialCertificate.png';
import ImageFinancialCertificate from '@assets/images/financialCertificate/ImageFinancialCertificate.png';

export const financialCertificateData: FinancialCertificateData = {
    banner: {
        imageUrl: BannerImage,
    },
    mainTitle: "Certificado Financiero",
    subtitle: "Multiplica tu dinero con un depósito a plazo fijo",
    cta: {
        apply: "Solicitar",
        rates: "Tarifario"
    },
    benefits: {
        title: "Beneficios de tu Certificado Financiero",
        items: [
            {
                title: "Alta rentabilidad",
                description: "Obtén los mejores rendimientos del mercado"
            },
            {
                title: "Flexibilidad",
                description: "Elige el plazo que más te convenga"
            },
            {
                title: "Confianza",
                description: "Respaldado por una institución sólida"
            },
            {
                title: "Manejo en línea",
                description: "Gestiona tu inversión desde cualquier lugar"
            }
        ]
    },
    investment: {
        title: "Tu nueva Inversión",
        subtitle: "Especificaciones del depósito a plazo fijo para personas:",
        details: [
            "Plazo desde 30 a 180 días",
            "Requiere de una apertura de cuenta de ahorro o corriente",
            "Inversión desde $5,000,000.00",
            "Pago de interés al vencimiento de tu inversión",
            "Acerca tasa de interés según plazo y el monto de apertura",
            "Acceso en todo momento a la información desde tu Internet Banking"
        ],
        imageUrl: ImageFinancialCertificate
    },
    rates: {
        title: "Tarifas",
        items: [
            { label: "Monto de apertura", value: "$5,000,000.00" },
            { label: "Balance mínimo para el cobro de la comisión", value: "$5,000,000.00" },
            { label: "Pago de interés Anual", value: "9.5%" },
            { label: "Comisión por débajo de balance mínimo", value: "$500.00" },
            { label: "Comisión por cancelación antes de un mes transcurrido", value: "Exonerada" },
            { label: "Reposición por libreta perdida", value: "$250.00" }
        ]
    },
    requirements: {
        title: "Requisitos",
        items: [
            "El menor debe hacerse acompañar de uno de sus padres o tutor",
            "Identificación oficial vigente del representante o tutor",
            "Acta de nacimiento original del menor de edad"
        ]
    },
    depositRates: {
        title: "Escala de Tasas de Captaciones de Depósitos",
        items: [
            { range: 'De 10,000.00 a 500,000.00', rate: '5%', term: 'de 30 a 90 días' },
            { range: 'De 500,001.00 a 1,000,000.00', rate: '6%', term: 'de 30 a 90 días' },
            { range: 'De 1,000,001.00 a 3,000,000.00', rate: '7.5%', term: 'de 30 a 90 días' },
            { range: '3,000,001.00 EN ADELANTE', rate: '8%', term: 'De 30 a 90 días' },
        ],
        validFrom: "Vigente desde el 31 de enero del 2023",
    },
    faq: {
        title: "Preguntas Frecuentes Certificado Financiero",
        items: [
            {
                question: "¿Qué es una inversión?",
                answer: "Una inversión es la colocación de capital en una operación, proyecto o iniciativa empresarial con el fin de obtener una ganancia en el futuro."
            },
            {
                question: "¿Cuáles son los requisitos para abrir una inversión en ASOMAP?",
                answer: "Los requisitos específicos pueden variar. Por favor, consulte con un representante de ASOMAP para obtener la información más actualizada."
            },
            {
                question: "¿Cuáles son los plazos disponibles para mi inversión?",
                answer: "Los plazos disponibles van desde 30 hasta 180 días, según lo mencionado en las especificaciones de la inversión."
            }
        ]
    }
};