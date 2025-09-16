export const ENDPOINTS = {
    COLLECTIONS: {
        ABOUT: {
            // Implemented API endpoints
            HERO: '/about/hero/',
            ABOUT_US: '/about/quienes-somos/',
            OUR_HISTORY: '/about/nuestra-historia/',
            MISION: '/about/mision/',
            VISION: '/about/vision/',
            VALUES: '/about/valores/',
            DIRECTOR_BOARD: '/about/consejo-directores/',
            // Community Support endpoints
            COMMUNITY_SUPPORT: '/about/community-support/',
            COMMUNITY_CATEGORIES: '/about/community-categories/',
            COMMUNITY_INITIATIVES: '/about/community-initiatives/',
            // Mock endpoints
            FINANCIAL_STATEMENTS: '/about/financial-statements/',
            MEMORIES: '/about/memories/',
            POLICIES: '/about/policies/'
        },
        PRODUCTS: {
            ACCOUNTS: '/products/accounts/',
            LOANS: '/products/loans/',
            CARDS: '/products/cards/',
            CERTIFICATES: '/products/certificates/',
            BANNERS: '/banners/'
        },

        HOME: {
            DEBIT_CARD_PROMO: '/home/debit-card-promo/',
            EDUCATION_SECTION: '/home/education-section/',
            PEKE_ACCOUNT_SUMMARY: '/home/peke-account-summary/',
            PRODUCT_SECTION: '/home/product-section/',
            SLIDER: '/home/slider/'
        },
        LAYOUT: {
            HEADER: '/header/navigation/',
            EXCHANGE_RATE: '/header/exchange/',
            FOOTER: '/layout/footer/',
            SOCIAL_NETWORKS: '/social-networks/',
            CONTACTS: '/contacts/',
            MENU: '/layout/menu/'
        },
        LOCATIONS: {
            ALL: '/locations/'
        },
        NEWS: {
            ALL: '/news/',
            LATEST: '/news/latest/',
            PROMOTIONS: '/news/promotions/'
        },
        FINANCIAL_GUIDANCE: {
            SAVING_TIPS: '/financial-guidance/saving-tips/',
            SLIDER_SLIDES: '/financial-guidance/slider-slides/',
            FAQ: '/financial-guidance/faq/'
        },
        USER_SUPPORT: {
            RIGHTS_AND_DUTIES: '/user-support/rights-and-duties/',
            SUGGESTION_BOX: '/user-support/suggestion-box/',
            SUGGESTION_BOX_PAGE: '/user-support/suggestion-box-page/',
            PROVINCES: '/user-support/provinces/',
            FRAUD_REPORT: '/user-support/fraud-reports/',
            FRAUD_REPORT_PAGE: '/user-support/fraud-report-page/',
            CLAIM_REQUEST: '/user-support/claim-requests/',
            CLAIM_REQUEST_PAGE: '/user-support/claim-request-page/',
            SERVICE_RATES: '/user-support/service-rates/',
            SERVICE_CATEGORIES: '/user-support/service-categories/',
            ABANDONED_ACCOUNTS: '/user-support/abandoned-accounts/',
            ACCOUNT_CONTRACTS: '/user-support/account-contracts/'
        },
        SERVICES: {
            MAIN: '/services/'
        }
    }
} as const;