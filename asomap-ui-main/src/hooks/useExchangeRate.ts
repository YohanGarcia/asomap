import { useState, useEffect } from 'react';
import { exchangeRateData } from '@/mocks';

interface ExchangeRate {
    currency: string;
    buyRate?: number;
    sellRate?: number;
    rate?: number;
}

interface ExchangeRateData {
    rates: ExchangeRate[];
}

export const useExchangeRate = () => {
    const [data, setData] = useState<ExchangeRateData>({ rates: [] });

    useEffect(() => {
        // En un entorno real, aquí se haría la llamada a la API
        // Por ahora, usamos los datos estáticos
        setData({ rates: exchangeRateData.rates });
    }, []);

    return {
        exchangeRateData: data,
        isLoading: false,
        error: null
    };
};
