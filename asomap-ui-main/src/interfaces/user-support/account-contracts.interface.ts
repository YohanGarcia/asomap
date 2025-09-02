export interface IContractAPI {
  title: string;
  url: string;
  category: string;
}

export interface IAccountContractsAPI {
  id: number;
  title: string;
  description: string;
  contracts: IContractAPI[];
  categories: string[];
  is_active: boolean;
  created_at: string;
  updated_at: string;
}

export interface IAccountContractsAPIResponse {
  count: number;
  next: string | null;
  previous: string | null;
  results: IAccountContractsAPI[];
}

// Interfaces transformadas para el frontend
export interface IContractData {
  title: string;
  url: string;
  category: string;
}

export interface IAccountContractsData {
  id: number;
  title: string;
  description: string;
  contracts: IContractData[];
  categories: string[];
}
