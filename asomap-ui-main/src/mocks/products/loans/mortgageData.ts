import { IMortgageLoansData } from '@interfaces';
import ImageMortgage from '@assets/images/loans/ImageMortgage.png';
import ImageCard from '@assets/images/loans/ImageCard.png';

export const mortgageLoansData: IMortgageLoansData = {
    bannerData: {
        imageUrl: ImageMortgage,
    },
    loansData: [
        {
            title: "Compra de vivienda",
            image: ImageCard,
            details: [
                "Financiamiento máximo de hasta del 80% del inmueble, incluye gastos legales.",
                "Plazo de hasta 20 años.",
                "Tasa de interés preferencial.",
                "Aceptamos distintos comprobantes de ingresos.",
                "Ingresos mínimos requeridos del grupo familiar de $600.00, durante el plazo del crédito"
            ]
        },
        {
            title: "Ampliación o remodelación",
            image: ImageCard,
            details: [
                "Hasta el 100% del presupuesto de la obra, sin exceder del 80% del valor comercial del inmueble.",
                "Plazo de hasta 20 años.",
                "Aceptamos distintos comprobantes de ingresos.",
                "Tasa de interés preferencial."
            ]
        },
        {
            title: "Contrucción",
            image: ImageCard,
            details: [
                "Construye tu vivienda con un crédito hipotecario.",
                "Financiamiento de hasta el 70% del valor del proyecto.",
                "Plazo de hasta 20 años.",
                "Tasa de interés preferencial en función del monto de la obra.",
                "Aceptamos distintos comprobantes de ingresos.",
                "Ingresos mínimos requeridos del grupo familiar de $600.00, durante el plazo del crédito.",
                "Forma de pago: desembolsos según el avance de la obra."
            ]
        },
        {
            title: "Compra de terreno",
            image: ImageCard,
            details: [
                "Adquiere el terreno para construir tu vivienda",
                "Financiamiento máximo de hasta el 70% del valor del terreno.",
                "Plazo de hasta 15 años.",
                "Aceptamos distintos comprobantes de ingresos.",
                "Tasa de interés preferencial."
            ]
        }
    ],
    requirements: {
        image: ImageCard,
        items: [
            "Para adquirir un Crédito Hipotecario:",
            "Ser mayor de 21 años.",
            "Ingreso mínimo de $600 del grupo familiar durante el plazo del crédito.",
            "Estabilidad laboral.",
            "Buen récord crediticio."
        ]
    }
};