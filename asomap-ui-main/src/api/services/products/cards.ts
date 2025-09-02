import { httpClient } from '../../config/httpClient';
import { API_CONFIG } from '../../config/config';
import { ENDPOINTS } from '@/constants';
import { debugLog, errorLog } from '@/utils/environment';
import type { ICardsAPIResponse, ICardData } from '@/interfaces';

export const cardsService = {
  getAllCards: async (): Promise<ICardData[]> => {
    try {
      debugLog('[CardsService] Fetching all cards');
      
      const response = await httpClient.get<ICardsAPIResponse>(ENDPOINTS.COLLECTIONS.PRODUCTS.CARDS);
      
      // Filtrar solo tarjetas activas y transformar datos
      const cards: ICardData[] = response.data.results
        .filter(card => card.is_active)
        .map(card => ({
          id: card.id,
          title: card.title,
          description: card.description,
          bannerImage: card.bannerImage || '',
          cardImage: card.cardImage || '',
          cardType: card.card_type,
          features: card.features,
          requirements: card.requirements,
          benefits: card.benefits,
          slug: card.slug
        }));

      debugLog('[CardsService] Cards fetched successfully:', cards);
      return cards;

    } catch (error) {
      errorLog('[CardsService] Error fetching cards:', error);
      // En desarrollo, retornar array vacío para evitar errores
      if (API_CONFIG.IS_DEVELOPMENT) {
        console.warn('[CardsService] Development mode: returning empty array due to API error');
        return [];
      }
      throw error; // En producción, lanzar el error
    }
  },

  getCardBySlug: async (slug: string): Promise<ICardData | null> => {
    try {
      debugLog(`[CardsService] Fetching card by slug: ${slug}`);
      
      const cards = await cardsService.getAllCards();
      const card = cards.find(c => c.slug === slug);
      
      if (card) {
        debugLog('[CardsService] Card found:', card);
        return card;
      } else {
        debugLog('[CardsService] Card not found');
        return null;
      }

    } catch (error) {
      errorLog('[CardsService] Error fetching card by slug:', error);
      throw error;
    }
  }
};
