import { create } from 'zustand';
import type { HeaderResponse } from '@/interfaces';

interface LayoutState {
    headerData: HeaderResponse;
    setHeaderData: (data: HeaderResponse) => void;
}

export const useLayoutStore = create<LayoutState>((set) => ({
    headerData: {
        navigation: {
            individual: '',
            empresarial: ''
        },
        exchange: {
            base: '',
            lastUpdated: '',
            showBuyRate: false,
            showSellRate: false,
            rates: []
        }
    },
    setHeaderData: (data) => set({ headerData: data }),
})); 