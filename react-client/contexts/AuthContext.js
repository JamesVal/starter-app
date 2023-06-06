import React, { createContext, useReducer } from 'react';

const initialState = {
  user: null,
  isLoading: false,
  dataReady: false,
  error: null,
};

const authReducer = (state, action) => {
  switch (action.type) {
    case 'LOGIN':
      return {
        ...state,
        user: action.payload,
        isLoading: false,
        dataReady: true,
        error: null,
      };
    case 'LOGOUT':
      return {
        ...state,
        user: null,
        error: null,
      };
    case 'FETCHING_START':
      return {
        ...state,
        isLoading: true,
        dataReady: false,
      };
    case 'FETCH_ERROR':
      return {
        ...state,
        isLoading: false,
        error: action.payload,
      };
    default:
      return state;
  }
};

const AuthContext = createContext();

const AuthProvider = ({ children }) => {
  const [state, dispatch] = useReducer(authReducer, initialState);

  const login = (authData) => {
    dispatch({ type: 'FETCHING_START' });

    // Perform the POST request
      fetch('http://localhost:8000/api/token/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(authData)
      })
        .then(response => {
          if (!response.ok) {
            throw new Error('Request failed with status ' + response.status);
          }
          return response.json();
        })
        .then(data => {
          dispatch({ type: 'LOGIN', payload: data });
        })
        .catch(error => dispatch({ type: 'FETCHING_ERROR', payload: error }));
  };

  const logout = () => {
    dispatch({ type: 'LOGOUT' });
  };

  return (
    <AuthContext.Provider value={{ state, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};

export { AuthContext, AuthProvider };
