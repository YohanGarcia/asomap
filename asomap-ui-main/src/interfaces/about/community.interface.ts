export interface CommunitySupportResponse {
    data: {
        title: string;
        description: string;
        categories: Array<{
            id: string;
            name: string;
            icon: string;
            description: string;
        }>;
        initiatives: Array<{
            id: string;
            title: string;
            description: string;
            impact: string;
            imageUrl: string;
            category: string;
        }>;
    };
} 