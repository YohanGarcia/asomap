export interface ICertificateBenefit {
  title: string;
  description: string;
}

export interface ICertificateBenefits {
  title: string;
  items: ICertificateBenefit[];
}

export interface ICertificateInvestment {
  title: string;
  subtitle: string;
  details: string[];
  imageUrl: string;
}

export interface ICertificateRate {
  label: string;
  value: string;
}

export interface ICertificateRates {
  title: string;
  items: ICertificateRate[];
}

export interface ICertificateRequirements {
  title: string;
  items: string[];
}

export interface ICertificateDepositRate {
  range: string;
  rate: string;
  term: string;
}

export interface ICertificateDepositRates {
  title: string;
  items: ICertificateDepositRate[];
  validFrom: string;
}

export interface ICertificateFAQ {
  question: string;
  answer: string;
}

export interface ICertificateFAQSection {
  title: string;
  items: ICertificateFAQ[];
}

export interface ICertificateAPI {
  id: number;
  title: string;
  subtitle: string;
  description: string;
  bannerImage: string | null;
  certificateImage: string | null;
  certificate_type: string;
  cta_apply: string;
  cta_rates: string;
  benefits_title: string;
  benefits: ICertificateBenefits;
  investment_title: string;
  investment_subtitle: string;
  investment: ICertificateInvestment;
  rates_title: string;
  rates: ICertificateRates;
  requirements_title: string;
  requirements: ICertificateRequirements;
  deposit_rates_title: string;
  depositRates: ICertificateDepositRates;
  deposit_rates_valid_from: string;
  faq_title: string;
  faq: ICertificateFAQSection;
  slug: string;
  is_active: boolean;
  created_at: string;
  updated_at: string;
}

export interface ICertificatesAPIResponse {
  count: number;
  next: string | null;
  previous: string | null;
  results: ICertificateAPI[];
}

export interface ICertificateData {
  id: number;
  title: string;
  subtitle: string;
  description: string;
  bannerImage: string;
  certificateImage: string;
  certificateType: string;
  ctaApply: string;
  ctaRates: string;
  benefits: ICertificateBenefits;
  investment: ICertificateInvestment;
  rates: ICertificateRates;
  requirements: ICertificateRequirements;
  depositRates: ICertificateDepositRates;
  faq: ICertificateFAQSection;
  slug: string;
}
