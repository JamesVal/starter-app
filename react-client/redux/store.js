import { configureStore } from '@reduxjs/toolkit';
import authReducer from './slices/auth-slice';
import itemsReducer from './slices/items-slice';

const store = configureStore({
  reducer: {
    auth: authReducer,
    items: itemsReducer,
  }
})

export default store;