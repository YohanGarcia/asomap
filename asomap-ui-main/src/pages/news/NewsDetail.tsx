import React, { useEffect, useState } from 'react';
import { motion } from 'framer-motion';
import { useParams, useNavigate } from 'react-router-dom';
import { INewsData, INewsMedia, INewsContent } from '@/interfaces/news.interface';
import { newsService } from '@/api';
import { getImageUrl, getMediaUrl } from '@/utils/environment';

const sectionVariants = {
  hidden: { opacity: 0, y: 20 },
  visible: {
    opacity: 1,
    y: 0,
    transition: {
      duration: 0.5,
    },
  },
};

const MediaGallery: React.FC<{ media: INewsMedia[] }> = ({ media }) => {
  // Función para determinar si es imagen o video basado en la extensión del archivo
  const getMediaType = (url: string, declaredType: string) => {
    const imageExtensions = ['.jpg', '.jpeg', '.png', '.gif', '.webp', '.svg'];
    const videoExtensions = ['.mp4', '.webm', '.ogg', '.avi', '.mov'];
    
    const extension = url.toLowerCase().substring(url.lastIndexOf('.'));
    
    if (imageExtensions.includes(extension)) {
      return 'image';
    } else if (videoExtensions.includes(extension)) {
      return 'video';
    }
    
    // Si no podemos determinar por extensión, usar el tipo declarado
    return declaredType;
  };

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 my-8">
      {media.map((item, index) => {
        const actualType = getMediaType(item.url, item.type);
        const mediaUrl = actualType === 'video' ? getMediaUrl(item.url) : getImageUrl(item.url);
        
        console.log(`Media item ${index}:`, {
          originalUrl: item.url,
          processedUrl: mediaUrl,
          declaredType: item.type,
          detectedType: actualType,
          expectedWorkingUrl: 'http://localhost:8080/media/news/Asociaci%C3%B3n_Mocana.mp4',
          urlsMatch: mediaUrl === 'http://localhost:8080/media/news/Asociaci%C3%B3n_Mocana.mp4'
        });
        
        return (
          <div key={index} className="relative">
            {actualType === 'image' ? (
              <div className="group relative overflow-hidden rounded-lg">
                <img
                  src={mediaUrl}
                  alt={item.caption || ''}
                  className="w-full h-64 object-cover transition-transform duration-300 group-hover:scale-105"
                  onError={(e) => {
                    console.error('Error loading image:', item.url, '->', mediaUrl);
                    e.currentTarget.style.display = 'none';
                  }}
                />
                {item.caption && (
                  <div className="absolute bottom-0 left-0 right-0 bg-black bg-opacity-50 text-white p-2 text-sm">
                    {item.caption}
                  </div>
                )}
              </div>
            ) : (
              <div className="relative aspect-video bg-gray-100 rounded-lg">
                {/* Debug info - remove in production */}
             {/* {   <div className="absolute top-2 left-2 bg-black bg-opacity-75 text-white text-xs p-1 rounded z-10">
                  <div>URL: {mediaUrl}</div>
                  <div>Type: {actualType}</div>
                  <button 
                    onClick={() => {
                      console.log('Testing video URL:', mediaUrl);
                      window.open(mediaUrl, '_blank');
                    }}
                    className="bg-blue-500 text-white px-2 py-1 rounded text-xs mt-1"
                  >
                    Test URL
                  </button>
                </div>} */}
                
            
                
                {/* Video original con URL dinámica */}
                <video
                  src={mediaUrl}
                  className="w-full h-full rounded-lg mt-2"
                  controls
                  preload="metadata"
                  title={item.caption || `Video ${index + 1}`}
                  onError={(e) => {
                    console.error('Error loading video:', {
                      originalUrl: item.url,
                      processedUrl: mediaUrl,
                      error: e,
                      videoElement: e.currentTarget
                    });
                    // Mostrar mensaje de error en lugar de intentar mostrar como imagen
                    const target = e.currentTarget as HTMLVideoElement;
                    target.style.display = 'none';
                    const parent = target.parentElement;
                    if (parent) {
                      parent.innerHTML = `
                        <div class="flex items-center justify-center h-full bg-gray-200 rounded-lg">
                          <div class="text-center text-gray-500">
                            <svg class="w-12 h-12 mx-auto mb-2" fill="currentColor" viewBox="0 0 20 20">
                              <path d="M2 6a2 2 0 012-2h6l2 2h6a2 2 0 012 2v6a2 2 0 01-2 2H4a2 2 0 01-2-2V6zM14.553 7.106A1 1 0 0014 8v4a1 1 0 00.553.894l2 1A1 1 0 0018 13V7a1 1 0 00-1.447-.894l-2 1z"/>
                            </svg>
                            <p class="text-sm">Error al cargar el video</p>
                            <p class="text-xs mt-1">URL: ${mediaUrl}</p>
                          </div>
                        </div>
                      `;
                    }
                  }}
                  onLoadStart={() => {
                    console.log('Video loading started:', mediaUrl);
                  }}
                  onCanPlay={() => {
                    console.log('Video can play:', mediaUrl);
                  }}
                  onLoadedData={() => {
                    console.log('Video data loaded:', mediaUrl);
                  }}
                  onLoadedMetadata={() => {
                    console.log('Video metadata loaded:', mediaUrl);
                  }}
                />
                {item.caption && (
                  <div className="absolute bottom-0 left-0 right-0 bg-black bg-opacity-50 text-white p-2 text-sm rounded-b-lg">
                    {item.caption}
                  </div>
                )}
              </div>
            )}
          </div>
        );
      })}
    </div>
  );
};

