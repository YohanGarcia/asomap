export interface IAccountBenefit {
  icon: string;
  text: string;
}

export interface IAccountAPI {
  id: number;
  title: string;
  description: string;
  bannerImage: string | null;
  accountImage: string | null;
  category: string;
  features: string[];
  requirements: string[];
  benefits: IAccountBenefit[];
  is_active: boolean;
  created_at: string;
  updated_at: string;
}

export interface IAccountsAPIResponse {
  count: number;
  next: string | null;
  previous: string | null;
  results: IAccountAPI[];
}

// Interfaz para el componente que consume los datos
export interface IAccountData {
  id: number;
  title: string;
  description: string;
  bannerImage: string;
  accountImage: string;
  category: string;
  features: string[];
  requirements: string[];
  benefits: IAccountBenefit[];
}
