import { httpClient } from '../../config/httpClient';
import { ENDPOINTS } from '@/constants';
import { debugLog, errorLog } from '@/utils/environment';
import type { 
  IAbandonedAccountsAPIResponse, 
  IAbandonedAccountsData,
  IAccountTypeData,
  IYearData
} from '@/interfaces';

export const abandonedAccountsService = {
  getAbandonedAccounts: async (): Promise<IAbandonedAccountsData | null> => {
    try {
      debugLog('[AbandonedAccountsService] Fetching abandoned accounts data');
      
      const response = await httpClient.get<IAbandonedAccountsAPIResponse>(
        ENDPOINTS.COLLECTIONS.USER_SUPPORT.ABANDONED_ACCOUNTS
      );

      if (response.data.results.length === 0) {
        debugLog('[AbandonedAccountsService] No abandoned accounts data found');
        return null;
      }

      const apiData = response.data.results[0]; // Tomamos el primer resultado

      // Transformar account_types
      const accountTypes: IAccountTypeData[] = apiData.account_types.map(type => ({
        id: type.id,
        label: type.label,
        description: type.description
      }));

      // Transformar years y documents
      const years: IYearData[] = apiData.years.map(year => {
        const documents = year.documents;
        
        // Mapear documentos usando el campo 'type' del backend
        const documentEntries = Object.entries(documents);
        
        let abandonedDoc = null;
        let inactiveDoc = null;
        
        for (const [, doc] of documentEntries) {
          if (doc.type === 'abandoned') {
            abandonedDoc = doc;
          } else if (doc.type === 'inactive') {
            inactiveDoc = doc;
          }
        }

        return {
          year: year.year,
          documents: {
            abandoned: {
              title: abandonedDoc?.title || '',
              url: abandonedDoc?.url || '',
              date: abandonedDoc?.date || ''
            },
            inactive: {
              title: inactiveDoc?.title || '',
              url: inactiveDoc?.url || '',
              date: inactiveDoc?.date || ''
            }
          }
        };
      });

      const transformedData: IAbandonedAccountsData = {
        id: apiData.id,
        title: apiData.title,
        description: apiData.description,
        accountTypes,
        years
      };

      debugLog('[AbandonedAccountsService] Abandoned accounts data fetched successfully:', transformedData);
      return transformedData;

    } catch (error) {
      errorLog('[AbandonedAccountsService] Error fetching abandoned accounts data:', error);
      throw error;
    }
  }
};
