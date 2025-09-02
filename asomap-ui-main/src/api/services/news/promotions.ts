import { httpClient } from '../../config/httpClient';
import { ENDPOINTS } from '@/constants';
import type { IPromotionsData, IPromotionsAPIResponse } from '@/interfaces';
import { debugLog, errorLog } from '@/utils/environment';
import { promotionsData } from '@/mocks/news/promotionsData';

export const promotionsService = {
    getPromotions: async (): Promise<IPromotionsData> => {
        try {
            debugLog('[PromotionsService] Fetching from backend');
            const response = await httpClient.get<IPromotionsAPIResponse>(
                ENDPOINTS.COLLECTIONS.NEWS.PROMOTIONS
            );

            debugLog('[PromotionsService] Backend response received successfully:', response.data);

            // Transformar la respuesta de la API al formato que espera la aplicación
            const transformedPromotions: IPromotionsData = {
                banner: {
                    title: "Promociones",
                    imageUrl: "https://images.unsplash.com/photo-1556742393-d75f468bfcb0?q=80&w=1200"
                },
                slides: response.data.results
                    .filter(promotion => promotion.is_active) // Solo promociones activas
                    .map(promotion => ({
                        id: promotion.id,
                        image: promotion.image,
                        title: promotion.title,
                        description: promotion.description,
                        date: promotion.fecha_inicio, // Usar fecha_inicio como date
                        slug: promotion.title.toLowerCase().replace(/\s+/g, '-'), // Generar slug desde título
                        validUntil: promotion.validUntil,
                        category: promotion.category,
                        tags: promotion.tags,
                        content: promotion.full_content,
                        media: promotion.media,
                        relatedLinks: promotion.related_links,
                        terms: promotion.terms
                    }))
            };

            debugLog('[PromotionsService] Transformed promotions data:', transformedPromotions);
            return transformedPromotions;

        } catch (error) {
            errorLog('[PromotionsService] Error fetching promotions data:', error);
            if (error instanceof TypeError || (error instanceof Error && error.message.includes('fetch'))) {
                debugLog('[PromotionsService] Network error, using mock data as fallback');
                return promotionsData;
            }
            debugLog('[PromotionsService] API error, using mock data as fallback');
            return promotionsData;
        }
    }
};
