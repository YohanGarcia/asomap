import { httpClient } from '../../config/httpClient';
import { ENDPOINTS } from '@/constants';
import type { IProductSectionResponse } from '@/interfaces';
import { debugLog, errorLog } from '@/utils/environment';

export const productSectionService = {
    getProductSection: async (): Promise<IProductSectionResponse['data'] | null> => {
        try {
            debugLog('[ProductSectionService] Fetching from backend');
            const response = await httpClient.get<IProductSectionResponse>(
                ENDPOINTS.COLLECTIONS.HOME.PRODUCT_SECTION
            );
            
            debugLog('[ProductSectionService] Backend response received successfully:', response.data);
            return response.data.data;
            
        } catch (error) {
            errorLog('[ProductSectionService] Error fetching product section data:', error);
            
            // No usar mock data, solo retornar null
            debugLog('[ProductSectionService] API error, returning null');
            return null;
        }
    }
};
