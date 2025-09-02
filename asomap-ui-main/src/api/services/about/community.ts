
import { API_CONFIG } from '../../config/config';
import { ENDPOINTS } from '@/constants';
import type { CommunitySupportResponse } from '@/interfaces';
import { debugLog, errorLog } from '@/utils/environment';
import { communitySupportData } from '@/mocks/about/communitySupport';

export const communityService = {
    getCommunitySupport: async (): Promise<CommunitySupportResponse> => {
        try {
            // SIEMPRE intentar obtener datos del backend primero
            debugLog('[CommunityService] Fetching from backend');
            const url = `${API_CONFIG.BASE_URL}${ENDPOINTS.COLLECTIONS.ABOUT.COMMUNITY_SUPPORT}`;
            debugLog('[CommunityService] Using URL:', url);
            
            // Usar fetch directo en lugar de httpClient para debugging
            const response = await fetch(url, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json',
                },
                mode: 'cors',
                credentials: 'omit'
            });
            
            debugLog('[CommunityService] Response status:', response.status);
            debugLog('[CommunityService] Response ok:', response.ok);
            
            if (!response.ok) {
                throw new Error(`HTTP ${response.status}: ${response.statusText}`);
            }
            
            const data = await response.json();
            debugLog('[CommunityService] Response data received:', data);
            
            // El backend devuelve directamente los datos, necesitamos transformarlos
            return {
                data: {
                    title: data.title || '',
                    description: data.description || '',
                    categories: data.categories?.map((cat: any) => ({
                        id: cat.id?.toString() || '',
                        name: cat.name || '',
                        icon: cat.icon || 'FaHandHoldingHeart',
                        description: cat.description || ''
                    })) || [],
                    initiatives: data.initiatives?.map((init: any) => ({
                        id: init.id?.toString() || '',
                        title: init.title || '',
                        description: init.description || '',
                        impact: init.impact || '',
                        imageUrl: init.image_src || '',
                        category: init.category?.name || ''
                    })) || []
                }
            };

        } catch (error) {
            errorLog('[CommunityService] Error fetching community support data:', error);
            debugLog('[CommunityService] Error type:', typeof error);
            debugLog('[CommunityService] Error instanceof Error:', error instanceof Error);
            debugLog('[CommunityService] Error instanceof TypeError:', error instanceof TypeError);
            
            // Solo usar mock si es un error de red real (no 404)
            if (error instanceof TypeError || (error instanceof Error && error.message.includes('fetch'))) {
                debugLog('[CommunityService] Network error, using mock data as fallback');
                return { data: communitySupportData };
            }
            
            // Para otros errores (404, 500, etc.), lanzar el error
            throw error;
        }
    }
}; 