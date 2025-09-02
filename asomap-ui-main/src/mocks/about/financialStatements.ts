export interface FinancialDocument {
  title: string;
  url: string;
  quarter?: string;
}

export interface YearData {
  year: string;
  documents: {
    audited: FinancialDocument[];
    quarterly: FinancialDocument[];
  };
}

export const financialStatementsData = {
  title: "Estados Financieros",
  description: "Consulta nuestros estados financieros auditados y trimestrales",
  years: [
    {
      year: "2024",
      documents: {
        audited: [
          {
            title: "Estados Financieros Auditados 2024",
            url: "/documents/financial/audited-2024.pdf"
          }
        ],
        quarterly: [
          {
            title: "Estados Financieros Q1 2024",
            url: "/documents/financial/q1-2024.pdf",
            quarter: "1"
          },
          {
            title: "Estados Financieros Q2 2024",
            url: "/documents/financial/q2-2024.pdf",
            quarter: "2"
          }
        ]
      }
    },
    {
      year: "2023",
      documents: {
        audited: [
          {
            title: "Estados Financieros Auditados 2023",
            url: "/documents/financial/audited-2023.pdf"
          }
        ],
        quarterly: [
          {
            title: "Estados Financieros Q1 2023",
            url: "/documents/financial/q1-2023.pdf",
            quarter: "1"
          },
          {
            title: "Estados Financieros Q2 2023",
            url: "/documents/financial/q2-2023.pdf",
            quarter: "2"
          },
          {
            title: "Estados Financieros Q3 2023",
            url: "/documents/financial/q3-2023.pdf",
            quarter: "3"
          },
          {
            title: "Estados Financieros Q4 2023",
            url: "/documents/financial/q4-2023.pdf",
            quarter: "4"
          }
        ]
      }
    },
    {
      year: "2022",
      documents: {
        audited: [
          {
            title: "Estados Financieros Auditados 2022",
            url: "/documents/financial/audited-2022.pdf"
          }
        ],
        quarterly: [
          {
            title: "Estados Financieros Q1 2022",
            url: "/documents/financial/q1-2022.pdf",
            quarter: "1"
          },
          {
            title: "Estados Financieros Q2 2022",
            url: "/documents/financial/q2-2022.pdf",
            quarter: "2"
          },
          {
            title: "Estados Financieros Q3 2022",
            url: "/documents/financial/q3-2022.pdf",
            quarter: "3"
          },
          {
            title: "Estados Financieros Q4 2022",
            url: "/documents/financial/q4-2022.pdf",
            quarter: "4"
          }
        ]
      }
    }
  ]
};
