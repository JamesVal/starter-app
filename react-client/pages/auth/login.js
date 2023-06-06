import React, { useState, useContext, useEffect } from 'react';
import TextInput from '../../components/text-input';
import { AuthContext } from '../../contexts/AuthContext';

export default function Login() {
  const { state, login } = useContext(AuthContext);
  const [formState, setFormState] = useState({
    username: '',
    password: '',
  });

  useEffect(() => {
    if (state.dataReady) {
      console.log("DATA_READY");
    }
  }, [state.dataReady])

  const updateUsername = (value) => {
    setFormState((prevState) => ({
      ...prevState,
      username: value,
    }))
  }

  const updatePassword = (value) => {
    setFormState((prevState) => ({
      ...prevState,
      password: value,
    }))
  }

  const handleLoginClick = (event) => {
    login({ username: formState.username, password: formState.password });
  }

  return(
    <div>
      <div>Username: <TextInput value={formState.username} onChange={updateUsername}></TextInput></div>
      <div>Password: <TextInput value={formState.password} onChange={updatePassword} isPassword={true}></TextInput></div>
      <div><button onClick={handleLoginClick}>Login</button></div>
    </div>
  );
}