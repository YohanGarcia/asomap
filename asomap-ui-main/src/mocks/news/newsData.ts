import { INewsData } from '@/interfaces/news.interface';

export const newsData: INewsData = {
  banner: {
    title: "Últimas Noticias",
    imageUrl: "https://images.unsplash.com/photo-1560472355-536de3962603?q=80&w=1200"
  },
  slides: [
    {
      id: 1,
      image: 'https://images.unsplash.com/photo-1560472355-536de3962603?q=80&w=1200',
      title: 'ASOMAP celebra su 60 aniversario',
      description: 'La Asociación Popular de Ahorros y Préstamos (ASOMAP) celebró su 60 aniversario con una serie de eventos especiales que resaltaron su trayectoria de servicio y compromiso con la comunidad dominicana.',
      date: '21 de septiembre, 2024',
      author: 'Equipo de Comunicaciones ASOMAP',
      category: 'Eventos Institucionales',
      tags: ['Aniversario', 'Celebración', 'Historia'],
      fullContent: [
        {
          type: 'paragraph',
          content: 'La Asociación Popular de Ahorros y Préstamos (ASOMAP) celebró su 60 aniversario con una serie de eventos especiales que resaltaron su trayectoria de servicio y compromiso con la comunidad dominicana.'
        },
        {
          type: 'subtitle',
          content: 'Un legado de servicio a la comunidad'
        },
        {
          type: 'paragraph',
          content: 'Durante seis décadas, ASOMAP ha sido un pilar fundamental en el desarrollo económico y social de la República Dominicana, ofreciendo servicios financieros accesibles y de calidad a miles de familias dominicanas.'
        }
      ]
    },
    {
      id: 2,
      image: 'https://images.unsplash.com/photo-1579621970563-ebec7560ff3e?q=80&w=1200',
      title: 'Nueva App Móvil ASOMAP Digital',
      description: 'Lanzamos nuestra nueva aplicación móvil con funcionalidades mejoradas y una experiencia de usuario optimizada para ofrecer servicios bancarios más ágiles y seguros.',
      date: '15 de septiembre, 2024',
      author: 'Departamento de Tecnología',
      category: 'Tecnología',
      tags: ['App Móvil', 'Innovación', 'Digital'],
      fullContent: [
        {
          type: 'paragraph',
          content: 'ASOMAP presenta su nueva aplicación móvil, diseñada para ofrecer una experiencia bancaria más ágil y segura.'
        },
        {
          type: 'subtitle',
          content: 'Funcionalidades principales'
        },
        {
          type: 'list',
          content: [
            'Consulta de saldos en tiempo real',
            'Transferencias entre cuentas',
            'Pago de servicios',
            'Historial de transacciones',
            'Notificaciones push'
          ]
        }
      ]
    },
    {
      id: 3,
      image: 'https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?q=80&w=1200',
      title: 'Resultados Financieros Q3 2024',
      description: 'ASOMAP reporta un sólido crecimiento en el tercer trimestre con aumentos significativos en depósitos y préstamos, demostrando la confianza de nuestros asociados.',
      date: '10 de septiembre, 2024',
      author: 'Departamento Financiero',
      category: 'Finanzas',
      tags: ['Resultados', 'Finanzas', 'Crecimiento'],
      fullContent: [
        {
          type: 'paragraph',
          content: 'Los resultados financieros del tercer trimestre muestran un crecimiento sostenido en todas las áreas clave del negocio.'
        },
        {
          type: 'quote',
          content: 'Estos resultados reflejan la confianza de nuestros asociados y el compromiso de nuestro equipo con la excelencia en el servicio.'
        }
      ]
    },
    {
      id: 4,
      image: 'https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?q=80&w=1200',
      title: 'Inauguración Nueva Sucursal Santiago',
      description: 'ASOMAP expande su presencia en el Cibao con una moderna sucursal en Santiago de los Caballeros, ofreciendo servicios financieros de calidad a la región.',
      date: '5 de septiembre, 2024',
      author: 'Equipo de Expansión',
      category: 'Expansión',
      tags: ['Sucursales', 'Santiago', 'Crecimiento'],
      fullContent: [
        {
          type: 'paragraph',
          content: 'La nueva sucursal en Santiago representa un paso importante en nuestra estrategia de expansión nacional.'
        }
      ]
    },
    {
      id: 5,
      image: 'https://images.unsplash.com/photo-1521791136064-7986c2920216?q=80&w=1200',
      title: 'Programa de Educación Financiera',
      description: 'Lanzamos nuevo programa educativo para promover la salud financiera en comunidades locales, empoderando a las familias con conocimientos financieros esenciales.',
      date: '1 de septiembre, 2024',
      author: 'Departamento de RSE',
      category: 'Educación',
      tags: ['Educación', 'Comunidad', 'RSE'],
      fullContent: [
        {
          type: 'paragraph',
          content: 'El nuevo programa de educación financiera busca empoderar a las comunidades con conocimientos financieros esenciales.'
        }
      ]
    },
    {
      id: 6,
      image: 'https://images.unsplash.com/photo-1553729459-efe14ef6055d?q=80&w=1200',
      title: 'Alianza Estratégica con MasterCard',
      description: 'Nueva alianza estratégica para ofrecer beneficios exclusivos a nuestros tarjetahabientes, ampliando las opciones de pago y recompensas.',
      date: '28 de agosto, 2024',
      author: 'Departamento de Productos',
      category: 'Alianzas',
      tags: ['MasterCard', 'Tarjetas', 'Beneficios'],
      fullContent: [
        {
          type: 'paragraph',
          content: 'La alianza con MasterCard permitirá ofrecer nuevos beneficios y recompensas a nuestros clientes.'
        }
      ]
    },
    {
      id: 7,
      image: 'https://images.unsplash.com/photo-1542744173-8e7e53415bb0?q=80&w=1200',
      title: 'Reconocimiento Great Place to Work',
      description: 'ASOMAP recibe certificación Great Place to Work por segundo año consecutivo, reconociendo nuestro compromiso con la excelencia en la gestión del talento humano.',
      date: '25 de agosto, 2024',
      author: 'Recursos Humanos',
      category: 'Reconocimientos',
      tags: ['GPTW', 'Cultura', 'Empleados'],
      fullContent: [
        {
          type: 'paragraph',
          content: 'La certificación Great Place to Work refleja nuestro compromiso con la excelencia en la gestión del talento humano.'
        }
      ]
    },
    {
      id: 8,
      image: 'https://images.unsplash.com/photo-1507679799987-c73779587ccf?q=80&w=1200',
      title: 'Nuevo Programa de Lealtad',
      description: 'Lanzamos programa de puntos renovado con más beneficios y opciones de canje, recompensando la fidelidad de nuestros clientes.',
      date: '20 de agosto, 2024',
      author: 'Departamento de Marketing',
      category: 'Productos',
      tags: ['Lealtad', 'Puntos', 'Beneficios'],
      fullContent: [
        {
          type: 'paragraph',
          content: 'El nuevo programa de lealtad ofrece más opciones y mejores beneficios para nuestros clientes fieles.'
        }
      ]
    }
  ]
};