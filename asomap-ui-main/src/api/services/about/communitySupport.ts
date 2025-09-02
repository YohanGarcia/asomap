import { ENDPOINTS } from '@/constants';
import { debugLog, errorLog, getApiUrl} from '@/utils/environment';
import { communitySupportData } from '@/mocks/about/communitySupport';

export interface CommunitySupportResponse {
    data: {
        title: string;
        description: string;
        categories: Array<{
            id: string;
            name: string;
            icon: string;
            description: string;
        }>;
        initiatives: Array<{
            id: string;
            title: string;
            description: string;
            impact: string;
            imageUrl: string;
            category: string;
        }>;
    };
}

export const communitySupportService = {
    getCommunitySupport: async (): Promise<CommunitySupportResponse> => {
        try {
            // SIEMPRE intentar obtener datos del backend primero
            debugLog('[CommunitySupportService] Fetching from backend');
            const response = await fetch(getApiUrl(ENDPOINTS.COLLECTIONS.ABOUT.COMMUNITY_SUPPORT));
            
            if (!response.ok) {
                throw new Error(`Backend returned ${response.status}: ${response.statusText}`);
            }

            const data = await response.json();
            debugLog('[CommunitySupportService] Backend response received successfully:', data);

            // Transformar datos del backend al formato esperado por el frontend
            return {
                data: {
                    title: data.title || communitySupportData.title,
                    description: data.description || communitySupportData.description,
                    categories: data.categories?.map((cat: any) => ({
                        id: cat.id?.toString() || cat.name?.toLowerCase().replace(/\s+/g, '-'),
                        name: cat.name || '',
                        icon: cat.icon || 'FaHandHoldingHeart',
                        description: cat.description || ''
                    })) || communitySupportData.categories,
                    initiatives: data.initiatives?.map((init: any) => ({
                        id: init.id?.toString() || init.title?.toLowerCase().replace(/\s+/g, '-'),
                        title: init.title || '',
                        description: init.description || '',
                        impact: init.impact || '',
                        imageUrl: init.image_src || '', // Usar image_src del backend
                        category: init.category?.name || '' // Usar category.name del backend
                    })) || communitySupportData.initiatives
                }
            };

        } catch (error) {
            errorLog('[CommunitySupportService] Error fetching community support data:', error);
            
            // Solo usar mock si es un error de red real (no 404)
            if (error instanceof TypeError || (error instanceof Error && error.message.includes('fetch'))) {
                debugLog('[CommunitySupportService] Network error, using mock data as fallback');
                return { data: communitySupportData };
            }
            
            // Para otros errores (404, 500, etc.), lanzar el error
            throw error;
        }
    }
};
