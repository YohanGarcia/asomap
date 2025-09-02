export interface IAccountTypeAPI {
  id: number;
  label: string;
  description: string;
}

export interface IDocumentAPI {
  title: string;
  url: string;
  date: string;
  type: string;
}

export interface IYearAPI {
  year: string;
  documents: {
    [key: string]: IDocumentAPI;
  };
}

export interface IAbandonedAccountsAPI {
  id: number;
  title: string;
  description: string;
  account_types: IAccountTypeAPI[];
  years: IYearAPI[];
  is_active: boolean;
  created_at: string;
  updated_at: string;
}

export interface IAbandonedAccountsAPIResponse {
  count: number;
  next: string | null;
  previous: string | null;
  results: IAbandonedAccountsAPI[];
}

// Interfaces transformadas para el frontend
export interface IAccountTypeData {
  id: number;
  label: string;
  description: string;
}

export interface IDocumentData {
  title: string;
  url: string;
  date: string;
}

export interface IYearData {
  year: string;
  documents: {
    abandoned: IDocumentData;
    inactive: IDocumentData;
  };
}

export interface IAbandonedAccountsData {
  id: number;
  title: string;
  description: string;
  accountTypes: IAccountTypeData[];
  years: IYearData[];
}
