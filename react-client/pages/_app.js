// pages/_app.js
import React from 'react';
import { AuthProvider } from '../contexts/AuthContext';

function CustomApp({ Component, pageProps, router }) {
  return (
    <AuthProvider>
      <Component {...pageProps} />
    </AuthProvider>
  );
}

export default CustomApp;
