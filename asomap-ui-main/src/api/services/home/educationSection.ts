import { httpClient } from '../../config/httpClient';
import { ENDPOINTS } from '@/constants';
import type { IEducationSectionProps } from '@/interfaces';
import { debugLog, errorLog } from '@/utils/environment';

export const educationSectionService = {
    getEducationSection: async (): Promise<IEducationSectionProps['data']> => {
        try {
            debugLog('[EducationSectionService] Fetching from backend');
            const response = await httpClient.get<{ data: IEducationSectionProps['data'] }>(
                ENDPOINTS.COLLECTIONS.HOME.EDUCATION_SECTION
            );
            
            debugLog('[EducationSectionService] Backend response received successfully:', response.data);
            return response.data.data;
            
        } catch (error) {
            errorLog('[EducationSectionService] Error fetching education section data:', error);
            throw error;
        }
    }
};
