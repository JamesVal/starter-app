// pages/_app.js
import React from 'react';
import { Provider } from 'react-redux';
import store from '../redux/store';

function CustomApp({ Component, pageProps, router }) {
  return (
    <Provider store={store}>
      <Component {...pageProps} />
    </Provider>
  );
}

export default CustomApp;
