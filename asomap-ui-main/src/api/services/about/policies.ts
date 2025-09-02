import { httpClient } from '../../config/httpClient';
import type { PoliciesResponse } from '@/interfaces';
import { ENDPOINTS } from '@/constants';

export const policiesService = {
    getPolicies: async (): Promise<PoliciesResponse> => {
        const response = await httpClient.get<PoliciesResponse>(ENDPOINTS.COLLECTIONS.ABOUT.POLICIES);
        return response.data;
    }
}; 