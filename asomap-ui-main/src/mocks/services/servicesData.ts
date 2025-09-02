import { Service } from '@/interfaces';
import ImageService from '@/assets/images/service/ImageService.png';
import ImageEdenorte from '@/assets/images/service/ImageEdenorte.png';
import ImageClaro from '@/assets/images/service/claro.jpg';
import ImageDGII from '@/assets/images/service/ImageDGII.png';
import ImageTelecable from '@/assets/images/service/telecable.png';

export const servicesData: Service = {
  title: "Servicios Bancarios",
  subtitle: "Descubre todos nuestros servicios disponibles para ti",
  bannerBg: "#FBE3D2",
  searchPlaceholder: "Buscar servicios...",
  noResultsText: "No se encontraron servicios",
  internetBankingUrl: "https://www.ibanking.asomap.com.do/onlinebanking",
  internetBankingButton: "Acceder a Banca en Línea",
  items: [
    "Autocaja",
    "Pago impuestos DGII",
    "Pago servicio de teléfono",
    "Pago servicio de telecable",
    "Pago energía eléctrica",
    "Depósito nocturno",
    "Tarifario de productos y servicios"
  ],
  itemDetails: [
    {
      title: "Autocaja",
      description: "Es un servicio que te permite realizar tus transacciones desde tu propio vehículo. Disponible en las sucursales de:",
      steps: [
        "Oficina Principal",
        "Cayetano Germosén",
        "San Víctor",
        "Licey al Medio"
      ],
      imageUrl: ImageService,
    },
    {
      title: "Pago impuestos DGII",
      description: "Paga todo los Impuestos de la DGII en nuestras oficina de la Asociación Mocana de Ahorros y Prestamos",
      steps: [
        "Ingresa a tu cuenta en línea o visita una sucursal",
        "Selecciona la opción de pago de impuestos DGII",
        "Ingresa el número de referencia de tu declaración",
        "Verifica los detalles y confirma el pago"
      ],
      imageUrl: ImageDGII,
    },
    {
      title: "Pago servicio de teléfono",
      description: "Paga tu factura de CLARO-CODETEL en nuestra oficina principal y cada una de nuestras sucursales, con un servicio personalizado de primera calidad.",
      steps: [
        "Accede a tu banca en línea o móvil",
        "Selecciona la opción de pago de servicios",
        "Elige tu proveedor de servicio telefónico",
        "Ingresa el número de cuenta o referencia",
        "Confirma el monto y realiza el pago"
      ],
      imageUrl: ImageClaro,
    },
    {
      title: "Pago servicio de telecable",
      description: "Paga tu factura de Televiaducto S.A. en nuestra oficina principal y en nuestras sucursales de San Víctor, Juan López y Cayetano Germosén donde te esperamos para brindarte el mejor de los servicios.",
      steps: [
        "Inicia sesión en tu cuenta bancaria en línea",
        "Busca la sección de pagos de servicios",
        "Selecciona tu proveedor de cable",
        "Ingresa tu número de cuenta de cable",
        "Verifica el monto y completa el pago"
      ],
      imageUrl: ImageTelecable,
    },
    {
      title: "Pago energía eléctrica",
      description: "Paga tu factura de EDENORTE en nuestra oficina principal y en cada una de nuestras sucursales con el mejor de los servicios.",
      steps: [
        "Accede a nuestra plataforma de banca en línea",
        "Navega hasta la sección de pago de servicios",
        "Elige tu compañía eléctrica",
        "Introduce el número de referencia de tu factura",
        "Revisa los detalles y confirma el pago"
      ],
      imageUrl: ImageEdenorte,
    },
    {
      title: "Depósito nocturno",
      description: "Es la facilidad que otorga la Asociación a sus clientes de depositar sus recursos en horario nocturno, sábado en la tarde, domingos y días feriados, con los mayores niveles de seguridad. Opera en la Oficina Principal y varias sucursales.",
      steps: [
        "Prepara tu depósito en una bolsa de seguridad especial",
        "Visita la ubicación del depósito nocturno más cercana",
        "Utiliza tu tarjeta de acceso para abrir el buzón",
        "Coloca la bolsa de depósito en el buzón",
        "Asegúrate de que el buzón se cierre completamente"
      ],
      imageUrl: ImageService,
    },
    {
      title: "Tarifario de productos y servicios",
      description: "Consulta nuestro tarifario actualizado de productos y servicios, donde encontrarás información detallada sobre tasas, comisiones y cargos.",
      steps: [],
      pdfUrl: "https://www.asomap.com.do/wp-content/uploads/2024/04/Tarifario-actualizado-a-Marzo-2024.pdf"
    }
  ]
};