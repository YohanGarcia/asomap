export interface ServiceRate {
    service: string;
    description: string;
    rate: string;
    details?: string[];
}

export interface ServiceRatesData {
    title: string;
    description: string;
    categories: {
        name: string;
        rates: ServiceRate[];
    }[];
}

export const serviceRatesData: ServiceRatesData = {
    title: 'Tarifas de Servicios',
    description: 'Información detallada sobre las tarifas de nuestros servicios',
    categories: [
        {
            name: 'Servicios Básicos',
            rates: [
                {
                    service: 'Apertura de Cuenta',
                    description: 'Proceso de apertura de cuenta nueva',
                    rate: 'RD$ 500.00',
                    details: [
                        'Incluye tarjeta de débito',
                        'Kit de bienvenida',
                        'Acceso a banca en línea'
                    ]
                },
                {
                    service: 'Mantenimiento Mensual',
                    description: 'Cargo por mantenimiento de cuenta',
                    rate: 'RD$ 100.00',
                    details: [
                        'Aplica a cuentas de ahorro regular',
                        'Exento para cuentas premium'
                    ]
                }
            ]
        },
        {
            name: 'Servicios Electrónicos',
            rates: [
                {
                    service: 'Transferencia Interbancaria',
                    description: 'Transferencias a otros bancos',
                    rate: 'RD$ 75.00',
                    details: [
                        'Procesamiento mismo día',
                        'Límite máximo RD$ 1,000,000.00'
                    ]
                },
                {
                    service: 'Pago de Servicios',
                    description: 'Pagos de servicios públicos',
                    rate: 'Gratis',
                    details: [
                        'Luz, agua, teléfono',
                        'Sin comisión adicional'
                    ]
                }
            ]
        },
        {
            name: 'Tarjetas',
            rates: [
                {
                    service: 'Reposición de Tarjeta',
                    description: 'Reemplazo de tarjeta por pérdida o daño',
                    rate: 'RD$ 300.00',
                    details: [
                        'Entrega en 3-5 días hábiles',
                        'Incluye nueva activación'
                    ]
                },
                {
                    service: 'Avance de Efectivo',
                    description: 'Retiro de efectivo con tarjeta de crédito',
                    rate: '6% del monto',
                    details: [
                        'Mínimo RD$ 300.00',
                        'Sujeto a disponibilidad'
                    ]
                }
            ]
        }
    ]
};
