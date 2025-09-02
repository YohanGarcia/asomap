
import { FaShieldAlt, FaGlobeAmericas, FaMobileAlt } from 'react-icons/fa';
import { IDebitCardFeature, IDebitCardProps } from '@interfaces'

export const debitCardFeatures: IDebitCardFeature[] = [
    {
        icon: FaShieldAlt,
        title: "Seguridad Avanzada",
        description: "Protección contra fraudes y tecnología de chip EMV",
    },
    {
        icon: FaGlobeAmericas,
        title: "Aceptación Global",
        description: "Utiliza tu tarjeta en millones de establecimientos en todo el mundo",
    },
    {
        icon: FaMobileAlt,
        title: "Control Móvil",
        description: "Gestiona tu tarjeta y tus gastos desde nuestra app móvil",
    },
];

export const debitCardBenefits: string[] = [
    "Sin cuota anual",
    "Reembolso de cargos en cajeros automáticos",
    "Programa de recompensas por uso",
    "Notificaciones instantáneas de transacciones",
];

export const debitCardRequirements: string[] = [
    "Ser titular de una cuenta corriente o de ahorros",
    "Documento de identidad válido",
    "Comprobante de domicilio reciente",
    "Cumplir con los requisitos mínimos de saldo en cuenta",
];

export const debitCardData: IDebitCardProps = {
    bannerImage: "https://images.pexels.com/photos/6214474/pexels-photo-6214474.jpeg?auto=compress&cs=tinysrgb&w=1600",
    cardImage: "https://images.pexels.com/photos/4386366/pexels-photo-4386366.jpeg?auto=compress&cs=tinysrgb&w=800",
    title: "Tarjeta de Débito",
    description: "Accede a tu dinero de forma segura y conveniente, con beneficios exclusivos en cada compra.",
};