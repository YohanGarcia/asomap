export interface IEducationItem {
    image: string;
    alt: string;
    description: string;
}

export interface IEducationSectionProps {
    data: {
        title: string;
        subtitle: string;
        educationItems: IEducationItem[];
        footerText: string;
    };
}