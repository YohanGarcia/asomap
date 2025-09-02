export const claimRequestData = {
    title: 'Solicitud de reclamación',
    description: 'Complete este formulario para reportar su reclamación. Todos los campos marcados con * son obligatorios.',
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
                title: 'Formulario de Reclamación',
                fields: [
                    {
                        id: 'fullName',
                        label: 'Nombre Completo',
                        type: 'text',
                        placeholder: 'Nombres, Apellidos',
                        required: true
                    },
                    {
                        id: 'document',
                        label: 'Cédula, Pasaporte o RNC',
                        type: 'text',
                        placeholder: 'Números sin guion',
                        required: true
                    },
                    {
                        id: 'phone',
                        label: 'Teléfono',
                        type: 'tel',
                        placeholder: 'Números sin guion',
                        required: true
                    },
                    {
                        id: 'email',
                        label: 'Correo electrónico',
                        type: 'email',
                        placeholder: 'Correo electrónico',
                        required: true
                    },
                    {
                        id: 'productType',
                        label: 'Tipo Producto Financiero',
                        type: 'select',
                        placeholder: 'Seleccione el tipo de producto',
                        required: true,
                        options: [
                            'CUENTAS DE AHORRO'
                        ]
                    },
                    {
                        id: 'claimType',
                        label: 'Tipo de reclamación',
                        type: 'select',
                        placeholder: 'Seleccione el tipo de reclamación',
                        required: true,
                        options: [
                            'NO RECONOCE CONSUMO EN TARJETA DE CREDITO',
                            'RECONOCE EL CONSUMO EN ESTABLECIMIENTO',
                            'NO RECONOCE CARGO/NO ESTIPULADO O AUTORIZADO',
                            'ERROR EN EL COBRO DE INTERESES',
                            'CONSUMO DUPLICADO',
                            'PAGO NO REFLEJADO',
                            'DEPOSITO NO REFLEJADO',
                            'SOLICITUD CANCELACION DE PRODUCTO O SERVICIO',
                            'DEBITOS DE CUENTAS NO AUTORIZADOS',
                            'EFECTIVO NO DISPENSADO POR EL CAJERO',
                            'PLASTICO (TARJETA DE DEBITO O CREDITO) RETENIDO POR EL CAJERO',
                            'PAGO INCOMPLETO DE INTERESES POR CONCEPTO DE CERTIFICADOS Y CUENTAS',
                            'NO SE LE HAN ACREDITADO LOS INTERESES ESTABLECIDOS EN SU CUENTA',
                            'CAJERO DISPENSO DINERO FALSO',
                            'PAGO EN EXCESO SOBRE SALDO',
                            'CAMBIO DE TASA SIN NOTIFICACION PREVIA POR ESCRITO',
                            'TARJETA DE CREDITO CREADA SIN SU CONSENTIMIENTO ESCRITO',
                            'TRANSACCION FRAUDULENTA',
                            'PROBLEMAS CON LA ENTREGA DE LOS ESTADOS DE CUENTA',
                            'COBRO ERRONEO DEL IMPUESTO DE 0.15%',
                            'TRANSITO TARDIO DE FONDOS',
                            'REDONDEO EN PERJUICIO DEL CLIENTE AL CERRAR UNA CUENTA EN ME',
                            'BLOQUEO DE CUENTA SIN JUSTIFICACION',
                            'CHEQUE CARGADO DOS VECES SOBRE UNA MISMA CUENTA CORRIENTE',
                            'REPORTE DE INFORMACION ERRONEA A LOS BUROS DE CREDITO',
                            'COBRO DE PENALIDAD NO ESTIPULADA',
                            'PAGOS NO APLICADOS DGII',
                            'PAGOS NO APLICADOS TSS',
                            'TRANSFERENCIA NO APLICADA',
                            'CARGO CUOTA PRESTAMO DIFIERE DE LA PACTADA',
                            'FALLO EN EL PAGO AUTOMATICO DEL PRESTAMO',
                            'ERROR EN LA APLICACION DE PAGO',
                            'NOTA DE CREDITO NO CORRESPONDE',
                            'NOTA DE CREDITO NO REGISTRADA',
                            'DEVOLUCION SALDO A FAVOR',
                            'ELIMINACION CARGO FLOTANTE',
                            'RECHAZO DE TARJETA',
                            'PROBLEMAS EN DPTO. COBRANZA LEGAL/EXTERNA',
                            'PROBLEMAS EN DPTO. DE COBROS',
                            'PROBLEMAS LLAMADAS DE COBROS (TURBO COBRO)',
                            'PROBLEMA CON EL PROGRAMA DE FIDELIDAD',
                            'RECLAMACION BENEFICIOS DEL PROGRAMA DE FIDELIDAD',
                            'COMPRA TARJETA DE LLAMADA NO DISPENSADO',
                            'CANCELACION DE PRODUCTO NO EJECUTADA',
                            'ERRORES DETECTADOS EN EL ESTADO DE CUENTA',
                            'CARGO DUPLICADO POR CERTIFICACION DE CHEQUE',
                            'TRANSACCION PROCESADA CON DIFERENCIA',
                            'DEBITOS AUTOMATICOS POR PAGO DE FACTURAS'
                        ]
                    },
                    {
                        id: 'distributionChannel',
                        label: 'Canal de distribución',
                        type: 'select',
                        placeholder: 'Seleccione el canal de distribución',
                        required: true,
                        options: [
                            'CAJEROS AUTOMÁTICOS (ATM)',
                            'E-BANKING',
                            'INTERACTIVE VOICE RESPONSE (IVR)',
                            'PROCESO INTERNO AUTOMATIZADO',
                            'PROCESO INTERNO POR ERROR MANUAL',
                            'VENTANILLA'
                        ]
                    },
                    {
                        id: 'message',
                        label: 'Mensaje',
                        type: 'textarea',
                        placeholder: 'Escriba su mensaje aquí',
                        required: true
                    }
                ]
            }
        }
    }
};
