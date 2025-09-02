import { IconType } from 'react-icons';
import { FaCalculator, FaMapMarkerAlt } from 'react-icons/fa';

export interface NavItem {
    icon: IconType;
    label: string;
    href: string;
}

export interface SideNavProps { }

export interface InputFieldProps {
    id: string;
    label: string;
    value: number;
    onChange: (value: number) => void;
    className?: string;
    min?: number;
    max?: number;
    step?: number;
    decimals?: number;
    readOnly?: boolean;
}

export interface ModalProps {
    isOpen: boolean;
    onClose: () => void;
    children: React.ReactNode;
}

export interface CalculatorModalProps {
    isOpen: boolean;
    closeModal: () => void;
}

export const navItems: NavItem[] = [
    {
        icon: FaCalculator,
        label: 'Calculadora Financiera',
        href: '#',
    },
    {
        icon: FaMapMarkerAlt,
        label: 'Sucursales y Cajeros',
        href: '/mapa-ubicaciones',
    },
];

export const DEFAULT_LOAN_RATE = 23;
export const DEFAULT_CERTIFICATE_RATE = 18.75;


export const calculatorLabels = {
    loan: {
        title: 'Préstamo',
        amount: 'Monto del Préstamo',
        rate: 'Tasa Anual (%)',
        term: 'Plazo (meses)',
        result: 'Cuota Mensual:',
    },
    certificate: {
        title: 'Certificado',
        amount: 'Monto del certificado',
        rate: 'Tasa de interés anual (%)',
        term: 'Plazo (días)',
        result: 'Interés:',
        note: 'Nota: Este cálculo asume un año de 360 días.',
        monthsEquivalent: 'Equivalente a aproximadamente {0} meses',
    },
    common: {
        bankReferenceRate: 'Tasa de referencia del banco',
        fixedRate: 'Tasa fija:',
        days: '% a 90 días',
    },
};

export const initialValues = {
    loan: {
        amount: 0,
        term: 0,
    },
    certificate: {
        amount: 0,
        term: 0,
    },
};

export const inputLimits = {
    loan: {
        amount: { min: 1000, max: 1000000, step: 1000 },
        term: { min: 1, max: 360, step: 1 },
    },
    certificate: {
        amount: { min: 1000, max: 1000000, step: 1000 },
        term: { min: 1, max: 3650, step: 1 },
    },
    interestRate: { min: 0.01, max: 100, step: 0.01, decimals: 2 },
};