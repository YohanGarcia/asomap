import { IconType } from 'react-icons';

export interface IDebitCardProps {
    bannerImage: string;
    cardImage: string;
    title: string;
    description: string;
}

export interface IDebitCardFeature {
    icon: IconType;
    title: string;
    description: string;
}