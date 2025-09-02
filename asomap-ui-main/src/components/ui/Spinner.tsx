import React from 'react';

interface SpinnerProps {
  className?: string;
}

export const Spinner: React.FC<SpinnerProps> = ({ className = '' }) => {
  return (
    <div 
      className={`animate-spin rounded-full h-12 w-12 border-t-4 border-b-4 border-primary ${className}`}
    />
  );
};
