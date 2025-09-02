export interface IPromotionsData {
  banner: {
    title: string;
    imageUrl: string;
  };
  slides: IPromotionSlide[];
}

export interface IPromotionSlide {
  id: number;
  image: string;
  title: string;
  description: string;
  date: string;
  slug: string;
  validUntil?: string;
  category?: string;
  tags?: string[];
  content?: IPromotionContent[];
  media?: IPromotionMedia[];
  relatedLinks?: IPromotionLink[];
  terms?: string[];
}

export interface IPromotionContent {
  type: 'paragraph' | 'subtitle' | 'quote' | 'list';
  content: string | string[];
}

export interface IPromotionMedia {
  type: 'image' | 'video';
  url: string;
  caption?: string;
}

export interface IPromotionLink {
  url: string;
  title: string;
  description?: string;
}

// Interfaces para la API
export interface IPromotionSlideAPI {
  id: number;
  image: string;
  title: string;
  description: string;
  category?: string;
  tags?: string[];
  full_content?: IPromotionContent[];
  media?: IPromotionMedia[];
  related_links?: IPromotionLink[];
  validUntil?: string;
  terms?: string[];
  fecha_inicio: string;
  fecha_fin: string;
  is_active: boolean;
  created_at: string;
  updated_at: string;
}

export interface IPromotionsAPIResponse {
  count: number;
  next: string | null;
  previous: string | null;
  results: IPromotionSlideAPI[];
}
