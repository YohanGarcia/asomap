import React, { useEffect, useState } from 'react';
import { motion } from 'framer-motion';
import { useParams, useNavigate } from 'react-router-dom';
import { INewsData, INewsMedia, INewsContent } from '@/interfaces/news.interface';
import { newsService } from '@/api';

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
  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 my-8">
      {media.map((item, index) => (
        <div key={index} className="relative">
          {item.type === 'image' ? (
            <div className="group relative overflow-hidden rounded-lg">
              <img
                src={item.url}
                alt={item.caption || ''}
                className="w-full h-64 object-cover transition-transform duration-300 group-hover:scale-105"
              />
              {item.caption && (
                <div className="absolute bottom-0 left-0 right-0 bg-black bg-opacity-50 text-white p-2 text-sm">
                  {item.caption}
                </div>
              )}
            </div>
          ) : (
            <div className="relative aspect-video">
              <iframe
                src={item.url}
                className="absolute inset-0 w-full h-full rounded-lg"
                allowFullScreen
                title={item.caption || `Video ${index + 1}`}
              />
            </div>
          )}
        </div>
      ))}
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
            src={link.image}
            alt={String(link.title)}
            className="w-full h-48 object-cover rounded-[20px] sm:rounded-[30px] lg:rounded-[50px]"
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
            src={newsItem.image}
            alt={String(newsItem.title)}
            className="w-full h-full object-cover"
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
            <div className="mt-12">
              <h2 className="text-2xl font-bold text-primary mb-4">Enlaces Relacionados</h2>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                {newsItem.relatedLinks.map((link: any, index: number) => (
                  <a
                    key={index}
                    href={link.url}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="p-4 border rounded-lg hover:bg-gray-50 transition-colors"
                  >
                    <h3 className="font-semibold text-primary mb-2">{link.title}</h3>
                    {link.description && (
                      <p className="text-gray-600 text-sm">{link.description}</p>
                    )}
                  </a>
                ))}
              </div>
            </div>
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
