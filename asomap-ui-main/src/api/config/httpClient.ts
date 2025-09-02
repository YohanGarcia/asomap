import { API_CONFIG } from '@api';

interface ApiResponse<T> {
    status: number;
    data: T;
    message?: string;
}

class HttpError extends Error {
    constructor(
        public status: number,
        public message: string,
        public data?: unknown
    ) {
        super(message);
        this.name = 'HttpError';
    }
}

async function handleResponse<T>(response: Response): Promise<ApiResponse<T>> {
    const data = await response.json();

    if (!response.ok) {
        throw new HttpError(
            response.status,
            data.message || 'Ha ocurrido un error',
            data
        );
    }

    return {
        status: response.status,
        data: data as T,
        message: data.message
    };
}

export const httpClient = {
    get: async <T>(endpoint: string): Promise<ApiResponse<T>> => {
        try {
            const response = await fetch(`${API_CONFIG.BASE_URL}${endpoint}`, {
                method: 'GET',
                headers: API_CONFIG.HEADERS,
            });
            return handleResponse<T>(response);
        } catch (error) {
            if (error instanceof HttpError) {
                throw error;
            }
            throw new HttpError(500, 'Error de conexión');
        }
    },

    post: async <T, D extends Record<string, unknown>>(endpoint: string, data: D): Promise<ApiResponse<T>> => {
        try {
            const response = await fetch(`${API_CONFIG.BASE_URL}${endpoint}`, {
                method: 'POST',
                headers: API_CONFIG.HEADERS,
                body: JSON.stringify(data)
            });
            return handleResponse<T>(response);
        } catch (error) {
            if (error instanceof HttpError) {
                throw error;
            }
            throw new HttpError(500, 'Error de conexión');
        }
    },

    put: async <T, D extends Record<string, unknown>>(endpoint: string, data: D): Promise<ApiResponse<T>> => {
        try {
            const response = await fetch(`${API_CONFIG.BASE_URL}${endpoint}`, {
                method: 'PUT',
                headers: API_CONFIG.HEADERS,
                body: JSON.stringify(data)
            });
            return handleResponse<T>(response);
        } catch (error) {
            if (error instanceof HttpError) {
                throw error;
            }
            throw new HttpError(500, 'Error de conexión');
        }
    },

    delete: async <T>(endpoint: string): Promise<ApiResponse<T>> => {
        try {
            const response = await fetch(`${API_CONFIG.BASE_URL}${endpoint}`, {
                method: 'DELETE',
                headers: API_CONFIG.HEADERS,
            });
            return handleResponse<T>(response);
        } catch (error) {
            if (error instanceof HttpError) {
                throw error;
            }
            throw new HttpError(500, 'Error de conexión');
        }
    }
};