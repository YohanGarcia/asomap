// Interfaces para el formulario
export interface IFraudReportFormData {
  classification: string;
  fullName: string;
  document: string;
  phone: string;
  email: string;
  file: File | null;
  message: string;
}

// Interfaces para la respuesta del backend
export interface IFraudReportAPI {
  id: number;
  title: string;
  description: string;
  email: string;
  form: {
    sections: {
      personalInfo: {
        title: string;
        fields: Array<{
          id: string;
          label: string;
          type: string;
          placeholder: string;
          required: boolean;
          options?: string[];
          accept?: string;
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

export interface IFraudReportAPIResponse {
  count: number;
  next: string | null;
  previous: string | null;
  results: IFraudReportAPI[];
}

// Interfaces transformadas para el frontend
export interface IFraudReportData {
  id: number;
  title: string;
  description: string;
  email: string;
  form: {
    sections: {
      personalInfo: {
        title: string;
        fields: Array<{
          id: string;
          label: string;
          type: string;
          placeholder: string;
          required: boolean;
          options?: string[];
          accept?: string;
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
export interface ISubmitFraudReport {
  classification: string;
  fullName: string;
  document: string;
  phone: string;
  email: string;
  file: File | null;
  message: string;
  [key: string]: unknown;
}
