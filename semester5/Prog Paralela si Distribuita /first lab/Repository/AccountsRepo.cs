using Lab1PPD.Domain;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lab1PPD.Repository
{
    internal class AccountsRepo
    {
        private List<Account> accounts { get; set; }
        private string filepath = "C:\\Users\\maria\\OneDrive\\Documents\\ubb\\sem5\\programare paralela si distribuita\\Lab1PPD\\consistency_check.txt";
        public void addAccount(Account account)
        {
            accounts.Add(account);
        }
        public void removeAccount(Account account)
        {
            accounts.Remove(account);
        }
        public bool updateAccount(Account updatedAccount)
        {
            bool found = false;
            for (int count = 0; count < accounts.Count(); count++)
            {
                if (accounts[count].Id == updatedAccount.Id)
                {
                    accounts[count] = updatedAccount;
                    found = true;
                }
            }
            return found;
        }
        public void initializeRepository()
        {
            accounts = new List<Account>();
            accounts.Add(new Account(Account.generateNewId(), 800));
            accounts.Add(new Account(Account.generateNewId(), 800));
            accounts.Add(new Account(Account.generateNewId(), 800));
            accounts.Add(new Account(Account.generateNewId(), 800));
            accounts.Add(new Account(Account.generateNewId(), 800));
            accounts.Add(new Account(Account.generateNewId(), 800));
            accounts.Add(new Account(Account.generateNewId(), 800));
            accounts.Add(new Account(Account.generateNewId(), 800));
            accounts.Add(new Account(Account.generateNewId(), 800));
        }

        public Account GetAccount(int id)
        {
            return accounts[id];
        }

        public void ConsistencyCheck()
        {
            lock (accounts)
            {
                bool pass = true;
                Console.WriteLine("Consistency check at " + DateTime.Now);
                using (StreamWriter writer = new StreamWriter(filepath))
                {
                    writer.WriteLine("Consistency check at " + DateTime.Now);
                
                for (int counter = 0; counter <= 8; counter++)
                {
                    Account currentAccount = GetAccount(counter);

                    
                        writer.WriteLine("Account " + counter);
                        writer.WriteLine("Balance in account: " + currentAccount.GetBalance());
                    
                    List<OperationRecord> records = currentAccount.getLogs();
                    double logBalance = 800;
                    foreach (OperationRecord record in records)
                    {
                        if (record.FirstAccountID == counter)
                        {
                            logBalance -= record.AmountTransfered;
                        }
                        else
                        {
                            if (record.LastAccountID == counter)
                            {
                                logBalance += record.AmountTransfered;
                            }
                        }
                    }

                    
                        writer.WriteLine("Balance computed with logs: " + logBalance);
                    
                    if (logBalance != currentAccount.GetBalance())
                    {
                        pass = false;
                    }

                }
                if (pass == true)
                {
                    Console.ForegroundColor = ConsoleColor.Green;
                    Console.WriteLine("Consistency check passed!");
                    
                        writer.WriteLine("Consistency check passed!");
                    
                }
                else
                {
                    Console.ForegroundColor = ConsoleColor.Red;
                    Console.WriteLine("Consistency check failed.");
                    
                        writer.WriteLine("Consistency check failed.");
                    
                }
            }
                Console.ResetColor();
            }

        }
    }
}
