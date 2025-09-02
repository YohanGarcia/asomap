import { httpClient } from '../../config/httpClient';
import type { MemoriesResponse } from '@/interfaces';
import { ENDPOINTS } from '@/constants';

export const memoriesService = {
    getMemories: async (): Promise<MemoriesResponse> => {
        const response = await httpClient.get<MemoriesResponse>(ENDPOINTS.COLLECTIONS.ABOUT.MEMORIES);
        return response.data;
    }
}; 