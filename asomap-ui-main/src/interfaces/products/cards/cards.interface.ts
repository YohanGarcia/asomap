export interface ICardBenefit {
  icon: string;
  text: string;
}

export interface ICardAPI {
  id: number;
  title: string;
  description: string;
  bannerImage: string | null;
  cardImage: string | null;
  card_type: string;
  features: string[];
  requirements: string[];
  benefits: ICardBenefit[];
  slug: string;
  is_active: boolean;
  created_at: string;
  updated_at: string;
}

export interface ICardsAPIResponse {
  count: number;
  next: string | null;
  previous: string | null;
  results: ICardAPI[];
}

export interface ICardData {
  id: number;
  title: string;
  description: string;
  bannerImage: string;
  cardImage: string;
  cardType: string;
  features: string[];
  requirements: string[];
  benefits: ICardBenefit[];
  slug: string;
}
