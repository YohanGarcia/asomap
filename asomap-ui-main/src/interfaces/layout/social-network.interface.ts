// Interfaces para Redes Sociales

export interface ISocialNetworkAPI {
    id: number;
    name: string;
    url: string;
    icon: string;
    order: number;
    is_active: boolean;
    created_at: string;
    updated_at: string;
}

export interface ISocialNetworkData {
    id: number;
    name: string;
    url: string;
    icon: string;
    order: number;
    isActive: boolean;
    createdAt: string;
    updatedAt: string;
}

export interface ISocialNetworkResponse {
    count: number;
    next: string | null;
    previous: string | null;
    results: ISocialNetworkData[];
}
