import { createSlice } from '@reduxjs/toolkit';

const initialState = {
  user: null,
  accessToken: "",
  refreshToken: "",
  isLoading: false,
  dataReady: false,
  error: null,
};

const authSlice = createSlice({
  name: 'auth',
  initialState,
  reducers: {
    pending(state, action) {
      state.isLoading = true;
    },
    success(state, action) {
      state.isLoading = false;
      state.dataReady = true;
      state.accessToken = action.payload.accessToken;
      state.refreshToken = action.payload.refreshToken;
      state.error = null;
    },
    failed(state, action) {
      state.isLoading = false;
      state.error = action.payload;  
    },
    logout(state, action)  {
      state.accessToken = "";
      state.refreshToken = "";
    }
  },
})

export const { pending, success, failed } = authSlice.actions;
export default authSlice.reducer;

export const login = (username, password) => async (dispatch) => {
  dispatch(pending());

  const response = await fetch('http://localhost:8000/api/token/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ username, password })
  });

  if (response.ok) {
    const resp = await response.json();
    dispatch(success(resp));
  } else {
    dispatch(failed("Login Failed"));
  }
}