const ContentSection: React.FC<{ content: INewsContent[] }> = ({ content }) => {
  return (
    <div className="prose max-w-none">
      {content.map((item, index) => {
        switch (item.type) {
          case 'paragraph':
            return (
              <p key={index} className="text-lg leading-relaxed mb-6">
                {item.content}
              </p>
            );
          case 'subtitle':
            return (
              <h2 key={index} className="text-2xl font-bold text-primary mt-8 mb-4">
                {item.content}
              </h2>
            );
          case 'quote':
            return (
              <blockquote key={index} className="border-l-4 border-primary pl-4 italic my-6">
                {item.content}
              </blockquote>
            );
          case 'list':
            return (
              <ul key={index} className="list-disc pl-6 my-4">
                {Array.isArray(item.content) &&
                  item.content.map((listItem: any, listIndex: number) => (
                    <li key={listIndex} className="mb-2">
                      {listItem}
                    </li>
                  ))}
              </ul>
            );
          default:
            return null;
        }
      })}
    </div>
  );
};

const RelatedLinks: React.FC<{ links: INewsData['slides'] }> = ({ links }) => {
  const navigate = useNavigate();

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mt-8">
      {links.map((link: any) => (
        <div
          key={link.id}
          className="bg-white rounded-[20px] sm:rounded-[30px] lg:rounded-[50px] shadow-md hover:shadow-lg transition-all cursor-pointer"
          onClick={() => navigate(`/novedades/ultimas-noticias/${link.id}`)}
        >
          <img
            src={getImageUrl(link.image)}
            alt={String(link.title)}
            className="w-full h-48 object-cover rounded-[20px] sm:rounded-[30px] lg:rounded-[50px]"
            onError={(e) => {
              console.error('Error loading related news image:', link.image);
              e.currentTarget.style.display = 'none';
            }}
          />
          <div className="p-4">
            <h3 className="text-lg font-semibold text-primary mb-2">{link.title}</h3>
            {link.date && <p className="text-sm text-gray-600">{link.date}</p>}
          </div>
        </div>
      ))}
    </div>
  );
};

