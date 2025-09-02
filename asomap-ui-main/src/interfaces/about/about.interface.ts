export interface AboutResponse {
    hero: {
        title: string;
        description: string;
    };
    quienesSomos: {
        title: string;
        paragraphs: string[];
        imageSrc: string;
        imageAlt: string;
    };
    nuestraHistoria: {
        title: string;
        paragraphs: string[];
        imageSrc: string;
        imageAlt: string;
    };
    mision: {
        title: string;
        description: string[] | string;
    };
    vision: {
        title: string;
        description: string[] | string;
    };
    valores: {
        title: string;
        items: Array<{
            title: string;
            description: string;
        }>;
    };
    consejoDirectores: Array<{
        name: string;
        position: string;
        imageSrc: string;
        imageAlt: string;
    }>;
}

// Removed duplicate interface - using the one from financial.interface.ts

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

export interface PoliciesResponse {
    title: string;
    description: string;
    download_text: string;
    last_update_text: string;
    all_policies_text: string;
    categories: Array<{
        title: string;
        icon: string;
        description: string;
        documents: Array<{
            title: string;
            description: string;
            url: string | null;
            lastUpdate: string;
        }>;
    }>;
} 