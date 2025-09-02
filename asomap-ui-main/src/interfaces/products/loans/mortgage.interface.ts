export interface IBannerData {
    imageUrl: string;
}

export interface ILoanOption {
    title: string;
    image: string;
    details: string[];
}

export interface IMortgageLoansData {
    bannerData: IBannerData;
    loansData: ILoanOption[];
    requirements: {
        image: string;
        items: string[];
    };
}