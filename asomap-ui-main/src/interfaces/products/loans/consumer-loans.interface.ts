export interface IConsumerLoanBanner {
    title: string;
    imageUrl: string;
}

export interface IConsumerLoanBenefit {
    title: string;
    description: string;
    iconUrl: string;
}

export interface IConsumerLoanRequirement {
    text: string;
}

export interface IConsumerLoanData {
    banner: IConsumerLoanBanner;
    subtitle: string;
    benefits: IConsumerLoanBenefit[];
    requirements: {
        title: string;
        items: IConsumerLoanRequirement[];
        imageUrl: string;
    };
}