import { httpClient } from '../../config/httpClient';
import { API_CONFIG } from '../../config/config';
import { ENDPOINTS } from '@/constants';
import { debugLog, errorLog } from '@/utils/environment';
import type { ICertificatesAPIResponse, ICertificateData } from '@/interfaces';

export const certificatesService = {
  getAllCertificates: async (): Promise<ICertificateData[]> => {
    try {
      debugLog('[CertificatesService] Fetching all certificates');
      
      const response = await httpClient.get<ICertificatesAPIResponse>(ENDPOINTS.COLLECTIONS.PRODUCTS.CERTIFICATES);
      
      // Filtrar solo certificados activos y transformar datos
      const certificates: ICertificateData[] = response.data.results
        .filter(certificate => certificate.is_active)
        .map(certificate => ({
          id: certificate.id,
          title: certificate.title,
          subtitle: certificate.subtitle,
          description: certificate.description,
          bannerImage: certificate.bannerImage || '',
          certificateImage: certificate.certificateImage || '',
          certificateType: certificate.certificate_type,
          ctaApply: certificate.cta_apply,
          ctaRates: certificate.cta_rates,
          benefits: certificate.benefits,
          investment: certificate.investment,
          rates: certificate.rates,
          requirements: certificate.requirements,
          depositRates: certificate.depositRates,
          faq: certificate.faq,
          slug: certificate.slug
        }));

      debugLog('[CertificatesService] Certificates fetched successfully:', certificates);
      return certificates;

    } catch (error) {
      errorLog('[CertificatesService] Error fetching certificates:', error);
      // En desarrollo, retornar array vacío para evitar errores
      if (API_CONFIG.IS_DEVELOPMENT) {
        console.warn('[CertificatesService] Development mode: returning empty array due to API error');
        return [];
      }
      throw error; // En producción, lanzar el error
    }
  },

  getCertificateBySlug: async (slug: string): Promise<ICertificateData | null> => {
    try {
      debugLog(`[CertificatesService] Fetching certificate by slug: ${slug}`);
      
      const certificates = await certificatesService.getAllCertificates();
      const certificate = certificates.find(c => c.slug === slug);
      
      if (certificate) {
        debugLog('[CertificatesService] Certificate found:', certificate);
        return certificate;
      } else {
        debugLog('[CertificatesService] Certificate not found');
        return null;
      }

    } catch (error) {
      errorLog('[CertificatesService] Error fetching certificate by slug:', error);
      throw error;
    }
  }
};
