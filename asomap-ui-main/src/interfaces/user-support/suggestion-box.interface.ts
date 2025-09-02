// Interfaces para la API de provincias
export interface IProvinceAPI {
  id: number;
  name: string;
}

export interface IProvincesAPIResponse {
  count: number;
  next: string | null;
  previous: string | null;
  results: IProvinceAPI[];
}

// Interfaces transformadas para el frontend
export interface IProvinceData {
  id: number;
  name: string;
}

// Interfaces para el formulario (mantener estructura actual)
export interface ISuggestionBoxFormData {
  classification: string;
  fullName: string;
  document: string;
  phone: string;
  email: string;
  province: string;
  message: string;
}

export interface ISubmitSuggestionBox {
  classification: string;
  fullName: string;
  document: string;
  phone: string;
  email: string;
  province: string | number;
  message: string;
  [key: string]: unknown;
}
