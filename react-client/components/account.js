import React from 'react';

export default function Account({ account, selected }) {
  return(
    <div className={ selected ? 'selected' : '' }>
      {account.accountName}
    </div>
  );
}