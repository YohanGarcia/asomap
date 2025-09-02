import React from 'react';
import { BrowserRouter } from 'react-router-dom';
import { AppRouter } from '@/router';

export const App: React.FC = () => {
  return (
    <BrowserRouter future={{ 
      v7_relativeSplatPath: true,
      v7_startTransition: true 
    }}>
      <AppRouter />
    </BrowserRouter>
  );
};
