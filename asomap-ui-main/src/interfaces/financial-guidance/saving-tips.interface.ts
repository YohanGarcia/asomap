export interface ISavingTipAPI {
  id: number;
  title: string;
  description: string;
  content: string;
  link: string;
  order: number;
  is_active: boolean;
  created_at: string;
  updated_at: string;
}

export interface ISavingTipsAPIResponse {
  count: number;
  next: string | null;
  previous: string | null;
  results: ISavingTipAPI[];
}

export interface ISavingTipData {
  id: number;
  title: string;
  description: string;
  content: string;
  link: string;
  order: number;
}

export interface ISliderSlideAPI {
  id: number;
  image_url: string;
  title?: string;
  description?: string;
  order: number;
  is_active: boolean;
  created_at: string;
  updated_at: string;
}

export interface ISliderSlidesAPIResponse {
  count: number;
  next: string | null;
  previous: string | null;
  results: ISliderSlideAPI[];
}

export interface ISliderSlideData {
  id: number;
  image: string;
  title?: string;
  description?: string;
}

export interface IFAQItemAPI {
  id: number;
  question: string;
  answer: string;
  order: number;
  is_active: boolean;
  created_at: string;
  updated_at: string;
}

export interface IFAQAPIResponse {
  count: number;
  next: string | null;
  previous: string | null;
  results: IFAQItemAPI[];
}

export interface IFAQItemData {
  id: number;
  question: string;
  answer: string;
  order: number;
}

export interface ISavingTipsPageData {
  tips: ISavingTipData[];
  sliderSlides: ISliderSlideData[];
  faqItems: IFAQItemData[];
  pageTitle: string;
  pageDescription: string;
}
