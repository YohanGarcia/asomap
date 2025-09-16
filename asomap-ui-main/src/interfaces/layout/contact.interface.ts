// Interfaces para Contactos

export interface IContactAPI {
    id: number;
    name: string;
    url: string;
    icon: string;
    order: number;
    is_active: boolean;
    created_at: string;
    updated_at: string;
}

export interface IContactData {
    id: number;
    name: string;
    url: string;
    icon: string;
    order: number;
    isActive: boolean;
    createdAt: string;
    updatedAt: string;
}

export interface IContactResponse {
    count: number;
    next: string | null;
    previous: string | null;
    results: IContactData[];
}
