// Interfaces para la API
export interface IServiceRateAPI {
  id: number;
  service: string;
  description: string;
  rate: string;
  details: string; // HTML content from backend
}

export interface IServiceCategoryAPI {
  id: number;
  name: string;
  rates: IServiceRateAPI[];
}

export interface IServiceRatesAPI {
  id: number;
  title: string;
  description: string;
  categories: IServiceCategoryAPI[];
  is_active: boolean;
  created_at: string;
  updated_at: string;
}

export interface IServiceRatesAPIResponse {
  count: number;
  next: string | null;
  previous: string | null;
  results: IServiceRatesAPI[];
}

// Interfaces para categorías individuales
export interface IServiceCategoryAPIResponse {
  count: number;
  next: string | null;
  previous: string | null;
  results: IServiceCategoryAPI[];
}

// Interfaces transformadas para el frontend
export interface IServiceRateData {
  id: number;
  service: string;
  description: string;
  rate: string;
  details: string; // HTML content
}

export interface IServiceCategoryData {
  id: number;
  name: string;
  rates: IServiceRateData[];
}

export interface IServiceRatesData {
  title: string;
  description: string;
  categories: IServiceCategoryData[];
}
