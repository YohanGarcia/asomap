// Interfaces para la API
export interface IServiceInfoAPI {
  id: number;
  title: string;
  description: string;
  steps: string;
  image_url: string | null;
  image_alt: string | null;
  pdf_url: string | null;
}

export interface IServicesPageAPI {
  id: number;
  title: string;
  subtitle: string;
  search_placeholder: string;
  no_results_text: string;
  internet_banking_url: string;
  internet_banking_button: string;
  items: string[];
  item_details: IServiceInfoAPI[];
  is_active: boolean;
  created_at: string;
  updated_at: string;
}

export interface IServicesPageAPIResponse {
  count: number;
  next: string | null;
  previous: string | null;
  results: IServicesPageAPI[];
}

// Interfaces transformadas para el frontend
export interface IServiceInfoData {
  id: number;
  title: string;
  description: string;
  steps: string;
  imageUrl: string | null;
  imageAlt: string | null;
  pdfUrl: string | null;
}

export interface IServicesPageData {
  title: string;
  subtitle: string;
  searchPlaceholder: string;
  noResultsText: string;
  internetBankingUrl: string;
  internetBankingButton: string;
  items: string[];
  itemDetails: IServiceInfoData[];
}
