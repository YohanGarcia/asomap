import { httpClient } from '../../config/httpClient';
import { ENDPOINTS } from '@/constants';
import { debugLog, errorLog } from '@/utils/environment';
import type { 
  IFraudReportPageAPIResponse, 
  IFraudReportPageData 
} from '@/interfaces';

export const fraudReportPageService = {
  getFraudReportPage: async (): Promise<IFraudReportPageData> => {
    try {
      debugLog('[FraudReportPageService] Fetching fraud report page data');
      
      const response = await httpClient.get<IFraudReportPageAPIResponse>(
        ENDPOINTS.COLLECTIONS.USER_SUPPORT.FRAUD_REPORT_PAGE
      );

      debugLog('[FraudReportPageService] API response:', response.data);

      if (!response.data.results || response.data.results.length === 0) {
        throw new Error('No fraud report page data found');
      }

      const apiData = response.data.results[0];

      // Transformar datos de la API al formato del frontend
      const transformedData: IFraudReportPageData = {
        id: apiData.id,
        title: apiData.title,
        description: apiData.description,
        isActive: apiData.is_active,
        createdAt: apiData.created_at,
        updatedAt: apiData.updated_at
      };

      debugLog('[FraudReportPageService] Transformed data:', transformedData);
      
      return transformedData;

    } catch (error) {
      errorLog('[FraudReportPageService] Error fetching fraud report page:', error);
      throw error;
    }
  }
};
