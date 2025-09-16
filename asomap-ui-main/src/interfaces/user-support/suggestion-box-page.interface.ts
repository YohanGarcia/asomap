// Interfaces para la API
export interface ISuggestionBoxPageAPI {
  id: number;
  title: string;
  description: string;
  is_active: boolean;
  created_at: string;
  updated_at: string;
}

export interface ISuggestionBoxPageAPIResponse {
  count: number;
  next: string | null;
  previous: string | null;
  results: ISuggestionBoxPageAPI[];
}

// Interfaces transformadas para el frontend
export interface ISuggestionBoxPageData {
  id: number;
  title: string;
  description: string;
  isActive: boolean;
  createdAt: string;
  updatedAt: string;
}
