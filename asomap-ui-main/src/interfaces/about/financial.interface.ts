export interface FinancialStatementsResponse {
    title: string;
    description: string;
    years: Array<{
        year: string;
        documents: {
            audited: Array<{
                title: string;
                url: string;
            }>;
            quarterly: Array<{
                title: string;
                url: string;
                quarter: string;
            }>;
        };
    }>;
} 