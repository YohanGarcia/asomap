import { httpClient } from '../../config/httpClient';
import { ENDPOINTS } from '@/constants';
import type { SliderItemAPI } from '@/interfaces';
import { debugLog, errorLog } from '@/utils/environment';

export const sliderService = {
    getSlider: async (): Promise<SliderItemAPI[]> => {
        try {
            debugLog('[SliderService] Fetching from backend');
            const response = await httpClient.get<SliderItemAPI[]>(
                ENDPOINTS.COLLECTIONS.HOME.SLIDER
            );
            
            debugLog('[SliderService] Backend response received successfully:', response.data);
            debugLog('[SliderService] Response length:', response.data.length);
            debugLog('[SliderService] All slides:', response.data);
            
            // Validar que la respuesta es un array
            if (!Array.isArray(response.data)) {
                debugLog('[SliderService] Response is not an array');
                return [];
            }
            
            debugLog('[SliderService] Slides count:', response.data.length);
            debugLog('[SliderService] Processed slides:', response.data);
            return response.data;
            
        } catch (error) {
            errorLog('[SliderService] Error fetching slider data:', error);
            throw error;
        }
    }
};
