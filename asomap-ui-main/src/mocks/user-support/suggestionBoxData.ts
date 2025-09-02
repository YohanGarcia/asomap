export const suggestionBoxData = {
    title: 'Buzón de Sugerencias',
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
    provinces: [
        'Azua', 'Bahoruco', 'Barahona', 'Dajabón', 'Distrito Nacional', 'Duarte',
        'Elías Piña', 'El Seibo', 'Espaillat', 'Hato Mayor', 'Hermanas Mirabal',
        'Independencia', 'La Altagracia', 'La Romana', 'La Vega', 'María Trinidad Sánchez',
        'Monseñor Nouel', 'Monte Cristi', 'Monte Plata', 'Pedernales', 'Peravia',
        'Puerto Plata', 'Samaná', 'San Cristóbal', 'San José de Ocoa', 'San Juan',
        'San Pedro de Macorís', 'Santiago', 'Santiago Rodríguez', 'Santo Domingo',
        'Sánchez Ramírez', 'Valverde'
    ],
    form: {
        sections: {
            personalInfo: {
                title: 'Datos de la Persona',
                fields: [
                    {
                        id: 'classification',
                        label: 'Clasificación',
                        type: 'select',
                        placeholder: 'Seleccione una opción',
                        required: true,
                        options: [
                            'Sugerencia',
                            'Queja'
                        ]
                    },
                    {
                        id: 'fullName',
                        label: 'Nombre y apellidos',
                        type: 'text',
                        placeholder: 'Ingrese nombres y apellidos',
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
                        label: 'Correo electrónico',
                        type: 'email',
                        placeholder: 'correo@ejemplo.com',
                        required: true
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
        },
        submitButton: {
            text: 'Enviar',
            loadingText: 'Enviando...'
        }
    }
};
