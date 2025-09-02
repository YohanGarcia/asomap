import { httpClient } from '../../config/httpClient';
import type { FinancialStatementsResponse } from '@/interfaces';
import { ENDPOINTS } from '@/constants';

export const financialStatementsService = {
    getFinancialStatements: async (): Promise<FinancialStatementsResponse> => {
        const response = await httpClient.get<FinancialStatementsResponse>(ENDPOINTS.COLLECTIONS.ABOUT.FINANCIAL_STATEMENTS);
        return response.data;
    }
}; 