using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lab1PPD.Domain
{
    internal class Account
    {
        public Guid Id {  get; set; }
        private double Balance { get; set; }
        private List<OperationRecord> Logs {  get; set; }

        private object accountLock = new object();

        public Account(Guid newId, double newBalance) { 
            this.Id = newId;
            this.Balance = newBalance;
            this.Logs = new List<OperationRecord>();
        }
        public static Guid generateNewId()
        {
            return Guid.NewGuid();
        }

        public void RecieveTransfer(int amount, OperationRecord logRecord)
        {
            lock (accountLock)
            {
                Logs.Add(logRecord);
                this.Balance += amount;
            }
        }

        public void DoTransfer(int amount, OperationRecord logRecord)
        {
            lock (accountLock)
            {
                Logs.Add(logRecord);
                this.Balance -= amount;
            }
        }

        public double GetBalance()
        {
            return this.Balance;
        }

        public List<OperationRecord> getLogs()
        {
            return Logs;
        }
    }
}
