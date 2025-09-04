import { API_CONFIG } from '@/api/config/config';

/**
 * Utility functions for environment management
 */

// Debug logging (only in development)
export const debugLog = (message: string, data?: any) => {
    if (API_CONFIG.FEATURES.DEBUG_LOGS) {
        console.log(`🔍 [DEBUG] ${message}`, data || '');
    }
};

// Error logging with environment awareness
export const errorLog = (message: string, error?: any) => {
    if (API_CONFIG.IS_DEVELOPMENT) {
        console.error(`❌ [ERROR] ${message}`, error || '');
    } else if (API_CONFIG.FEATURES.ERROR_REPORTING) {
        // En producción, enviar a servicio de reporting
        console.error(`❌ [ERROR] ${message}`);
        // TODO: Implementar servicio de error reporting (Sentry, etc.)
    }
};

// Check if we should use mock data
export const shouldUseMockData = () => {
    return API_CONFIG.FEATURES.MOCK_DATA;
};

// Get appropriate API URL
export const getApiUrl = (endpoint: string) => {
    const baseUrl = API_CONFIG.BASE_URL;
    const cleanEndpoint = endpoint.startsWith('/') ? endpoint : `/${endpoint}`;
    return `${baseUrl}${cleanEndpoint}`;
};

// Convert relative image URLs to absolute backend URLs
export const getImageUrl = (relativePath: string) => {
    if (!relativePath) return '';
    
    // If it's already an absolute URL, return as is
    if (relativePath.startsWith('http://') || relativePath.startsWith('https://')) {
        return relativePath;
    }
    
    // Remove leading slash if present
    const cleanPath = relativePath.startsWith('/') ? relativePath.slice(1) : relativePath;
    
    // Use Vite environment variables for media URL
    const mediaBaseUrl = import.meta.env.VITE_MEDIA_BASE_URL || API_CONFIG.BASE_URL.replace('/api', '');
    
    return `${mediaBaseUrl}/${cleanPath}`;
};

// Environment-specific configurations
export const getEnvironmentConfig = () => {
    return {
        isDevelopment: API_CONFIG.IS_DEVELOPMENT,
        isProduction: API_CONFIG.IS_PRODUCTION,
        isStaging: API_CONFIG.IS_STAGING,
        baseUrl: API_CONFIG.BASE_URL,
        timeout: API_CONFIG.TIMEOUT,
        features: API_CONFIG.FEATURES,
        serverIP: import.meta.env.VITE_SERVER_IP,
        serverPort: import.meta.env.VITE_SERVER_PORT,
        nginxUrl: import.meta.env.VITE_NGINX_URL,
        backendUrl: import.meta.env.VITE_BACKEND_URL,
        mediaBaseUrl: import.meta.env.VITE_MEDIA_BASE_URL
    };
};

// Feature flag checker
export const isFeatureEnabled = (feature: keyof typeof API_CONFIG.FEATURES) => {
    return API_CONFIG.FEATURES[feature];
};
