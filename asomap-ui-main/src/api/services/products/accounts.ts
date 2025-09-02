import { httpClient } from '../../config/httpClient';
import { API_CONFIG } from '../../config/config';
import { ENDPOINTS } from '@/constants';
import type { IAccountsAPIResponse, IAccountData } from '@/interfaces';
import { debugLog, errorLog } from '@/utils/environment';

export const accountsService = {
  getAllAccounts: async (): Promise<IAccountData[]> => {
    try {
      debugLog('[AccountsService] Fetching all accounts from backend');
      const response = await httpClient.get<IAccountsAPIResponse>(
        ENDPOINTS.COLLECTIONS.PRODUCTS.ACCOUNTS
      );

      debugLog('[AccountsService] Backend response received successfully:', response.data);

      // Transformar la respuesta de la API al formato que espera la aplicación
      const transformedAccounts: IAccountData[] = response.data.results
        .filter(account => account.is_active) // Solo cuentas activas
        .map(account => ({
          id: account.id,
          title: account.title,
          description: account.description,
          bannerImage: account.bannerImage || '', // Imagen por defecto
          accountImage: account.accountImage || '', // Imagen por defecto
          category: account.category,
          features: account.features,
          requirements: account.requirements,
          benefits: account.benefits
        }));

      debugLog('[AccountsService] Transformed accounts data:', transformedAccounts);
      return transformedAccounts;

    } catch (error) {
      errorLog('[AccountsService] Error fetching accounts data:', error);
      // En desarrollo, retornar array vacío para evitar errores
      if (API_CONFIG.IS_DEVELOPMENT) {
        console.warn('[AccountsService] Development mode: returning empty array due to API error');
        return [];
      }
      throw error; // En producción, lanzar el error
    }
  },

  getAccountById: async (id: number): Promise<IAccountData | null> => {
    try {
      debugLog(`[AccountsService] Fetching account with ID ${id} from backend`);
      const response = await httpClient.get<IAccountData>(
        `${ENDPOINTS.COLLECTIONS.PRODUCTS.ACCOUNTS}${id}/`
      );

      debugLog('[AccountsService] Account response received successfully:', response.data);

      // Transformar la respuesta
      const account = response.data;
      const transformedAccount: IAccountData = {
        id: account.id,
        title: account.title,
        description: account.description,
        bannerImage: account.bannerImage || 'https://images.unsplash.com/photo-1563013544-824ae1b704d3?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&h=400&q=80',
        accountImage: account.accountImage || 'https://images.unsplash.com/photo-1601597111158-2fceff292cdc?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&h=400&q=80',
        category: account.category,
        features: account.features,
        requirements: account.requirements,
        benefits: account.benefits
      };

      debugLog('[AccountsService] Transformed account data:', transformedAccount);
      return transformedAccount;

    } catch (error) {
      errorLog(`[AccountsService] Error fetching account with ID ${id}:`, error);
      return null;
    }
  }
};
