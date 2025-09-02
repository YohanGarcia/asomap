import { httpClient } from '../../config/httpClient';
import { ENDPOINTS } from '@/constants';
import { debugLog, errorLog } from '@/utils/environment';
import type { ISubmitFraudReport } from '@/interfaces';

interface FraudReportResponse {
  message: string;
}

export const fraudReportService = {
  submitFraudReport: async (formData: ISubmitFraudReport): Promise<string> => {
    try {
      debugLog('[FraudReportService] Submitting fraud report:', formData);
      
      // Console log para ver los datos que se envían
      console.log('📤 Datos del formulario:');
      console.log('- classification:', formData.classification);
      console.log('- fullName:', formData.fullName);
      console.log('- document:', formData.document);
      console.log('- phone:', formData.phone);
      console.log('- email:', formData.email);
      console.log('- message:', formData.message);
      console.log('- file:', formData.file ? `${formData.file.name} (${formData.file.size} bytes)` : 'No file');
      
      // Crear objeto JSON sin el archivo
      const submitData = {
        classification: formData.classification,
        fullName: formData.fullName,
        document: formData.document,
        phone: formData.phone,
        email: formData.email,
        message: formData.message
        // ❌ NO incluir file aquí - se maneja por separado
      };
      
      // Console log para ver el JSON creado
      console.log('📤 JSON enviando al backend:', submitData);
      
      const response = await httpClient.post<FraudReportResponse, Record<string, unknown>>(
        ENDPOINTS.COLLECTIONS.USER_SUPPORT.FRAUD_REPORT,
        submitData
        // Removemos el Content-Type para que se establezca automáticamente con FormData
      );

      debugLog('[FraudReportService] Fraud report submitted successfully:', response.data);
      
      // Console log para ver la respuesta del backend
      console.log('📥 Respuesta del backend:', response.data);
      
      return response.data.message;

    } catch (error) {
      errorLog('[FraudReportService] Error submitting fraud report:', error);
      throw error;
    }
  }
};
