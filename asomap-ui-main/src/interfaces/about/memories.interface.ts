export interface MemoriesResponse {
    title: string;
    description: string;
    years: Array<{
        year: string;
        documents: Array<{
            url: string;
        }>;
    }>;
} 