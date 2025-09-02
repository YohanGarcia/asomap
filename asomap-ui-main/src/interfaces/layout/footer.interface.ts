export interface FooterResponse {
    sections: {
        about: {
            title: string;
            items: Array<{
                text: string;
                to: string;
            }>;
        };
        services: {
            title: string;
            items: Array<{
                text: string;
                to: string;
            }>;
        };
    };
    company: {
        name: string;
        logo: string;
    };
}