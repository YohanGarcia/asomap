export interface SliderItem {
    id: number;
    image: string;
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
