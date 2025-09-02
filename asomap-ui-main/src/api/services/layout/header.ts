import { httpClient } from '@/api';
import { ENDPOINTS } from '@/constants';
import type { HeaderResponse, NavigationResponse, ExchangeRateResponse, ExchangeRateAPIResponse } from '@/interfaces';
import { debugLog, errorLog } from '@/utils/environment';
import { API_CONFIG } from '@api';
import { headerMockData } from '@mocks';

export const headerService = {
    getHeader: async (): Promise<HeaderResponse> => {
        if (API_CONFIG.IS_DEVELOPMENT) {
            return Promise.resolve(headerMockData);
        }

        const response = await httpClient.get<HeaderResponse>(ENDPOINTS.COLLECTIONS.LAYOUT.HEADER);
        return response.data;
    },

    getNavigation: async (): Promise<NavigationResponse> => {
        if (API_CONFIG.IS_DEVELOPMENT) {
            return Promise.resolve(headerMockData.navigation);
        }

        const response = await httpClient.get<NavigationResponse>(ENDPOINTS.COLLECTIONS.LAYOUT.HEADER);
        return response.data;
    },

    getExchangeRate: async (): Promise<ExchangeRateResponse> => {
        try {
            debugLog('[HeaderService] Fetching exchange rate from backend');
            const response = await httpClient.get<ExchangeRateAPIResponse>(ENDPOINTS.COLLECTIONS.LAYOUT.EXCHANGE_RATE);
            
            debugLog('[HeaderService] Exchange rate response received:', response.data);
            
            // Transformar la respuesta de la API al formato esperado
            const exchangeRate: ExchangeRateResponse = {
                base: "Tasa de Cambio",
                lastUpdated: response.data.lastUpdated,
                showBuyRate: response.data.showBuyRate,
                showSellRate: response.data.showSellRate,
                rates: response.data.rates
            };
            
            debugLog('[HeaderService] Transformed exchange rate:', exchangeRate);
            return exchangeRate;
            
        } catch (error) {
            errorLog('[HeaderService] Error fetching exchange rate:', error);
            
            // Solo usar mock si es un error de red real (no 404)
            if (error instanceof TypeError || (error instanceof Error && error.message.includes('fetch'))) {
                debugLog('[HeaderService] Network error, using mock data as fallback');
                return headerMockData.exchange;
            }
            
            // Para otros errores (404, 500, etc.), usar mock data como fallback
            debugLog('[HeaderService] API error, using mock data as fallback');
            return headerMockData.exchange;
        }
    }
};