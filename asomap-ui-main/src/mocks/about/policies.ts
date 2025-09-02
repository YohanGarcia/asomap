export interface Pagination {
  page: number;
  pageSize: number;
  total: number;
  totalPages: number;
}

export interface PaginatedResponse<T> {
  data: T;
  pagination: Pagination;
}

export interface PolicyDocument {
  title: string;
  description: string;
  url: string;
  lastUpdate: string;
  categoryId?: string;
  categoryTitle?: string;
}

export interface PolicyCategory {
  title: string;
  icon: string;
  description: string;
  documents: PolicyDocument[];
}

export interface PoliciesData {
  title: string;
  description: string;
  downloadText: string;
  lastUpdateText: string;
  allPoliciesText: string;
  categories: PolicyCategory[];
}

export const policiesData: PoliciesData = {
  title: "Políticas",
  description: "Nuestras políticas institucionales garantizan la transparencia y eficiencia en nuestras operaciones.",
  downloadText: "Descargar documento",
  lastUpdateText: "Última actualización",
  allPoliciesText: "Todas las Políticas",
  categories: [
    {
      title: "Políticas de Gobernanza",
      icon: "shield",
      description: "Lineamientos fundamentales que rigen nuestra institución",
      documents: [
        {
          title: "Código de Ética y Conducta",
          description: "Lineamientos éticos y conductuales para todos los miembros de la institución",
          url: "/documents/policies/code-of-ethics.pdf",
          lastUpdate: "2024-01-15"
        },
        {
          title: "Política de Gobierno Corporativo",
          description: "Marco de gobierno y toma de decisiones institucional",
          url: "/documents/policies/corporate-governance.pdf",
          lastUpdate: "2023-12-01"
        },
        {
          title: "Política de Transparencia",
          description: "Directrices para garantizar la transparencia en todas nuestras operaciones",
          url: "/documents/policies/transparency-policy.pdf",
          lastUpdate: "2024-01-20"
        },
        {
          title: "Manual de Gobernanza Digital",
          description: "Guía para la gestión de activos y procesos digitales",
          url: "/documents/policies/digital-governance.pdf",
          lastUpdate: "2024-01-18"
        }
      ]
    },
    {
      title: "Políticas Operativas",
      icon: "cog",
      description: "Procedimientos y normas para nuestras operaciones diarias",
      documents: [
        {
          title: "Manual de Procedimientos",
          description: "Procedimientos operativos estándar de la institución",
          url: "/documents/policies/procedures-manual.pdf",
          lastUpdate: "2024-01-10"
        },
        {
          title: "Política de Seguridad",
          description: "Normas y procedimientos de seguridad institucional",
          url: "/documents/policies/security-policy.pdf",
          lastUpdate: "2023-11-15"
        },
        {
          title: "Manual de Calidad",
          description: "Estándares y procesos para asegurar la calidad del servicio",
          url: "/documents/policies/quality-manual.pdf",
          lastUpdate: "2024-01-22"
        },
        {
          title: "Política de Gestión de Riesgos",
          description: "Marco para la identificación y gestión de riesgos operativos",
          url: "/documents/policies/risk-management.pdf",
          lastUpdate: "2024-01-05"
        },
        {
          title: "Manual de Continuidad de Negocio",
          description: "Procedimientos para garantizar la continuidad operativa",
          url: "/documents/policies/business-continuity.pdf",
          lastUpdate: "2024-01-12"
        }
      ]
    },
    {
      title: "Políticas de Cumplimiento",
      icon: "check-circle",
      description: "Normativas y regulaciones que aseguran nuestro cumplimiento",
      documents: [
        {
          title: "Manual de Prevención de Lavado",
          description: "Políticas y procedimientos contra el lavado de activos",
          url: "/documents/policies/aml-manual.pdf",
          lastUpdate: "2024-01-05"
        },
        {
          title: "Política de Protección al Usuario",
          description: "Lineamientos para la protección de nuestros usuarios",
          url: "/documents/policies/user-protection.pdf",
          lastUpdate: "2023-12-20"
        },
        {
          title: "Política de Privacidad de Datos",
          description: "Normas para la protección y manejo de datos personales",
          url: "/documents/policies/data-privacy.pdf",
          lastUpdate: "2024-01-25"
        },
        {
          title: "Manual de Cumplimiento Regulatorio",
          description: "Guía para el cumplimiento de regulaciones financieras",
          url: "/documents/policies/regulatory-compliance.pdf",
          lastUpdate: "2024-01-15"
        },
        {
          title: "Política Antisoborno y Anticorrupción",
          description: "Medidas preventivas contra el soborno y la corrupción",
          url: "/documents/policies/anti-corruption.pdf",
          lastUpdate: "2024-01-08"
        },
        {
          title: "Manual de Debida Diligencia",
          description: "Procedimientos para la evaluación de clientes y proveedores",
          url: "/documents/policies/due-diligence.pdf",
          lastUpdate: "2024-01-19"
        }
      ]
    }
  ]
};