const NewsDetail: React.FC = () => {
  const [newsData, setNewsData] = useState<INewsData | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const { id } = useParams<{ id: string }>();
  const navigate = useNavigate();

  useEffect(() => {
    const fetchNewsData = async () => {
      try {
        setLoading(true);
        setError(null);
        const data = await newsService.getNews();
        setNewsData(data);
      } catch (err) {
        console.error('Error loading news data:', err);
        setError('Error al cargar los datos de la noticia');
        setNewsData(newsData); // Fallback a mock data
      } finally {
        setLoading(false);
      }
    };

    fetchNewsData();
  }, []);

  useEffect(() => {
    if (!loading && newsData) {
      const newsItem = newsData.slides.find((item: any) => item.id.toString() === id);
      if (!newsItem) {
        navigate('/novedades/ultimas-noticias');
      }
    }
    window.scrollTo(0, 0);
  }, [loading, newsData, id, navigate]);

  // Estado de carga
  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-gray-50">
        <div className="text-center">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-primary mx-auto mb-4"></div>
          <p className="text-gray-600">Cargando noticia...</p>
        </div>
      </div>
    );
  }

  // Estado de error
  if (error) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-gray-50">
        <div className="text-center">
          <div className="text-red-500 text-6xl mb-4">⚠️</div>
          <h2 className="text-xl font-semibold text-gray-800 mb-2">Error</h2>
          <p className="text-gray-600 mb-4">{error}</p>
          <button
            onClick={() => navigate('/novedades/ultimas-noticias')}
            className="bg-primary text-white px-4 py-2 rounded-lg hover:bg-primary/80 transition-colors"
          >
            Volver a Noticias
          </button>
        </div>
      </div>
    );
  }

  if (!newsData) return null;

  const newsItem = newsData.slides.find((item: any) => item.id.toString() === id);
  const relatedNews = newsData.slides
    .filter((item: any) => item.id.toString() !== id)
    .slice(0, 3);

  if (!newsItem) return null;

  return (
    <motion.div
      initial="hidden"
      animate="visible"
      variants={sectionVariants}
      className="relative"
    >
      <div className="font-sans bg-white">
        {/* Banner Section */}
        <div className="relative h-[360px] sm:h-[400px] md:h-[450px] lg:h-[500px] -mt-[80px] rounded-b-[30px] sm:rounded-b-[50px] lg:rounded-b-[80px] overflow-hidden">
          <img
            src={getImageUrl(newsItem.image)}
            alt={String(newsItem.title)}
            className="w-full h-full object-cover"
            onError={(e) => {
              console.error('Error loading banner image:', newsItem.image);
              e.currentTarget.style.display = 'none';
            }}
          />
          <div className="absolute inset-0 bg-gradient-to-t from-black/50 to-transparent rounded-b-[30px] sm:rounded-b-[50px] lg:rounded-b-[80px]" />
          <div className="absolute bottom-0 left-0 right-0 p-6 text-white">
            {newsItem.category && (
              <span className="inline-block bg-primary px-3 py-1 rounded-full text-sm mb-4">
                {newsItem.category}
              </span>
            )}
            <h1 className="text-4xl font-bold mb-2">{newsItem.title}</h1>
            <div className="flex items-center gap-4">
              {newsItem.author && <span>{newsItem.author}</span>}
              {newsItem.date && <span>{newsItem.date}</span>}
            </div>
          </div>
        </div>

        <div className="container mx-auto px-4 py-8">
          {/* Back to News Button */}
          <div className="container mx-auto px-4 py-6">
            <button
              onClick={() => navigate('/novedades/ultimas-noticias')}
              className="flex items-center gap-2 text-primary hover:text-primary/80 transition-colors"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                className="h-5 w-5"
                viewBox="0 0 20 20"
                fill="currentColor"
              >
                <path
                  fillRule="evenodd"
                  d="M9.707 16.707a1 1 0 01-1.414 0l-6-6a1 1 0 010-1.414l6-6a1 1 0 011.414 1.414L5.414 9H17a1 1 0 110 2H5.414l4.293 4.293a1 1 0 010 1.414z"
                  clipRule="evenodd"
                />
              </svg>
              Volver a Noticias
            </button>
          </div>

          {/* Tags */}
          {newsItem.tags && newsItem.tags.length > 0 && (
            <div className="flex flex-wrap gap-2 mb-6">
              {newsItem.tags.map((tag: any, index: number) => (
                <span
                  key={index}
                  className="bg-gray-100 text-gray-700 px-3 py-1 rounded-full text-sm"
                >
                  {tag}
                </span>
              ))}
            </div>
          )}

          {/* Main Content */}
          {newsItem.fullContent && <ContentSection content={newsItem.fullContent} />}

          {/* Media Gallery */}
          {newsItem.media && newsItem.media.length > 0 && (
            <>
              <h2 className="text-2xl font-bold text-primary mt-12 mb-6">Galería</h2>
              <MediaGallery media={newsItem.media} />
            </>
          )}

          {/* Related Links */}
          {newsItem.relatedLinks && newsItem.relatedLinks.length > 0 && (
            <motion.div 
              className="mt-16"
              initial="hidden"
              whileInView="visible"
              viewport={{ once: true }}
              variants={sectionVariants}
            >
              <h2 className="text-3xl font-bold text-primary mb-8 text-center">
                Enlaces Relacionados
              </h2>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                {newsItem.relatedLinks.map((link: any, index: number) => (
                  <motion.a
                    key={index}
                    href={link.url}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="group block bg-white rounded-xl shadow-md hover:shadow-lg transition-all duration-300 transform hover:-translate-y-1 border border-gray-200 overflow-hidden"
                    initial={{ opacity: 0, y: 20 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    viewport={{ once: true }}
                    transition={{ delay: index * 0.1 }}
                  >
                    <div className="p-6">
                      <div className="flex items-start gap-4">
                        {/* Icono de enlace externo */}
                        <div className="flex-shrink-0">
                          <div className="flex items-center justify-center w-10 h-10 bg-primary rounded-lg group-hover:bg-primary/80 transition-colors duration-300">
                            <svg 
                              className="w-5 h-5 text-white" 
                              fill="none" 
                              stroke="currentColor" 
                              viewBox="0 0 24 24"
                            >
                              <path 
                                strokeLinecap="round" 
                                strokeLinejoin="round" 
                                strokeWidth={2} 
                                d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" 
                              />
                            </svg>
                          </div>
                        </div>
                        
                        {/* Contenido del enlace */}
                        <div className="flex-1 min-w-0">
                          <h3 className="font-semibold text-lg text-gray-800 mb-2 group-hover:text-primary transition-colors duration-300">
                            {link.title}
                          </h3>
                          
                          {link.description && (
                            <p className="text-gray-600 text-sm leading-relaxed mb-3">
                              {link.description.length > 120 
                                ? `${link.description.substring(0, 120)}...` 
                                : link.description
                              }
                            </p>
                          )}
                          
                          {/* Indicador de enlace externo */}
                          <div className="flex items-center text-primary text-sm font-medium group-hover:translate-x-1 transition-transform duration-300">
                            <span>Visitar enlace</span>
                            <svg 
                              className="w-4 h-4 ml-1" 
                              fill="none" 
                              stroke="currentColor" 
                              viewBox="0 0 24 24"
                            >
                              <path 
                                strokeLinecap="round" 
                                strokeLinejoin="round" 
                                strokeWidth={2} 
                                d="M9 5l7 7-7 7" 
                              />
                            </svg>
                          </div>
                        </div>
                      </div>
                    </div>
                    
                    {/* Borde inferior con efecto hover */}
                    <div className="h-1 bg-gradient-to-r from-primary to-primary/50 transform scale-x-0 group-hover:scale-x-100 transition-transform duration-300 origin-left"></div>
                  </motion.a>
                ))}
              </div>
            </motion.div>
          )}

          {/* Related News */}
          {relatedNews.length > 0 && (
            <div className="mt-16">
              <h2 className="text-2xl font-bold text-primary mb-6">Noticias Relacionadas</h2>
              <RelatedLinks links={relatedNews} />
            </div>
          )}
        </div>
      </div>
    </motion.div>
  );
};

export default NewsDetail;