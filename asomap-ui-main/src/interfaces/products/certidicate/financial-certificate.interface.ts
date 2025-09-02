export interface BenefitItem {
    title: string;
    description: string;
}

export interface DepositRate {
    range: string;
    rate: string;
    term: string;
}

export interface FinancialCertificateData {
    banner: {
        imageUrl: string;
    };
    mainTitle: string;
    subtitle: string;
    cta: {
        apply: string;
        rates: string;
    };
    benefits: {
        title: string;
        items: BenefitItem[];
    };
    investment: {
        title: string;
        subtitle: string;
        details: string[];
        imageUrl: string;
    };
    rates: {
        title: string;
        items: { label: string; value: string }[];
    };
    requirements: {
        title: string;
        items: string[];
    };
    faq: {
        title: string;
        items: { question: string; answer: string }[];
    };
    depositRates: {
        title: string;
        items: DepositRate[];
        validFrom: string;
    };
}