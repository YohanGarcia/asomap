import { httpClient } from '../../config/httpClient';
import { ENDPOINTS } from '@/constants';
import type { INewsData, INewsAPIResponse } from '@/interfaces';
import { debugLog, errorLog } from '@/utils/environment';
import { newsData } from '@/mocks/news/newsData';

export const newsService = {
    getNews: async (): Promise<INewsData> => {
        try {
            debugLog('[NewsService] Fetching from backend');
            const response = await httpClient.get<INewsAPIResponse>(
                ENDPOINTS.COLLECTIONS.NEWS.ALL
            );

            debugLog('[NewsService] Backend response received successfully:', response.data);

            // Transformar la respuesta de la API al formato que espera la aplicación
            const transformedNews: INewsData = {
                banner: {
                    title: "Últimas Noticias",
                    imageUrl: "https://images.unsplash.com/photo-1560472355-536de3962603?q=80&w=1200"
                },
                slides: response.data.results.map(item => ({
                    id: item.id,
                    image: item.image,
                    title: item.title,
                    description: item.description,
                    date: item.date,
                    author: item.author,
                    category: item.category,
                    tags: item.tags,
                    fullContent: item.full_content,
                    media: item.media,
                    relatedLinks: item.related_links
                }))
            };

            debugLog('[NewsService] Transformed news data:', transformedNews);
            return transformedNews;

        } catch (error) {
            errorLog('[NewsService] Error fetching news data:', error);
            if (error instanceof TypeError || (error instanceof Error && error.message.includes('fetch'))) {
                debugLog('[NewsService] Network error, using mock data as fallback');
                return newsData;
            }
            debugLog('[NewsService] API error, using mock data as fallback');
            return newsData;
        }
    }
};
