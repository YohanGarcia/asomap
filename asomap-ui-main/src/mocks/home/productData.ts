import { IProduct } from '@interfaces';

import Image1 from '@assets/images/products/product-cards1.png'
import Image2 from '@assets/images/products/product-cards2.png'
import Image3 from '@assets/images/products/product-cards3.png'

export const productsData: { section: { title: string, subtitle: string }, buttonText: string, products: IProduct[] } = {
    section: {
        title: '¿Qué necesitas hoy?',
        subtitle: '¡Mira los productos que tenemos para ti online!'
    },
    buttonText: '¡Solicítalo!',
    products: [
        {
            id: '1',
            title: '¡Tus sueños, tu Préstamo!',
            description: 'Obtenlo en menos 30 minutos a través de nuestros canales digitales.',
            image: Image1,
            category: 'prestamos',
            imageWidth: 600,
            imageHeight: 400
        },
        {
            id: '2',
            title: 'Cuenta de Ahorros',
            description: 'Abre tu cuenta y empieza a ahorrar hoy mismo.',
            image: Image2,
            category: 'cuentas',
            imageWidth: 600,
            imageHeight: 400
        },
        {
            id: '3',
            title: 'Tarjeta de Debito',
            description: 'Abre tu cuenta y empieza a utilizar para tus compras y retiros.',
            image: Image3,
            category: 'tarjetas',
            imageWidth: 600,
            imageHeight: 400
        },
    ]
}; 