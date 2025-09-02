import { httpClient } from '../../config/httpClient';
import { ENDPOINTS } from '@/constants';
import { debugLog, errorLog } from '@/utils/environment';
import type { ISubmitClaimRequest } from '@/interfaces';

interface ClaimRequestResponse {
  message: string;
}

export const claimRequestService = {
  submitClaimRequest: async (formData: ISubmitClaimRequest): Promise<string> => {
    try {
      debugLog('[ClaimRequestService] Submitting claim request:', formData);
      
      const response = await httpClient.post<ClaimRequestResponse, ISubmitClaimRequest>(
        ENDPOINTS.COLLECTIONS.USER_SUPPORT.CLAIM_REQUEST,
        formData
      );

      debugLog('[ClaimRequestService] Claim request submitted successfully:', response.data);
      return response.data.message;

    } catch (error) {
      errorLog('[ClaimRequestService] Error submitting claim request:', error);
      throw error;
    }
  }
};
