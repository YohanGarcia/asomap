import ImageHistory from '@assets/images/about/historia.jpg'
import ImagePresidente from '@assets/images/about/Presidente.jpg'
import ImagePrimerVicepresidente from '@assets/images/about/PrimerVicepresidente.jpg'
import ImageSegundoVicepresidente from '@assets/images/about/SegundaVicepresidente.jpg'
import ImageVicepresidenteEjecutivo from '@assets/images/about/VicepresidenteEjecutivo.jpg'
import ImageSecretario from '@assets/images/about/Secretario.jpg'
import ImageMiembro from '@assets/images/about/Miembro.jpg'

// Los iconos se manejarán como strings y se resolverán en el componente
export const aboutData = {
    hero: {
        title: "Sobre Nosotros",
        description: "Conoce más sobre nuestra misión, visión y valores."
    },
    quienesSomos: {
        title: "¿Quiénes Somos?",
        paragraphs: [
            "Para el año 1969, la ciudad de Moca era apenas una aldea, enmarcada en unas cuantas calles y con un nivel de desarrollo semirural, aspecto que fue aprovechado por un selecto grupo de munícipes visionarios y emprendedores para crear una institución que permitiera a la provincia Espaillat crecer en los ámbitos urbanístico y económico, en sentido general.",
            "De esa idea, nace la Asociación Mocana de Ahorros y Préstamos, que 54 años después cuenta con oficinas en: Moca Oficina Principal, Plaza Sunrise Moca, Colinas Mall Santiago, Bella Terra Mall Santiago, Altamira, Gaspar Hernandez, San Víctor, Villa Tapia, Cayetano Germosen, Juan López, Licey y Santo Domingo.",
            "Hoy, 50 años después, la ciudad de Moca se ha convertido en una urbe con un movimiento comercial de gran actividad y un desarrollo urbanístico, en el que ha estado presente, vía el financiamiento, la mano de la Asociación de Mocana.",
            "La Asociación Mocana fue constituida el 11 de marzo del año 1969, amparada en las leyes que rigen el Sistema Dominicano de Ahorros y Préstamos e inició sus operaciones el 1ero. de abril de 1969."
        ],
        imageSrc: ImageHistory,
        imageAlt: "Imagen que representa quienes somos"
    },
    nuestraHistoria: {
        title: "Nuestra Historia",
        paragraphs: [
            "Esta entidad es de carácter mutualista y su objetivo consiste en proveer y fomentar el ahorro, el cual es inicialmente destinado al otorgamiento de préstamos para la construcción, adquisición y mejoramiento de viviendas y locales comerciales.",
            "Las actividades de la Asociación están sujetas a la regulación y vigilancia por la Superintendencia de Bancos y el Banco Central de la República Dominicana."
        ],
        imageSrc: ImageHistory,
        imageAlt: "Imagen que representa nuestra historia"
    },
    misionVision: {
        title: "Misión y Visión",
        items: [
            {
                title: "Misión",
                description: "Somos una institución mutualista que oferta productos y servicios financieros basados en la excelencia en el servicio, en tiempo oportuno y accesibilidad a dichos servicios con colaboradores altamente calificados y el uso de tecnología de punta.",
                icon: "FaHandHoldingHeart"
            },
            {
                title: "Visión",
                description: "Ocupar una posición preferencial como asociación de ahorros y préstamos, a través de un crecimiento sostenido en la oferta diversa de productos y servicios.",
                icon: "FaUserShield"
            }
        ]
    },
    valores: {
        title: "Nuestros Valores",
        items: [
            {
                title: "Honestidad",
                description: "Como institución, buscamos comportarnos y expresarnos siempre con coherencia y sinceridad y de acuerdo a valores de verdad y justicia.",
                icon: "FaPeopleArrows"
            },
            {
                title: "Prudencia",
                description: "En la toma de decisiones, procuramos actuar con prudencia, justicia y cautela, teniendo conciencia del efecto que pueden producir nuestras acciones a lo interno y externo de la institución.",
                icon: "FaTree"
            },
            {
                title: "Credibilidad",
                description: "Mediante un accionar íntegro y operaciones ejecutadas bajo estrictas normas éticas y morales, generamos confianza y el conocimiento necesario entre nuestros asociados de que sus recursos son manejados adecuadamente.",
                icon: "FaServicestack"
            },
            {
                title: "Responsabilidad Social",
                description: "La Asociación trabaja en pro del desarrollo y el bienestar social de las demarcaciones en las que tenemos incidencia.",
                icon: "FaPeopleArrows"
            },
            {
                title: "Espíritu de Servicio",
                description: "Procuramos ofrecer un servicio personalizado y de calidad a todos nuestros clientes.",
                icon: "FaHandHoldingHeart"
            }
        ]
    },
    consejoDirectores: [
        {
            name: "Omar A. Taveras López",
            position: "Presidente",
            imageSrc: ImagePresidente,
            imageAlt: "Omar A. Taveras López",
        },
        {
            name: "Johany Teresa García Martínez",
            position: "Miembro",
            imageSrc: "/path/to/johany.jpg", 
            imageAlt: "Johany Teresa García Martínez",
        },
        {
            name: "María Esther Veras Taveras",
            position: "Primer Vicepresidente",
            imageSrc: ImagePrimerVicepresidente, 
            imageAlt: "María Esther Veras Taveras",
        },
        {
            name: "Marianny Paola Abreu Pérez",
            position: "Segunda Vicepresidente",
            imageSrc: ImageSegundoVicepresidente, 
            imageAlt: "Marianny Paola Abreu Pérez",
        },
        {
            name: "Manuel de Jesús Ruiz Beato",
            position: "Vicepresidente Ejecutivo",
            imageSrc: ImageVicepresidenteEjecutivo, 
            imageAlt: "Manuel de Jesús Ruiz Beato",
        },
        {
            name: "Pedro José Pérez Ferreras",
            position: "Secretario",
            imageSrc: ImageSecretario, 
            imageAlt: "Pedro José Pérez Ferreras",
        },
        {
            name: "Miguel Darío Bencosme Comprés",
            position: "Miembro",
            imageSrc: ImageMiembro, 
            imageAlt: "Miguel Darío Bencosme Comprés",
        },
    ],
} as const;

export const aboutItems = [
    {
        text: "¿Quiénes Somos?",
        to: "/about/quienes-somos"
    },
    {
        text: "Nuestra Historia",
        to: "/about/historia"
    },
    {
        text: "Misión y Visión",
        to: "/about/mision-vision"
    },
    {
        text: "Nuestros Valores",
        to: "/about/valores"
    },
    {
        text: "Consejo de Directores",
        to: "/about/consejo-directores"
    }
];

export default aboutData;
