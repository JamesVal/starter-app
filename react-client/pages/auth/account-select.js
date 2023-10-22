import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import Account from '../../components/account';
import { getAccounts } from '../../redux/slices/auth-slice';
import styles from './account-select.module.scss';

export default function AccountSelect() {
  const { availableAccounts: accounts, selectedAccount, dataReady } = useSelector((state) => state.auth);
  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(getAccounts());
  }, []);

  useEffect(() => {
    if (dataReady) {
      console.log("ACCOUNTS_READY", accounts);
    }
  }, [dataReady])

  return(
    <div className={styles.accountsContainer}>
      <div className={styles.accountsCard}>
        Select Account
        {accounts.map(account => <Account key={account.id} account={account} selected={false} />)} 
      </div>
    </div>
  );
}