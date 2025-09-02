export interface PoliciesResponse {
    title: string;
    description: string;
    downloadText: string;
    lastUpdateText: string;
    allPoliciesText: string;
    categories: Array<{
        title: string;
        icon: string;
        description: string;
        documents: Array<{
            title: string;
            description: string;
            url: string;
            lastUpdate: string;
        }>;
    }>;
} 