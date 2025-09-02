export interface AbandonedAccountsData {
  title: string;
  description: string;
  accountTypes: {
    id: string;
    label: string;
    description: string;
  }[];
  years: {
    year: string;
    documents: {
      abandoned: {
        title: string;
        url: string;
        date: string;
      };
      inactive: {
        title: string;
        url: string;
        date: string;
      };
    };
  }[];
}

export const abandonedAccountsData: AbandonedAccountsData = {
  title: "Cuentas Abandonadas e Inactivas",
  description: "Consulta el listado de cuentas abandonadas e inactivas por año",
  accountTypes: [
    {
      id: "abandoned",
      label: "Cuentas Abandonadas",
      description: "Cuentas sin movimientos por más de 10 años",
    },
    {
      id: "inactive",
      label: "Cuentas Inactivas",
      description: "Cuentas sin movimientos por más de 3 años",
    },
  ],
  years: [
    {
      year: "2024",
      documents: {
        abandoned: {
          title: "Listado de Cuentas Abandonadas 2024",
          url: "/documents/abandoned-accounts/2024/abandoned-accounts.pdf",
          date: "2024-01-15",
        },
        inactive: {
          title: "Listado de Cuentas Inactivas 2024",
          url: "/documents/abandoned-accounts/2024/inactive-accounts.pdf",
          date: "2024-01-15",
        },
      },
    },
    {
      year: "2023",
      documents: {
        abandoned: {
          title: "Listado de Cuentas Abandonadas 2023",
          url: "/documents/abandoned-accounts/2023/abandoned-accounts.pdf",
          date: "2023-12-15",
        },
        inactive: {
          title: "Listado de Cuentas Inactivas 2023",
          url: "/documents/abandoned-accounts/2023/inactive-accounts.pdf",
          date: "2023-12-15",
        },
      },
    },
    {
      year: "2022",
      documents: {
        abandoned: {
          title: "Listado de Cuentas Abandonadas 2022",
          url: "/documents/abandoned-accounts/2022/abandoned-accounts.pdf",
          date: "2022-12-15",
        },
        inactive: {
          title: "Listado de Cuentas Inactivas 2022",
          url: "/documents/abandoned-accounts/2022/inactive-accounts.pdf",
          date: "2022-12-15",
        },
      },
    },
  ],
};
