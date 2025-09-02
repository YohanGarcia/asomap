// Interfaces para la API
export interface IImageAPI {
  id: number;
  src: string;
  alt_text: string;
  description: string;
}

export interface ISectionAPI {
  id: string;
  title: string;
  description: string;
  button_text: string;
  additional_info: string;
  images: IImageAPI[];
}

export interface IRightsAndDutiesAPI {
  id: number;
  pageTitle: string;
  pageDescription: string;
  sections: ISectionAPI[];
  is_active: boolean;
  created_at: string;
  updated_at: string;
}

export interface IRightsAndDutiesAPIResponse {
  count: number;
  next: string | null;
  previous: string | null;
  results: IRightsAndDutiesAPI[];
}

// Interfaces transformadas para el frontend
export interface IImageData {
  id: number;
  src: string;
  alt: string;
  description: string;
}

export interface ISectionData {
  id: string;
  title: string;
  description: string;
  buttonText: string;
  additionalInfo: string;
  images: IImageData[];
}

export interface IRightsAndDutiesData {
  pageTitle: string;
  pageDescription: string;
  sections: ISectionData[];
}
