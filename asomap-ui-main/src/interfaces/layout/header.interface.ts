// Interfaces para el Header
export interface NavigationResponse {
    individual: string;
    empresarial: string;
}

// Interfaces para Exchange Rate
export interface ExchangeRate {
    currency: string;
    buyRate: number;
    sellRate: number;
}

export interface ExchangeRateResponse {
    base: string;
    lastUpdated: string;
    showBuyRate: boolean;
    showSellRate: boolean;
    rates: ExchangeRate[];
}

export interface ExchangeRateAPIResponse {
    id: number;
    rates: ExchangeRate[];
    showBuyRate: boolean;
    showSellRate: boolean;
    lastUpdated: string;
    is_active: boolean;
    created_at: string;
    updated_at: string;
}

export interface HeaderResponse {
    navigation: NavigationResponse;
    exchange: ExchangeRateResponse;
}

