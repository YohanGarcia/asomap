import { httpClient } from '../../config/httpClient';
import { API_CONFIG } from '../../config/config';
import { ENDPOINTS } from '@/constants';
import { debugLog, errorLog } from '@/utils/environment';
import type { ILoansAPIResponse, ILoanData } from '@/interfaces';

// Función para generar slug desde el título
const generateSlug = (title: string): string => {
  return title.toLowerCase()
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/(^-|-$)/g, '');
};

export const loansService = {
  getAllLoans: async (): Promise<ILoanData[]> => {
    try {
      debugLog('[LoansService] Fetching all loans');
      
      const response = await httpClient.get<ILoansAPIResponse>(ENDPOINTS.COLLECTIONS.PRODUCTS.LOANS);
      
      // Filtrar solo préstamos activos y transformar datos
      const loans: ILoanData[] = response.data.results
        .filter(loan => loan.is_active)
        .map(loan => ({
          id: loan.id,
          title: loan.title,
          description: loan.description,
          loanType: loan.loan_type,
          details: loan.details,
          requirementsTitle: loan.requirements_title,
          requirements: loan.requirements,
          slug: generateSlug(loan.title),
          bannerImage: 'https://images.unsplash.com/photo-1554224155-8947307dabb2?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&h=500&q=80'
        }));

      debugLog('[LoansService] Loans fetched successfully:', loans);
      return loans;

    } catch (error) {
      errorLog('[LoansService] Error fetching loans:', error);
      // En desarrollo, retornar array vacío para evitar errores
      if (API_CONFIG.IS_DEVELOPMENT) {
        console.warn('[LoansService] Development mode: returning empty array due to API error');
        return [];
      }
      throw error; // En producción, lanzar el error
    }
  },

  getLoanBySlug: async (slug: string): Promise<ILoanData | null> => {
    try {
      debugLog(`[LoansService] Fetching loan by slug: ${slug}`);
      
      const loans = await loansService.getAllLoans();
      const loan = loans.find(l => l.slug === slug);
      
      if (loan) {
        debugLog('[LoansService] Loan found:', loan);
        return loan;
      } else {
        debugLog('[LoansService] Loan not found');
        return null;
      }

    } catch (error) {
      errorLog('[LoansService] Error fetching loan by slug:', error);
      throw error;
    }
  },

  getLoansByType: async (loanType: string): Promise<ILoanData[]> => {
    try {
      debugLog(`[LoansService] Fetching loans by type: ${loanType}`);
      
      const allLoans = await loansService.getAllLoans();
      const filteredLoans = allLoans.filter(loan => loan.loanType === loanType);
      
      debugLog(`[LoansService] Found ${filteredLoans.length} loans of type ${loanType}`);
      return filteredLoans;

    } catch (error) {
      errorLog('[LoansService] Error fetching loans by type:', error);
      throw error;
    }
  }
};
