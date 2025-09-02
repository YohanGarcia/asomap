import { create } from 'zustand';
import type { ExchangeRateResponse } from '@/interfaces';

interface ExchangeRateState {
    exchangeRateData: ExchangeRateResponse;
    setExchangeRateData: (data: ExchangeRateResponse) => void;
}

const initialState: ExchangeRateResponse = {
    base: "Tasa de Cambio",
    lastUpdated: "",
    showBuyRate: true,
    showSellRate: true,
    rates: [{
        currency: "US DOLAR",
        buyRate: 0,
        sellRate: 0
    }]
};

export const useExchangeRateStore = create<ExchangeRateState>((set) => ({
    exchangeRateData: initialState,
    setExchangeRateData: (data) => set({ exchangeRateData: data }),
}));
