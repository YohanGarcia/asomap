// interface del banner
export interface IBannerAPI {
    id: number;
    title: string;
    description: string;
    button1_name: string;
    button1_url: string;
    button2_name: string;
    button2_url: string;
    is_active: boolean;
    order: number;
    slug: string;
    created_at: string;
    updated_at: string;
  }
  
export interface IBannerDataAPI {
    id: number;
    title: string;
    description: string;
    button1Name: string;
    button1Url: string;
    button2Name: string;
    button2Url: string;
    isActive: boolean;
    order: number;
    slug: string;
  }