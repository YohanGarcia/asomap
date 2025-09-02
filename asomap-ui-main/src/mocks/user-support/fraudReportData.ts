export const fraudReportData = {
    title: 'Repota tu Fraude',
    description: 'Completa este formulario si requieres de algún apoyo adicional en caso presentes alguna discapacidad física, sensorial, permanente o temporal. Estamos para ayudarte en todo momento.',
    email: 'prousuarioasomap@asomap.com.do',
    validation: {
        document: {
            cedula: /^\d{11}$/,
            pasaporte: /^[A-Z0-9]{9,12}$/i,
            rnc: /^\d{9}$/
        },
        phone: /^\d{10}$/
    },
    form: {
        sections: {
            personalInfo: {
                title: 'Formulario Reporte de Fraude',
                fields: [
                    {
                        id: 'classification',
                        label: 'Clasificación',
                        type: 'select',
                        placeholder: 'Selección de Clasificación',
                        required: true,
                        options: [
                            'Tarjeta perdida',
                            'Tarjeta robada ',
                        ]
                    },
                    {
                        id: 'fullName',
                        label: 'Nombre y apellidos',
                        type: 'text',
                        placeholder: 'Nombre y apellidos',
                        required: true
                    },
                    {
                        id: 'document',
                        label: 'Cédula, Pasaporte o RNC',
                        type: 'text',
                        placeholder: 'Ingrese número sin guiones',
                        required: true
                    },
                    {
                        id: 'phone',
                        label: 'No. de contacto',
                        type: 'tel',
                        placeholder: 'Ingrese número telefónico',
                        required: true
                    },
                    {
                        id: 'email',
                        label: 'Email',
                        type: 'email',
                        placeholder: 'Email',
                        required: true
                    },
                    {
                        id: 'file',
                        label: 'Adjuntar Archivo',
                        type: 'file',
                        placeholder: 'Adjuntar Archivo',
                        required: true,
                        accept: '.jpg,.png'
                    },
                    {
                        id: 'message',
                        label: 'Comentario o mensaje',
                        type: 'textarea',
                        placeholder: 'Escriba su mensaje aquí',
                        required: true
                    }
                ]
            }
        }
    }
};
