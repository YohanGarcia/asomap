import { ENDPOINTS } from '@/constants';
import { debugLog, errorLog, getApiUrl } from '@/utils/environment';

export interface CommunityInitiative {
    id: number;
    title: string;
    description: string;
    impact: string;
    image_src: string | null;
    image_alt: string | null;
    category: {
        id: number;
        name: string;
        icon: string;
        description: string;
        is_active: boolean;
        created_at: string;
        updated_at: string;
    };
    is_active: boolean;
    created_at: string;
    updated_at: string;
}

export interface CommunityInitiativesResponse {
    count: number;
    next: string | null;
    previous: string | null;
    results: CommunityInitiative[];
}

export const communityInitiativesService = {
    getInitiatives: async (): Promise<CommunityInitiativesResponse> => {
        try {
            debugLog('[CommunityInitiativesService] Fetching initiatives from backend');
            const response = await fetch(getApiUrl(ENDPOINTS.COLLECTIONS.ABOUT.COMMUNITY_INITIATIVES));
            
            if (!response.ok) {
                throw new Error(`Backend returned ${response.status}: ${response.statusText}`);
            }

            const data = await response.json();
            debugLog('[CommunityInitiativesService] Initiatives received successfully:', data);
            return data;

        } catch (error) {
            errorLog('[CommunityInitiativesService] Error fetching initiatives:', error);
            throw error;
        }
    }
};
