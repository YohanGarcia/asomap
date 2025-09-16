export interface SliderItem {
    id: number;
    image: string | null;
    imageTablet?: string;
    imageMobile?: string;
    alt?: string;
}

export interface ICarousel {
    autoSlide?: boolean;
    autoSlideInterval?: number;
    slides: SliderItem[];
    fullScreen?: boolean;
    className?: string;
    minHeight?: string;
}
