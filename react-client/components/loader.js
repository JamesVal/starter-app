import React from 'react';
import { useSelector } from 'react-redux';

export default function Loader() {
  const loadingAuth = useSelector(state => state.auth.isLoading);
  const loadingItems = useSelector(state => state.items.isLoading);
  
  const getShowLoading = () => {
    return (loadingAuth || loadingItems);
  }

  return(
    <>
      {getShowLoading() && <div>Loading...</div>}
    </>
  );
}