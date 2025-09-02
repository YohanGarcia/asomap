export interface IProduct {
    id: string;
    title: string;
    description: string;
    image: string;
    category: string;
    imageWidth: number;
    imageHeight: number;
}

export interface IProductsProps {
    products: IProduct[];
}

export interface IProductSectionData {
    section: {
        title: string;
        subtitle: string;
    };
    buttonText: string;
    products: IProduct[];
}

export interface IProductSectionResponse {
    data: IProductSectionData;
}