export interface ServiceInfo {
    title: string;
    description: string;
    steps: string[];
    imageUrl?: string;
    imageAlt?: string;
    pdfUrl?: string;
}

export interface Service {
    title: string;
    subtitle: string;
    bannerBg: string;
    searchPlaceholder: string;
    noResultsText: string;
    items: string[];
    itemDetails: ServiceInfo[];
    internetBankingUrl?: string;
    internetBankingButton?: string;
}

export interface AppInfo {
    title: string;
    description: string;
    imageUrl?: string;
    imageAlt?: string;
    pdfUrl?: string;
    calloutText: string;
    note: string;
    phoneNumber: string;
    paymentLink: string;
    internetBankingUrl?: string;
}