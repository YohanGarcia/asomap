import { httpClient } from '@/api';
import { API_CONFIG } from '@api';
import { ENDPOINTS } from '@/constants';
import type { FooterResponse } from '@/interfaces';
import { footerMockData } from '@mocks';

export const footerService = {
    getFooter: async (): Promise<FooterResponse> => {
        if (API_CONFIG.IS_DEVELOPMENT) {
            return Promise.resolve(footerMockData);
        }
        const response = await httpClient.get<FooterResponse>(ENDPOINTS.COLLECTIONS.LAYOUT.FOOTER);
        return response.data;
    }
}; 