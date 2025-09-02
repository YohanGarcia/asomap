import { ReactNode } from 'react';
export interface IComercialBenefit {
    title: string;
    description: string;
    image: string;
}

export interface IRequirement {
    image: string | undefined;
    title: string;
    items: string[];
}

export interface ICommercialLoansData {
    subtitle: ReactNode;
    banner: unknown;
    bannerData: {
        title: ReactNode;
        imageUrl: string;
    };
    title: string;
    description: string;
    buttons: {
        primary: string;
        secondary: string;
    };
    benefitsTitle: string;
    benefitsDescription: string;
    benefits: IComercialBenefit[];
    requirements: IRequirement;
    familyImageUrl: string;
}