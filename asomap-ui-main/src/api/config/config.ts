// API Configuration
const ENV = import.meta.env.VITE_ENV || 'development';

export const API_CONFIG = {
    // Environment
    ENV,
    IS_DEVELOPMENT: ENV === 'development',
    IS_PRODUCTION: ENV === 'production',
    IS_STAGING: ENV === 'staging',
    IS_MOCK: ENV === 'mock',
    
    // API URLs based on environment
    BASE_URL: ENV === 'development' 
        ? 'http://localhost:8080/api'
        : import.meta.env.VITE_API_URL || 'https://api.asomap.com/api',
    
    // Timeouts
    TIMEOUT: ENV === 'development' ? 10000 : 60000, // Aumentar timeout en producción
    
    // Headers
    HEADERS: {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    },
    
    // External APIs
    GOOGLE_MAPS_API_KEY: import.meta.env.VITE_GOOGLE_MAPS_API_KEY,
    
    // Feature flags
    FEATURES: {
        DEBUG_LOGS: ENV === 'development',
        MOCK_DATA: ENV === 'development' || ENV === 'mock',
        ANALYTICS: ENV === 'production',
        ERROR_REPORTING: ENV === 'production'
    }
} as const;

// Debug information (always show in production for debugging)
console.log('🚀 ASOMAP API Configuration:', {
    environment: API_CONFIG.ENV,
    baseUrl: API_CONFIG.BASE_URL,
    timeout: API_CONFIG.TIMEOUT,
    features: API_CONFIG.FEATURES,
    googleMapsApiKey: API_CONFIG.GOOGLE_MAPS_API_KEY ? '✅ Configured' : '❌ Missing',
    viteApiUrl: import.meta.env.VITE_API_URL || 'Not set'
});
