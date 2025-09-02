export interface ILoanAPI {
  id: number;
  title: string;
  description: string;
  loan_type: string;
  details: string[];
  requirements_title: string;
  requirements: string[];
  is_active: boolean;
  created_at: string;
  updated_at: string;
}

export interface ILoansAPIResponse {
  count: number;
  next: string | null;
  previous: string | null;
  results: ILoanAPI[];
}

export interface ILoanData {
  id: number;
  title: string;
  description: string;
  loanType: string;
  details: string[];
  requirementsTitle: string;
  requirements: string[];
  slug: string;
  bannerImage: string;
}

// Interfaces existentes para compatibilidad
export interface ILoan {
  type: string;
  title: string;
  image: string;
}

export interface IPersonLoan {
  title: string;
  description: string;
  image: string;
}

export interface IBanner {
  title: string;
  subtitle: string;
  imageUrl: string;
}

export interface IWhyLoan {
  title: string;
  reasons: string[];
  existingLoanTitle: string;
  existingLoanDescription: string;
  image: string;
}
