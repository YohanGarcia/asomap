import { ENDPOINTS } from '@/constants';
import { AboutResponse } from '@/interfaces';
import { debugLog, errorLog, getApiUrl, getImageUrl } from '@/utils/environment';

// Función helper para extraer datos de respuesta paginada
const extractData = (response: any): any => {
    // Si la respuesta tiene estructura paginada (count, results, etc.)
    if (response && typeof response === 'object' && 'results' in response) {
        // Si results es un array, devolver el array completo
        if (Array.isArray(response.results)) {
            return response.results;
        }
        // Si results es un objeto directo
        return response.results;
    }
    // Si la respuesta es directa (sin paginación)
    return response;
};

export const aboutService = {
    getAbout: async (): Promise<AboutResponse> => {
            try {
        const [
            heroResponse,
            quienesSomosResponse,
            historiaResponse,
            misionResponse,
            visionResponse,
            valoresResponse,
        ] = await Promise.all([
            fetch(getApiUrl(ENDPOINTS.COLLECTIONS.ABOUT.HERO)),
            fetch(getApiUrl(ENDPOINTS.COLLECTIONS.ABOUT.ABOUT_US)),
            fetch(getApiUrl(ENDPOINTS.COLLECTIONS.ABOUT.OUR_HISTORY)),
            fetch(getApiUrl(ENDPOINTS.COLLECTIONS.ABOUT.MISION)),
            fetch(getApiUrl(ENDPOINTS.COLLECTIONS.ABOUT.VISION)),
            fetch(getApiUrl(ENDPOINTS.COLLECTIONS.ABOUT.VALUES)),
        ]);

        // Obtener todas las páginas del consejo de directores
        const getAllConsejoDirectores = async () => {
            const allDirectores = [];
            let nextUrl = getApiUrl(ENDPOINTS.COLLECTIONS.ABOUT.DIRECTOR_BOARD);
            
            while (nextUrl) {
                const response = await fetch(nextUrl);
                const data = await response.json();
                
                if (data.results && Array.isArray(data.results)) {
                    allDirectores.push(...data.results);
                }
                
                nextUrl = data.next || null;
            }
            
            // Ordenar por ID para mantener el orden correcto
            return allDirectores.sort((a, b) => a.id - b.id);
        };

        const consejo = await getAllConsejoDirectores();

                    const [heroRaw, quienesSomosRaw, historiaRaw, misionRaw, visionRaw, valoresRaw] = await Promise.all([
            heroResponse.json(),
            quienesSomosResponse.json(),
            historiaResponse.json(),
            misionResponse.json(),
            visionResponse.json(),
            valoresResponse.json(),
        ]);

            // Debug logs
            debugLog('[AboutService] Raw historia response:', historiaRaw);
            debugLog('[AboutService] Raw quienesSomos response:', quienesSomosRaw);

            // Extraer datos de las respuestas paginadas
            const hero = extractData(heroRaw);
            const quienesSomos = extractData(quienesSomosRaw);
            const historia = extractData(historiaRaw);
            const mision = extractData(misionRaw);
            const vision = extractData(visionRaw);
            const valores = extractData(valoresRaw);
            // consejo ya está procesado y ordenado arriba

            // Para endpoints que devuelven un solo elemento, tomar el primero
            const heroData = Array.isArray(hero) ? hero[0] : hero;
            const quienesSomosData = Array.isArray(quienesSomos) ? quienesSomos[0] : quienesSomos;
            const historiaData = Array.isArray(historia) ? historia[0] : historia;
            const misionData = Array.isArray(mision) ? mision[0] : mision;
            const visionData = Array.isArray(vision) ? vision[0] : vision;
            // Para valores, usar el array completo
            const valoresData = valores; // Mantener el array completo

            // Debug logs
            debugLog('[AboutService] Extracted historia:', historiaData);
            debugLog('[AboutService] Extracted quienesSomos:', quienesSomosData);
            debugLog('[AboutService] Extracted valores:', valoresData);
            debugLog('[AboutService] Consejo ordenado por ID:', consejo.map(d => ({ id: d.id, name: d.name, position: d.position })));

            const result = {
                hero: {
                    title: heroData?.title || heroData?.Title || '',
                    description: heroData?.description || heroData?.Description || '',
                },
                quienesSomos: {
                    title: quienesSomosData?.title || quienesSomosData?.Title || '',
                    paragraphs: quienesSomosData?.paragraphs || quienesSomosData?.Paragraphs || [],
                    imageSrc: getImageUrl(quienesSomosData?.image_src || quienesSomosData?.ImageSrc || ''),
                    imageAlt: quienesSomosData?.image_alt || quienesSomosData?.ImageAlt || '',
                },
                nuestraHistoria: {
                    title: historiaData?.title || historiaData?.Title || '',
                    paragraphs: historiaData?.paragraphs || historiaData?.Paragraphs || [],
                    imageSrc: getImageUrl(historiaData?.image_src || historiaData?.ImageSrc || ''),
                    imageAlt: historiaData?.image_alt || historiaData?.ImageAlt || '',
                },
                mision: {
                    title: misionData?.title || misionData?.Title || '',
                    description: misionData?.description || misionData?.Description || [],
                },
                vision: {
                    title: visionData?.title || visionData?.Title || '',
                    description: visionData?.description || visionData?.Description || [],
                },
                valores: {
                    title: "Nuestros Valores",
                    items: Array.isArray(valoresData) 
                        ? valoresData.map((valor: any) => ({
                            title: valor.title || valor.Title || '',
                            description: valor.description || valor.Description || '',
                            icon: "FaPeopleArrows" // Icono por defecto
                        }))
                        : [],
                },
                consejoDirectores: Array.isArray(consejo) 
                    ? consejo.map((director: { name?: string; position?: string; image_src?: string; image_alt?: string; Name?: string; Position?: string; ImageSrc?: string; ImageAlt?: string }) => ({
                        name: director.name || director.Name || '',
                        position: director.position || director.Position || '',
                        imageSrc: getImageUrl(director.image_src || director.ImageSrc || ''),
                        imageAlt: director.image_alt || director.ImageAlt || '',
                    }))
                    : [],
            };

            // Debug logs
            console.log('🔍 [AboutService] Final nuestraHistoria:', result.nuestraHistoria);
            console.log('🔍 [AboutService] Final quienesSomos:', result.quienesSomos);

            return result;
        } catch (error) {
            errorLog('[AboutService] Error fetching about data:', error);
            throw new Error('Failed to fetch about data');
        }
    }
};