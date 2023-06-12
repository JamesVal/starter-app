import React, { useState, useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { getItems } from '../../redux/slices/items-slice';
import Loader from '../../components/loader';
import Item from '../../components/item';

export default function Items() {
  const dispatch = useDispatch();
  const dataReady = useSelector((state) => state.items.dataReady);
  const items = useSelector((state) => state.items.allItems);

  useEffect(() => {
    dispatch(getItems());
  }, []);

  return(
    <>
    <Loader></Loader>
    { dataReady && (
      <div>
        {items.map(item => <Item key={item.id} item={item}/>)}
      </div>
    )}
    </>
  );
}