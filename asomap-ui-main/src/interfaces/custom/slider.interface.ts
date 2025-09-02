export interface SliderItemAPI {
    id: number;
    image: string;
    imageTablet?: string;
    imageMobile?: string;
    alt: string;
    sizes?: {
        mobile: string;
        tablet: string;
        desktop: string;
    };
}

export interface SliderItemAPIExtended extends SliderItemAPI {
    is_active: boolean;
    order: number;
    created_at: string;
    updated_at: string;
}

export interface SliderResponse {
    count: number;
    next: string | null;
    previous: string | null;
    results: SliderItemAPIExtended[];
} 