import { httpClient } from '../../config/httpClient';
import { ENDPOINTS } from '@/constants';
import type { IPekeAccountSummaryData } from '@/interfaces';
import { debugLog, errorLog } from '@/utils/environment';

export const pekeAccountSummaryService = {
    getPekeAccountSummary: async (): Promise<IPekeAccountSummaryData | null> => {
        try {
            debugLog('[PekeAccountSummaryService] Fetching from backend');
            const response = await httpClient.get<IPekeAccountSummaryData>(
                ENDPOINTS.COLLECTIONS.HOME.PEKE_ACCOUNT_SUMMARY
            );
            
            debugLog('[PekeAccountSummaryService] Backend response received successfully:', response.data);
            return response.data;
            
        } catch (error) {
            errorLog('[PekeAccountSummaryService] Error fetching peke account summary data:', error);
            
            // No usar mock data, solo retornar null
            debugLog('[PekeAccountSummaryService] API error, returning null');
            return null;
        }
    }
};
