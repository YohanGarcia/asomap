import { httpClient } from '../config/httpClient';
import { ENDPOINTS } from '@/constants';
import { debugLog, errorLog } from '@/utils/environment';
import type { 
  IServicesPageAPIResponse, 
  IServicesPageData 
} from '@/interfaces';

export const servicesService = {
  getServicesPage: async (): Promise<IServicesPageData> => {
    try {
      debugLog('[ServicesService] Fetching services page data');
      
      const response = await httpClient.get<IServicesPageAPIResponse>(
        ENDPOINTS.COLLECTIONS.SERVICES.MAIN
      );

      debugLog('[ServicesService] API response:', response.data);

      if (!response.data.results || response.data.results.length === 0) {
        throw new Error('No services page data found');
      }

      const apiData = response.data.results[0];

      // Transformar datos de la API al formato del frontend
      const transformedData: IServicesPageData = {
        title: apiData.title,
        subtitle: apiData.subtitle,
        searchPlaceholder: apiData.search_placeholder,
        noResultsText: apiData.no_results_text,
        internetBankingUrl: apiData.internet_banking_url,
        internetBankingButton: apiData.internet_banking_button,
        items: apiData.items,
        itemDetails: apiData.item_details.map(service => ({
          id: service.id,
          title: service.title,
          description: service.description,
          steps: service.steps,
          imageUrl: service.image_url,
          imageAlt: service.image_alt,
          pdfUrl: service.pdf_url
        }))
      };

      debugLog('[ServicesService] Transformed data:', transformedData);
      
      return transformedData;

    } catch (error) {
      errorLog('[ServicesService] Error fetching services page:', error);
      throw error;
    }
  }
};
