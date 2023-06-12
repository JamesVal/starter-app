import React from 'react';

export default function Item({ item }) {
  return(
    <div>
      Name: {item.itemName} Description: {item.itemDescription}
    </div>
  );
}