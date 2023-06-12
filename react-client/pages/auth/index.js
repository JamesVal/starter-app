import React, { useState, useEffect } from 'react';
import { useRouter } from 'next/router';
import { useDispatch, useSelector } from 'react-redux';
import TextInput from '../../components/text-input';
import { login } from '../../redux/slices/auth-slice';

export default function Login() {
  const dispatch = useDispatch();
  const router = useRouter();
  const dataReady = useSelector((state) => state.auth.dataReady);
  const [formState, setFormState] = useState({
    username: '',
    password: '',
  });

  useEffect(() => {
    if (dataReady) {
      router.push('/items');
    }
  }, [dataReady])

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
    dispatch(login(formState.username, formState.password));
  }

  return(
    <div>
      <div>Username: <TextInput value={formState.username} onChange={updateUsername}></TextInput></div>
      <div>Password: <TextInput value={formState.password} onChange={updatePassword} isPassword={true}></TextInput></div>
      <div><button onClick={handleLoginClick}>Login</button></div>
    </div>
  );
}