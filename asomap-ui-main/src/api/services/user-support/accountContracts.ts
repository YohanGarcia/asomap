import { httpClient } from '../../config/httpClient';
import { ENDPOINTS } from '@/constants';
import { debugLog, errorLog } from '@/utils/environment';
import type { 
  IAccountContractsAPIResponse, 
  IAccountContractsData,
  IContractData
} from '@/interfaces';

export const accountContractsService = {
  getAccountContracts: async (): Promise<IAccountContractsData | null> => {
    try {
      debugLog('[AccountContractsService] Fetching account contracts data');
      
      const response = await httpClient.get<IAccountContractsAPIResponse>(
        ENDPOINTS.COLLECTIONS.USER_SUPPORT.ACCOUNT_CONTRACTS
      );

      if (response.data.results.length === 0) {
        debugLog('[AccountContractsService] No account contracts data found');
        return null;
      }

      const apiData = response.data.results[0]; // Tomamos el primer resultado

      // Transformar contracts
      const contracts: IContractData[] = apiData.contracts.map(contract => ({
        title: contract.title,
        url: contract.url,
        category: contract.category
      }));

      const transformedData: IAccountContractsData = {
        id: apiData.id,
        title: apiData.title,
        description: apiData.description,
        contracts,
        categories: apiData.categories
      };

      debugLog('[AccountContractsService] Account contracts data fetched successfully:', transformedData);
      return transformedData;

    } catch (error) {
      errorLog('[AccountContractsService] Error fetching account contracts data:', error);
      throw error;
    }
  }
};
