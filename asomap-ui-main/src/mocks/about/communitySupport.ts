interface Initiative {
  id: string;
  title: string;
  description: string;
  impact: string;
  imageUrl: string;
  category: string;
}

interface Category {
  id: string;
  name: string;
  icon: string;
  description: string;
}

export interface CommunitySupportData {
  title: string;
  description: string;
  categories: Category[];
  initiatives: Initiative[];
}

export const communitySupportData: CommunitySupportData = {
  title: "Apoyo a la Comunidad",
  description: "Dentro de nuestra política de responsabilidad social, la Asociación Mocana de Ahorros y Préstamos contribuye con las instituciones sin fines de lucro que trabajan a favor de los más necesitados en la zona de incidencia de la entidad. Asimismo, aporta a las entidades propulsoras del deporte y la cultura de la región.",
  categories: [
    {
      id: "social",
      name: "Responsabilidad Social",
      icon: "FaHandHoldingHeart",
      description: "Apoyo a organizaciones e instituciones que trabajan en beneficio de los más necesitados"
    },
    {
      id: "culture",
      name: "Cultura",
      icon: "FaPalette",
      description: "Patrocinio de eventos culturales y publicaciones"
    },
    {
      id: "sports",
      name: "Deportes",
      icon: "FaFutbol",
      description: "Apoyo a actividades y campeonatos deportivos"
    }
  ],
  initiatives: [
    {
      id: "social-support",
      title: "Apoyo a Instituciones Sociales",
      description: "Contribuciones a organizaciones como el Albergue Educativo Infantil, parroquias, Centro Juvenil Don Bosco, Hogar Escuela La Milagrosa, y más.",
      impact: "Beneficiando a múltiples instituciones en Moca, Gaspar Hernández, Cayetano Germosén, Villa Tapia y otras localidades.",
      imageUrl: "https://www.asomap.com.do/wp-content/uploads/2018/07/comunidad.jpg",
      category: "social"
    },
    {
      id: "cultural-initiatives",
      title: "Iniciativas Culturales",
      description: "Patrocinio de publicaciones, libros, brochures, conciertos populares, fiestas de carnaval, fiestas patronales y ferias multiservicios.",
      impact: "Fortalecimiento de la identidad cultural y las tradiciones locales.",
      imageUrl: "https://www.asomap.com.do/wp-content/uploads/2018/07/comunidad.jpg",
      category: "culture"
    },
    {
      id: "sports-support",
      title: "Apoyo al Deporte",
      description: "Respaldo a campeonatos nacionales e internacionales en béisbol, ajedrez, damas, baloncesto, voleibol, fútbol y softball.",
      impact: "Promoción del deporte y la actividad física en la comunidad.",
      imageUrl: "https://www.asomap.com.do/wp-content/uploads/2018/07/comunidad.jpg",
      category: "sports"
    }
  ]
};
