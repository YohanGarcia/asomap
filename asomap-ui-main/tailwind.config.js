/** @type {import('tailwindcss').Config} */
import aspectRatio from '@tailwindcss/aspect-ratio';

export default {
  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {
      screens: {
        'xxs': '360px',
        'xs': '480px',
        'sm': '640px',
        'md': '768px',
        'lg': '1024px',
        'xl': '1280px',
        '2xl': '1536px',
      },
      fontFamily: {
        sans: ['Open Sans', 'sans-serif'],
        heading: ['Open Sans', 'sans-serif'],
        body: ['Open Sans', 'sans-serif'],
      },
      colors: {
        primary: {
          DEFAULT: "#2D4394",
          accent: "#F47821",
          light: "#4A69BD",
          dark: "#1C3167",
        },
        secondary: {
          DEFAULT: "#F4A649",
          light: "#F1F1F1",
          dark: "#D28A3D",
        },
        neutral: {
          100: "#0A0A0A",
          200: "#4F4D4D",
          300: "#6A6767",
          400: "#9A9A9A",
        },
        background: {
          light: "#FFFFFF",
          dark: "#F5F5F5",
        },
      },
      fontSize: {
        'xs': ['0.75rem', { lineHeight: '1rem' }],
        'sm': ['0.875rem', { lineHeight: '1.25rem' }],
        'base': ['1rem', { lineHeight: '1.5rem' }],
        'lg': ['1.125rem', { lineHeight: '1.75rem' }],
        'xl': ['1.25rem', { lineHeight: '1.75rem' }],
        '2xl': ['1.5rem', { lineHeight: '2rem' }],
        '3xl': ['1.875rem', { lineHeight: '2.25rem' }],
        '4xl': ['2.25rem', { lineHeight: '2.5rem' }],
      },
      spacing: {
        '128': '32rem',
        '144': '36rem',
      },
      aspectRatio: {
        'mobile': '4/3',    // Mobile aspect ratio
        'tablet': '16/9',   // Tablet aspect ratio
        'desktop': '21/9',  // Desktop aspect ratio
      },
      height: {
        'slider-mobile': '400px',
        'slider-tablet': '500px',
        'slider-desktop': '600px',
      },
      minHeight: {
        'slider-mobile': '400px',
        'slider-tablet': '500px',
        'slider-desktop': '600px',
      },
      maxHeight: {
        'slider-mobile': '480px',
        'slider-tablet': '576px',
        'slider-desktop': '820px',
      },
      width: {
        'slider-mobile': '640px',
        'slider-tablet': '1024px',
        'slider-desktop': '1920px',
      },
      borderRadius: {
        'sm': '0.125rem',
        DEFAULT: '0.25rem',
        'md': '0.375rem',
        'lg': '0.5rem',
        'xl': '0.75rem',
        '2xl': '1rem',
        'slider': {
          'sm': '20px',
          'md': '30px',
          'lg': '50px',
        },
      },
      boxShadow: {
        'sm': '0 1px 2px 0 rgba(0, 0, 0, 0.05)',
        DEFAULT: '0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px 0 rgba(0, 0, 0, 0.06)',
        'md': '0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)',
        'lg': '0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)',
      },
    },
  },
  plugins: [
    aspectRatio,
  ],
}