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
      return {
        ...state,
        isLoading: true
      }
    },
    success(state, action) {
      return {
        ...state,
        isLoading: false,
        dataReady: true,
        accessToken: action.payload.accessToken,
        refreshToken: action.payload.refreshToken
      }
    },
    failed(state, action) {
      return {
        ...state,
        isLoading: false,
        error: action.payload
      }
    },
    logout(state, action)  {
      return {
        ...state,
        accessToken: "",
        refreshToken: "",
      }
    }
  },
})

const { pending, success, failed } = authSlice.actions;

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

    localStorage.setItem("token", resp.access);
    localStorage.setItem("refresh_token", resp.refresh);
    dispatch(success(resp));
  } else {
    dispatch(failed("Login Failed"));
  }
}

export const logout = () => async (dispatch) => {
  localStorage.removeItem("token");
  localStorage.removeItem("refresh_token");
  dispatch(logout());
}

export default authSlice.reducer;
