// Interfaces para la API
export interface IFraudReportPageAPI {
  id: number;
  title: string;
  description: string;
  is_active: boolean;
  created_at: string;
  updated_at: string;
}

export interface IFraudReportPageAPIResponse {
  count: number;
  next: string | null;
  previous: string | null;
  results: IFraudReportPageAPI[];
}

// Interfaces transformadas para el frontend
export interface IFraudReportPageData {
  id: number;
  title: string;
  description: string;
  isActive: boolean;
  createdAt: string;
  updatedAt: string;
}
