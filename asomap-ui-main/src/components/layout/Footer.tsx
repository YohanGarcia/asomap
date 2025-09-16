import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { footerData } from '@/mocks';
import { socialNetworksService, contactsService } from '@/api';
import type { ISocialNetworkData, IContactData } from '@/interfaces';
import * as FaIcons from 'react-icons/fa';

export const Footer: React.FC = () => {
    const [socialNetworks, setSocialNetworks] = useState<ISocialNetworkData[]>([]);
    const [contacts, setContacts] = useState<IContactData[]>([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const fetchData = async () => {
            try {
                setLoading(true);
                console.log('🔄 Fetching footer data...');
                
                const [socialNetworksResponse, contactsResponse] = await Promise.all([
                    socialNetworksService.getAllSocialNetworks(),
                    contactsService.getAllContacts()
                ]);
                
                console.log('📱 Social Networks Response:', socialNetworksResponse);
                console.log('📞 Contacts Response:', contactsResponse);
                
                setSocialNetworks(socialNetworksResponse.results);
                setContacts(contactsResponse.results);
                
                console.log('✅ Footer data loaded successfully');
            } catch (error) {
                console.error('❌ Error fetching footer data:', error);
            } finally {
                setLoading(false);
            }
        };

        fetchData();
    }, []);

    // Función para obtener el icono de React Icons
    const getIconComponent = (iconName: string) => {
        const IconComponent = (FaIcons as any)[iconName];
        if (IconComponent) {
            return IconComponent;
        }
        return FaIcons.FaQuestion; // Fallback icon
    };

    // Debug logs
    console.log('🔍 Footer State:', { loading, socialNetworks, contacts });

    return (
        <footer className="bg-gradient-to-b from-white to-gray-50 text-gray-800 py-16">
            <div className="container mx-auto px-4 sm:px-6 lg:px-8">
                {/* Grid principal */}
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-x-8 gap-y-12">
                    {Object.entries(footerData.sections).map(([key, section]) => (
                        <div key={key} className="space-y-6">
                            <h3 className="text-lg font-semibold text-gray-900 border-b border-gray-200 pb-2">
                                {section.title}
                            </h3>
                            {section.items ? (
                                <ul className="space-y-3">
                                    {section.items.map((item, index) => (
                                        <li
                                            key={index}
                                            className="hover:text-primary transition-colors duration-300 flex items-center text-gray-600 hover:translate-x-1 transform transition-transform"
                                        >
                                            {item.isExternalLink ? (
                                                <a
                                                    href={item.to}
                                                    target="_blank"
                                                    rel="noopener noreferrer"
                                                    className="flex items-center space-x-2"
                                                >
                                                    {item.icon && React.createElement(item.icon, {
                                                        className: "w-4 h-4 text-primary"
                                                    })}
                                                    <span className="text-sm">{item.text}</span>
                                                </a>
                                            ) : (
                                                <Link
                                                    to={item.to || '#'}
                                                    className="flex items-center space-x-2"
                                                >
                                                    {item.icon && React.createElement(item.icon, {
                                                        className: "w-4 h-4 text-primary"
                                                    })}
                                                    <span className="text-sm">{item.text}</span>
                                                </Link>
                                            )}
                                        </li>
                                    ))}
                                </ul>
                            ) : (
                                key === 'follow' ? (
                                    loading ? (
                                        <div className="flex space-x-6">
                                            {[...Array(5)].map((_, index) => (
                                                <div
                                                    key={index}
                                                    className="w-6 h-6 bg-gray-200 rounded animate-pulse"
                                                />
                                            ))}
                                        </div>
                                    ) : socialNetworks.length > 0 ? (
                                        <div className="flex space-x-6">
                                            {socialNetworks.map((socialNetwork) => {
                                                const IconComponent = getIconComponent(socialNetwork.icon);
                                                return (
                                                    <a
                                                        key={socialNetwork.id}
                                                        href={socialNetwork.url}
                                                        target="_blank"
                                                        rel="noopener noreferrer"
                                                        className="transform hover:scale-110 transition-transform duration-300 text-gray-600 hover:text-primary"
                                                        title={socialNetwork.name}
                                                    >
                                                        <IconComponent className="w-6 h-6" />
                                                    </a>
                                                );
                                            })}
                                        </div>
                                    ) : (
                                        <div className="text-gray-500 text-sm">No hay redes sociales disponibles</div>
                                    )
                                ) : section.icons && (
                                    <div className="flex space-x-6">
                                        {section.icons.map((icon, index) => (
                                            <a
                                                key={index}
                                                href={icon.url}
                                                target="_blank"
                                                rel="noopener noreferrer"
                                                className={`${icon.className} transform hover:scale-110 transition-transform duration-300`}
                                            >
                                                {React.createElement(icon.icon, {
                                                    className: "w-6 h-6"
                                                })}
                                            </a>
                                        ))}
                                    </div>
                                )
                            )}
                            {/* Sección de Contactos desde API */}
                            {key === 'follow' && (
                                <div className="space-y-4 mt-8">
                                    <h3 className="text-lg font-semibold text-gray-900 border-b border-gray-200 pb-2">
                                        Contacto
                                    </h3>
                                    {loading ? (
                                        <div className="space-y-3">
                                            {[...Array(3)].map((_, index) => (
                                                <div key={index} className="flex items-center space-x-3">
                                                    <div className="w-4 h-4 bg-gray-200 rounded animate-pulse" />
                                                    <div className="h-4 bg-gray-200 rounded animate-pulse flex-1 max-w-32" />
                                                </div>
                                            ))}
                                        </div>
                                    ) : contacts.length > 0 ? (
                                        <div className="space-y-3">
                                            {contacts.map((contact) => {
                                                const IconComponent = getIconComponent(contact.icon);
                                                return (
                                                    <a
                                                        key={contact.id}
                                                        href={contact.url}
                                                        target={contact.url.startsWith('http') ? '_blank' : undefined}
                                                        rel={contact.url.startsWith('http') ? 'noopener noreferrer' : undefined}
                                                        className="flex items-center space-x-3 text-gray-600 hover:text-primary transition-colors duration-300 group"
                                                    >
                                                        <span className="flex-shrink-0 text-primary group-hover:scale-110 transition-transform duration-300">
                                                            <IconComponent className="w-4 h-4" />
                                                        </span>
                                                        <span className="text-sm">{contact.name}</span>
                                                    </a>
                                                );
                                            })}
                                        </div>
                                    ) : (
                                        <div className="text-gray-500 text-sm">No hay contactos disponibles</div>
                                    )}
                                </div>
                            )}
                        </div>
                    ))}
                </div>

                <hr className="my-12 border-gray-200" />

                {/* Footer bottom */}
                <div className="flex flex-col lg:flex-row items-center justify-between space-y-8 lg:space-y-0">
                    <div className="text-center lg:text-left space-y-4">
                        <img
                            src={footerData.company.logo}
                            alt={footerData.company.name}
                            className="w-48 mx-auto lg:mx-0 hover:opacity-90 transition-opacity duration-300"
                        />
                        <p className="text-sm text-gray-500">
                            <span className="flex items-center gap-1">
                                {footerData.company.copyright.icon && React.createElement(footerData.company.copyright.icon, {
                                    className: "w-4 h-4"
                                })}
                                {new Date().getFullYear()}, {footerData.company.copyright.text}
                            </span>
                            <br />
                            <span className="text-xs">{footerData.company.copyright.rights}</span>
                        </p>
                    </div>

                    {/* Certificaciones */}
                    <div className="flex flex-col sm:flex-row items-center space-y-6 sm:space-y-0 sm:space-x-8">
                        {footerData.company.certifications.map((cert, index) => (
                            <div key={index} className="group relative">
                                <a
                                    href={cert.url}
                                    target="_blank"
                                    rel="noopener noreferrer"
                                    className="w-24 h-24 rounded-lg overflow-hidden bg-white shadow-md hover:shadow-lg transition-all duration-300 block"
                                >
                                    <img
                                        src={cert.image}
                                        alt={cert.alt}
                                        className={cert.className}
                                    />
                                </a>
                            </div>
                        ))}
                    </div>
                </div>
            </div>
        </footer>
    );
};