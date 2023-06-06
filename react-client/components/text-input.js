import React from 'react';

export default function TextInput({ value, onChange, isPassword }) {
  const handleInputChange = (event) => {
    const newValue = event.target.value;
    onChange(newValue);
  }

  return(
    <input type={isPassword ? 'password' : 'text'} value={value} onChange={handleInputChange}></input>
  );
}