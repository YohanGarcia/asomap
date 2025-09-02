import { httpClient } from '../../config/httpClient';
import { ENDPOINTS } from '@/constants';
import type { Location, LocationsResponse } from '@/interfaces';
import { debugLog, errorLog } from '@/utils/environment';
import { locations } from '@/mocks/locations/locationsData';

// Función para verificar si está abierto ahora
const isOpenNow = (hours: { openingTime: string; closingTime: string }) => {
    const now = new Date();
    const day = now.getDay(); // 0 (domingo) - 6 (sábado)

    // Definir horarios
    const openingHour = new Date();
    const closingHour = new Date();

    const [openingHourString, openingPeriod] = hours.openingTime.split(" ");
    const [closingHourString, closingPeriod] = hours.closingTime.split(" ");

    openingHour.setHours(parseInt(openingHourString), 0);
    closingHour.setHours(parseInt(closingHourString), 0);

    // Ajustar según el periodo AM/PM
    if (openingPeriod === 'PM' && openingHour.getHours() < 12) openingHour.setHours(openingHour.getHours() + 12);
    if (closingPeriod === 'PM' && closingHour.getHours() < 12) closingHour.setHours(closingHour.getHours() + 12);

    // Verifica si es sábado (6) o lunes a viernes (1-5)
    if (day >= 1 && day <= 5) {
        // De lunes a viernes: 8:30 AM - 5 PM
        return now >= openingHour && now < closingHour;
    } else if (day === 6) {
        // Sábado: 8:30 AM - 12:30 PM
        const saturdayOpeningTime = new Date(openingHour);
        saturdayOpeningTime.setHours(8, 30); // 8:30 AM
        const saturdayClosingTime = new Date();
        saturdayClosingTime.setHours(12, 30); // 12:30 PM
        return now >= saturdayOpeningTime && now < saturdayClosingTime;
    } else {
        // Domingo: Cerrado
        return false;
    }
}

// Función para obtener texto del horario
const getScheduleText = (type: 'branch' | 'atm', hours?: { openingTime: string; closingTime: string }) => {
    if (type === 'atm') {
        return {
            availability: '24/7',
            scheduleText: 'Disponible 24/7 ',
            availabilityClass: 'bg-green-100 text-green-700'
        };
    }

    return {
        scheduleText: `Lunes a viernes ${hours?.openingTime} - ${hours?.closingTime}\nSábado 8:30 - 13:00`,
        availabilityClass: hours?.openingTime ? 'bg-yellow-100 text-yellow-700' : ''
    };
};

export const locationsService = {
    getLocations: async (): Promise<Location[]> => {
        try {
            debugLog('[LocationsService] Fetching from backend');
            const response = await httpClient.get<LocationsResponse>(
                ENDPOINTS.COLLECTIONS.LOCATIONS.ALL
            );
            
            debugLog('[LocationsService] Backend response received successfully:', response.data);
            debugLog('[LocationsService] Response count:', response.data.count);
            debugLog('[LocationsService] Response results length:', response.data.results?.length);
            
            // Validar que results existe y es un array
            if (!response.data.results || !Array.isArray(response.data.results)) {
                debugLog('[LocationsService] No results found or results is not an array');
                return [];
            }
            
            // Transformar la respuesta de la API al formato esperado
            const transformedLocations: Location[] = response.data.results.map(location => {
                const scheduleInfo = getScheduleText(location.type, location.hours);
                const isCurrentlyOpen = location.hours ? isOpenNow(location.hours) : false;
                
                return {
                    id: location.id.toString(),
                    type: location.type,
                    name: location.name,
                    address: location.address,
                    phone: location.phone,
                    hours: location.hours,
                    coordinates: location.coordinates,
                    isOpen: isCurrentlyOpen,
                    services: location.services,
                    scheduleText: scheduleInfo.scheduleText,
                    availabilityClass: scheduleInfo.availabilityClass
                };
            });
            
            debugLog('[LocationsService] Transformed locations count:', transformedLocations.length);
            debugLog('[LocationsService] Transformed locations:', transformedLocations);
            return transformedLocations;
            
        } catch (error) {
            errorLog('[LocationsService] Error fetching locations data:', error);
            
            // Solo usar mock si es un error de red real (no 404)
            if (error instanceof TypeError || (error instanceof Error && error.message.includes('fetch'))) {
                debugLog('[LocationsService] Network error, using mock data as fallback');
                return locations;
            }
            
            // Para otros errores (404, 500, etc.), usar mock data como fallback
            debugLog('[LocationsService] API error, using mock data as fallback');
            return locations;
        }
    }
};
