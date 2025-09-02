import { ENDPOINTS } from '@/constants';
import { debugLog, errorLog, getApiUrl } from '@/utils/environment';

export interface CommunityCategory {
    id: number;
    name: string;
    icon: string;
    description: string;
    is_active: boolean;
    created_at: string;
    updated_at: string;
}

export interface CommunityCategoriesResponse {
    count: number;
    next: string | null;
    previous: string | null;
    results: CommunityCategory[];
}

export const communityCategoriesService = {
    getCategories: async (): Promise<CommunityCategoriesResponse> => {
        try {
            debugLog('[CommunityCategoriesService] Fetching categories from backend');
            const response = await fetch(getApiUrl(ENDPOINTS.COLLECTIONS.ABOUT.COMMUNITY_CATEGORIES));
            
            if (!response.ok) {
                throw new Error(`Backend returned ${response.status}: ${response.statusText}`);
            }

            const data = await response.json();
            debugLog('[CommunityCategoriesService] Categories received successfully:', data);
            return data;

        } catch (error) {
            errorLog('[CommunityCategoriesService] Error fetching categories:', error);
            throw error;
        }
    }
};
