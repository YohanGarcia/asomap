import RightsImage1 from '@assets/images/user-support/rights/rights1.jpg';
import DutiesImage1 from '@assets/images/user-support/duties/duties1.jpg';

export interface Image {
    id: number;
    src: string;
    alt: string;
    description?: string;
}

export interface Section {
    additionalInfo: string;
    id: string;
    title: string;
    description: string;
    buttonText: string;
    images: Image[];
}

// Derechos y Deberes section
export const rightsAndDuties: Section = {
    id: "rightsAndDuties",
    title: "Derechos y Deberes",
    description: `Como usuario de ASOMAP, es importante conocer tanto sus derechos fundamentales que protegen sus intereses,
    como sus deberes que ayudan a mantener una relación financiera saludable y beneficiosa para todos.`,
    buttonText: "Ver Derechos y Deberes",
    images: [
        {
            id: 1,
            src: RightsImage1,
            alt: "Derechos y Deberes 1",
            description: "Derechos y deberes fundamentales"
        },
        {
            id: 2,
            src: DutiesImage1,
            alt: "Derechos y Deberes 2",
            description: "Responsabilidades y beneficios"
        }
    ],
    additionalInfo: ''
};

// Otros Derechos section
export const otherRights: Section = {
    id: "otherRights",
    title: "Otros Derechos",
    description: `Además de los derechos y deberes básicos, como usuario de servicios financieros usted cuenta con 
    derechos adicionales que complementan y fortalecen su protección como usuario de ASOMAP.`,
    buttonText: "Ver Otros Derechos",
    images: [
        {
            id: 1,
            src: RightsImage1,
            alt: "Otros Derechos 1",
            description: "Derechos complementarios"
        },
        {
            id: 2,
            src: RightsImage1,
            alt: "Otros Derechos 2",
            description: "Derechos adicionales"
        }
    ],
    additionalInfo: ''
};

// Main data structure
export const rightsAndDutiesData = {
    pageTitle: "Derechos y Deberes",
    pageDescription: `En ASOMAP, nos comprometemos a mantener una relación transparente y justa con nuestros usuarios. 
    Conocer sus derechos y deberes es fundamental para garantizar una experiencia financiera satisfactoria y segura.`,
    sections: [rightsAndDuties, otherRights]
};