// Interfaces para el formulario
export interface IClaimRequestFormData {
  fullName: string;
  document: string;
  phone: string;
  email: string;
  productType: string;
  claimType: string;
  distributionChannel: string;
  message: string;
}

// Interfaces para la respuesta del backend
export interface IClaimRequestAPI {
  id: number;
  title: string;
  description: string;
  email: string;
  form: {
    sections: {
      personalInfo: {
        title: string;
        fields: Array<{
          label: string;
          placeholder: string;
          options?: string[];
        }>;
      };
    };
  };
  validation: {
    document: {
      cedula: RegExp;
      pasaporte: RegExp;
      rnc: RegExp;
    };
    phone: RegExp;
  };
  is_active: boolean;
  created_at: string;
  updated_at: string;
}

export interface IClaimRequestAPIResponse {
  count: number;
  next: string | null;
  previous: string | null;
  results: IClaimRequestAPI[];
}

// Interfaces transformadas para el frontend
export interface IClaimRequestData {
  id: number;
  title: string;
  description: string;
  email: string;
  form: {
    sections: {
      personalInfo: {
        title: string;
        fields: Array<{
          label: string;
          placeholder: string;
          options?: string[];
        }>;
      };
    };
  };
  validation: {
    document: {
      cedula: RegExp;
      pasaporte: RegExp;
      rnc: RegExp;
    };
    phone: RegExp;
  };
}

// Interface para enviar el formulario
export interface ISubmitClaimRequest {
  fullName: string;
  document: string;
  phone: string;
  email: string;
  productType: string;
  claimType: string;
  distributionChannel: string;
  message: string;
  [key: string]: unknown;
}
