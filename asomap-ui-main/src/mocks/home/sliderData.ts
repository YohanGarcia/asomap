import { SliderItem } from '@interfaces';

// Desktop Images (1920px width)
import ImageDesktop1 from '@assets/images/slider/desktop/AsomapBanking.jpg';
import ImageDesktop2 from '@assets/images/slider/desktop/Comerciales.jpg';
import ImageDesktop3 from '@assets/images/slider/desktop/Microcredito.jpg';
import ImageDesktop4 from '@assets/images/slider/desktop/Pekes.jpg';
import ImageDesktop5 from '@assets/images/slider/desktop/PrestamoPersonal.jpg';
import ImageDesktop6 from '@assets/images/slider/desktop/Prousuario.jpg';

// Tablet Images (1024px width)
import imageTablet1 from '@assets/images/slider/tablet/AsomapBanking.jpg';
import imageTablet2 from '@assets/images/slider/tablet/Comerciales.jpg';
import imageTablet3 from '@assets/images/slider/tablet/Microcredito.jpg';
import imageTablet4 from '@assets/images/slider/tablet/Pekes.jpg';
import imageTablet5 from '@assets/images/slider/tablet/PrestamoPersonal.jpg';
import imageTablet6 from '@assets/images/slider/tablet/Prousuario.jpg';

// Mobile Images (640px width)
import imageMobile1 from '@assets/images/slider/mobile/AsomapBanking.jpg';
import imageMobile2 from '@assets/images/slider/mobile/Comerciales.jpg';
import imageMobile3 from '@assets/images/slider/mobile/Microcredito.jpg';
import imageMobile4 from '@assets/images/slider/mobile/Pekes.jpg';
import imageMobile5 from '@assets/images/slider/mobile/PrestamoPersonal.jpg';
import imageMobile6 from '@assets/images/slider/mobile/Prousuario.jpg';

export const slides: SliderItem[] = [
    {
        id: 1,
        image: ImageDesktop1,
        imageTablet: imageTablet1,
        imageMobile: imageMobile1,
        alt: 'Asomap Banking'
    },
    {
        id: 2,
        image: ImageDesktop2,
        imageTablet: imageTablet2,
        imageMobile: imageMobile2,
        alt: 'Créditos Comerciales'
    },
    {
        id: 3,
        image: ImageDesktop3,
        imageTablet: imageTablet3,
        imageMobile: imageMobile3,
        alt: 'Créditos Microcrédito'
    },
    {
        id: 4,
        image: ImageDesktop4,
        imageTablet: imageTablet4,
        imageMobile: imageMobile4,
        alt: 'Cuentas Pekes'
    },
    {
        id: 5,
        image: ImageDesktop5,
        imageTablet: imageTablet5,
        imageMobile: imageMobile5,
        alt: 'Préstamo Personal'
    },
    {
        id: 6,
        image: ImageDesktop6,
        imageTablet: imageTablet6,
        imageMobile: imageMobile6,
        alt: 'Prousuario'
    }
];
