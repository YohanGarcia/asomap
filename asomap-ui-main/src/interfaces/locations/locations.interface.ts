export interface Location {
    id: string;
    type: 'branch' | 'atm';
    name: string;
    address: string;
    phone?: string;
    hours?: {
        openingTime: string;
        closingTime: string;
    };
    coordinates: { lat: number; lng: number };
    isOpen?: boolean;
    distance?: number;
    services?: string[];
    scheduleText?: string;
    availabilityClass?: string;
}

export interface LocationAPI {
    id: number;
    type: 'branch' | 'atm';
    name: string;
    address: string;
    phone: string;
    coordinates: { lat: number; lng: number };
    hours: {
        openingTime: string;
        closingTime: string;
    };
    is_open: boolean;
    services: string[];
}

export interface LocationsResponse {
    count: number;
    next: string | null;
    previous: string | null;
    results: LocationAPI[];
}
