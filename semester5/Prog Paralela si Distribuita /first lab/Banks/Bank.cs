using Lab1PPD.Domain;
using Lab1PPD.Repository;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lab1PPD.Banks
{
    internal class Bank
    {
        private AccountsRepo accountsRepository;
        private int globalSerialNumber = 0;
        private object serialNumberLock = new object();
        public Bank()
        {
            accountsRepository = new AccountsRepo();
            accountsRepository.initializeRepository();
        }

        public void Transfer(int sourceAccountId, int targetAccountId, int amount)
        {
            if (sourceAccountId != targetAccountId)
            {
                lock (serialNumberLock)
                {
                    globalSerialNumber++;
                }
                OperationRecord newLogRecord = new OperationRecord(globalSerialNumber, sourceAccountId, targetAccountId, amount);
                Account sourceAccount = accountsRepository.GetAccount(sourceAccountId);
                Account targetAccount = accountsRepository.GetAccount(targetAccountId);


                //i will compare the ids of the accounts, for the following situation:
                // i have 1 thread that tries to transfer money from A to B, and
                //at the same time, a thread that transfers money from B to A.
                //i need to lock the accounts in the same order for both cases, to prevent a deadlock.

                Account first = sourceAccount.Id.CompareTo(targetAccount.Id) < 0 ? sourceAccount : targetAccount;
                Account second = sourceAccount.Id.CompareTo(targetAccount.Id) < 0 ? targetAccount : sourceAccount;

                lock (first)
                {
                    lock (second)
                    {
                        sourceAccount.DoTransfer(amount, newLogRecord);
                        targetAccount.RecieveTransfer(amount, newLogRecord);
                    }
                }
            }
        }

        
        public void ConsistencyCheck()
        {
            accountsRepository.ConsistencyCheck();
        }
    }
}
