import { createSlice } from '@reduxjs/toolkit';
import { fetchWithBearer } from '../../api';

const initialState = {
  user: null,
  selectedAccount: null,
  availableAccounts: [],
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
    authPending(state, action) {
      return {
        ...state,
        isLoading: true,
        dataReady: false,
      }
    },
    loginSuccess(state, action) {
      return {
        ...state,
        isLoading: false,
        dataReady: true,
        accessToken: action.payload.token,
        refreshToken: action.payload.refreshToken,
        availableAccounts: action.payload.availableAccounts,
      }
    },
    authError(state, action) {
      return {
        ...state,
        isLoading: false,
        dataReady: false,
        error: action.payload
      }
    },
    getAccountsSuccess(state, action) {
      return {
        ...state,
        isLoading: false,
        dataReady: true,
        availableAccounts: action.payload.availableAccounts
      }
    },
    logout(state, action)  {
      return {
        ...state,
        user: null,
        selectedAccount: null,
        availableAccounts: [],
        accessToken: "",
        refreshToken: "",
      }
    }
  },
})

const { authPending, loginSuccess, getAccountsSuccess, authError } = authSlice.actions;

export const login = (username, password) => async (dispatch) => {
  dispatch(authPending());
  let token;
  let refreshToken;

  let response = await fetch('http://localhost:8000/api/token/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ username, password })
  });

  if (response.ok) {
    const resp = await response.json();

    localStorage.setItem("token", resp.access);
    localStorage.setItem("refreshToken", resp.refresh);

    token = resp.access;
    refreshToken = resp.refresh;
  } else {
    dispatch(authError("Login Failed"));
  }

  response = await fetchWithBearer('http://localhost:8000/api/users/accounts/');

  if (response.ok) {
    const resp = await response.json();

    dispatch(loginSuccess({ token, refreshToken, availableAccounts: resp }));
  } else {
    dispatch(authError("Login Failed"));
  }
}

export const logout = () => async (dispatch) => {
  localStorage.removeItem("token");
  localStorage.removeItem("refreshToken");
  dispatch(logout());
}

export const getAccounts = () => async (dispatch) => {
  dispatch(authPending());

  let response = await fetchWithBearer('http://localhost:8000/api/users/accounts/');

  if (response.ok) {
    const resp = await response.json();

    dispatch(getAccountsSuccess({ availableAccounts: resp }));
  } else {
    dispatch(authError("Login Failed"));
  }
}

export const selectAccount = (id) => async (dispatch) => {

}

export default authSlice.reducer;
