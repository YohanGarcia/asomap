// Interfaces para la API
export interface IClaimRequestPageAPI {
  id: number;
  title: string;
  description: string;
  is_active: boolean;
  created_at: string;
  updated_at: string;
}

export interface IClaimRequestPageAPIResponse {
  count: number;
  next: string | null;
  previous: string | null;
  results: IClaimRequestPageAPI[];
}

// Interfaces transformadas para el frontend
export interface IClaimRequestPageData {
  id: number;
  title: string;
  description: string;
  isActive: boolean;
  createdAt: string;
  updatedAt: string;
}
