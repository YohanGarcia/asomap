import { httpClient } from '../../config/httpClient';
import { ENDPOINTS } from '@/constants';
import { debugLog, errorLog } from '@/utils/environment';
import type { 
  IClaimRequestPageAPIResponse, 
  IClaimRequestPageData 
} from '@/interfaces';

export const claimRequestPageService = {
  getClaimRequestPage: async (): Promise<IClaimRequestPageData> => {
    try {
      debugLog('[ClaimRequestPageService] Fetching claim request page data');
      
      const response = await httpClient.get<IClaimRequestPageAPIResponse>(
        ENDPOINTS.COLLECTIONS.USER_SUPPORT.CLAIM_REQUEST_PAGE
      );

      debugLog('[ClaimRequestPageService] API response:', response.data);

      if (!response.data.results || response.data.results.length === 0) {
        throw new Error('No claim request page data found');
      }

      const apiData = response.data.results[0];

      // Transformar datos de la API al formato del frontend
      const transformedData: IClaimRequestPageData = {
        id: apiData.id,
        title: apiData.title,
        description: apiData.description,
        isActive: apiData.is_active,
        createdAt: apiData.created_at,
        updatedAt: apiData.updated_at
      };

      debugLog('[ClaimRequestPageService] Transformed data:', transformedData);
      
      return transformedData;

    } catch (error) {
      errorLog('[ClaimRequestPageService] Error fetching claim request page:', error);
      throw error;
    }
  }
};
