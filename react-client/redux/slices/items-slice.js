import { createSlice } from '@reduxjs/toolkit';
import { fetchWithBearer } from '../../api';

const initialState = {
  allItems: [],
  singleItem: {},
  isLoading: false,
  dataReady: false,
  error: null,
};

const itemsSlice = createSlice({
  name: 'items',
  initialState,
  reducers: {
    pending(state, action) {
      return {
        ...state,
        isLoading: true
      }
    },
    getAllSuccess(state, action) {
      return {
        ...state,
        isLoading: false,
        dataReady: true,
        allItems: action.payload,
      }
    },
    getSingleSuccess(state, action) {
      return {
        ...state,
        isLoading: false,
        dataReady: true,
        singleItem: action.payload,
      }
    },
    failed(state, action) {
      return {
        ...state,
        isLoading: false,
        error: action.payload
      }
    },
  },
})

const { pending, getAllSuccess, failed } = itemsSlice.actions;

export const getItems = () => async (dispatch) => {
  dispatch(pending());

  const response = await fetchWithBearer('http://localhost:8000/api/items/');

  if (response.ok) {
    const resp = await response.json();
    dispatch(getAllSuccess(resp));
  } else {
    dispatch(failed("Get Items Failed"));
  }
}

export const getItem = (id) => async (dispatch) => {
  dispatch(pending());

  const response = await fetchWithBearer(`http://localhost:8000/api/items/${id}/`);

  if (response.ok) {
    const resp = await response.json();
    dispatch(getSingleSuccess(resp));
  } else {
    dispatch(failed("Get Item Failed"));
  }
}

export default itemsSlice.reducer;