import { accountsService } from '../products/accounts';
import { cardsService } from '../products/cards';
import { certificatesService } from '../products/certificates';
import { loansService } from '../products/loans';
import { debugLog, errorLog } from '@/utils/environment';

export interface MenuAccountItem {
  text: string;
  href: string;
  image: string;
  category: string;
}

export interface MenuSection {
  text: string;
  icon: string;
  subItems: MenuAccountItem[];
  image: string;
}

// Función para generar slug desde el título
const generateSlug = (title: string): string => {
  return title.toLowerCase()
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/(^-|-$)/g, '');
};

export const menuService = {
  getProductMenuItems: async (): Promise<MenuSection[]> => {
    try {
      debugLog('[MenuService] Fetching product menu items');
      
      // Obtener cuentas dinámicas
      const accounts = await accountsService.getAllAccounts();
      const accountsMenuItems: MenuAccountItem[] = accounts.map(account => ({
        text: account.title,
        href: `/productos/cuenta/${generateSlug(account.title)}`,
        image: account.accountImage || 'https://images.unsplash.com/photo-1554224155-6726b3ff858f?ixlib=rb-4.0.3&auto=format&fit=crop&w=300&q=80',
        category: account.category
      }));

      // Obtener tarjetas dinámicas
      const cards = await cardsService.getAllCards();
      const cardsMenuItems: MenuAccountItem[] = cards.map(card => ({
        text: card.title,
        href: `/productos/tarjeta/${card.slug}`,
        image: card.cardImage || 'https://images.unsplash.com/photo-1601597111158-f1446042c8fc?ixlib=rb-4.0.3&auto=format&fit=crop&w=300&q=80',
        category: card.cardType
      }));

      // Obtener certificados dinámicos
      const certificates = await certificatesService.getAllCertificates();
      const certificatesMenuItems: MenuAccountItem[] = certificates.map(certificate => ({
        text: certificate.title,
        href: `/productos/certificado/${certificate.slug}`,
        image: certificate.certificateImage || 'https://images.unsplash.com/photo-1611095566888-f1446042c8fc?ixlib=rb-4.0.3&auto=format&fit=crop&w=300&q=80',
        category: certificate.certificateType
      }));

      // Obtener préstamos dinámicos
      const loans = await loansService.getAllLoans();
      const loansMenuItems: MenuAccountItem[] = loans.map(loan => ({
        text: loan.title,
        href: `/productos/prestamo/${loan.slug}`,
        image: loan.bannerImage || 'https://images.unsplash.com/photo-1554224155-8947307dabb2?ixlib=rb-4.0.3&auto=format&fit=crop&w=300&q=80',
        category: loan.loanType
      }));

      // Estructura jerárquica del menú con categorías
      const menuSections: MenuSection[] = [
        {
          text: "Cuentas",
          icon: "FiDollarSign",
          subItems: accountsMenuItems,
          image: "https://images.unsplash.com/photo-1579621970563-ebec7560ff3e?ixlib=rb-4.0.3&auto=format&fit=crop&w=300&q=80"
        },
        {
          text: "Tarjetas",
          icon: "FiCreditCard",
          subItems: cardsMenuItems,
          image: "https://images.unsplash.com/photo-1563013544-824ae1b704d3?ixlib=rb-4.0.3&auto=format&fit=crop&w=300&q=80"
        },
        {
          text: "Préstamos",
          icon: "FiTrendingUp",
          subItems: loansMenuItems,
          image: "https://images.unsplash.com/photo-1554224155-8947307dabb2?ixlib=rb-4.0.3&auto=format&fit=crop&w=300&q=80"
        },
        {
          text: "Certificados",
          icon: "FiAward",
          subItems: certificatesMenuItems,
          image: "https://images.unsplash.com/photo-1607863680198-23d4b2565df0?ixlib=rb-4.0.3&auto=format&fit=crop&w=300&q=80"
        }
      ];

      debugLog('[MenuService] Generated menu sections:', menuSections);
      return menuSections;

    } catch (error) {
      errorLog('[MenuService] Error fetching product menu items:', error);
      // Retornar estructura por defecto si hay error
      return [
        {
          text: "Cuentas",
          icon: "FiDollarSign",
          subItems: [
            {
              text: "Cuenta Clásica Física",
              href: "/productos/cuenta/cuenta-fisica-clasica",
              image: "https://images.unsplash.com/photo-1554224155-6726b3ff858f?ixlib=rb-4.0.3&auto=format&fit=crop&w=300&q=80",
              category: "classic_physical"
            }
          ],
          image: "https://images.unsplash.com/photo-1579621970563-ebec7560ff3e?ixlib=rb-4.0.3&auto=format&fit=crop&w=300&q=80"
        },
        {
          text: "Tarjetas",
          icon: "FiCreditCard",
          subItems: [
            {
              text: "Tarjeta de Débito",
              href: "/productos/tarjeta/tarjeta-de-debito",
              image: "https://images.unsplash.com/photo-1601597111158-f1446042c8fc?ixlib=rb-4.0.3&auto=format&fit=crop&w=300&q=80",
              category: "debit"
            }
          ],
          image: "https://images.unsplash.com/photo-1563013544-824ae1b704d3?ixlib=rb-4.0.3&auto=format&fit=crop&w=300&q=80"
        },
        {
          text: "Certificados",
          icon: "FiAward",
          subItems: [
            {
              text: "Certificado Financiero",
              href: "/productos/certificado/certificado-financiero",
              image: "https://images.unsplash.com/photo-1611095566888-f1446042c8fc?ixlib=rb-4.0.3&auto=format&fit=crop&w=300&q=80",
              category: "financial"
            }
          ],
          image: "https://images.unsplash.com/photo-1607863680198-23d4b2565df0?ixlib=rb-4.0.3&auto=format&fit=crop&w=300&q=80"
        },
        {
          text: "Préstamos",
          icon: "FiTrendingUp",
          subItems: [
            {
              text: "Préstamo de Consumo",
              href: "/productos/prestamo/prestamo-de-consumo",
              image: "https://images.unsplash.com/photo-1450101499163-c8848c66ca85?ixlib=rb-4.0.3&auto=format&fit=crop&w=300&q=80",
              category: "consumer"
            },
            {
              text: "Préstamos Comercial",
              href: "/productos/prestamo/prestamos-comercial",
              image: "https://images.unsplash.com/photo-1560518883-ce09059eeffa?ixlib=rb-4.0.3&auto=format&fit=crop&w=300&q=80",
              category: "commercial"
            }
          ],
          image: "https://images.unsplash.com/photo-1554224155-8947307dabb2?ixlib=rb-4.0.3&auto=format&fit=crop&w=300&q=80"
        }
      ];
    }
  }
};
