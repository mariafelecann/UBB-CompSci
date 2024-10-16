using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lab1PPD.Domain
{
    internal class OperationRecord
    {
        public int SerialNumber { get; }
        public int FirstAccountID { get; }
        public int LastAccountID { get; }
        public int AmountTransfered {  get; }

        public OperationRecord(int serialNumber, int firstAccountID, int lastAccountID, int amountTransfered)
        {
            SerialNumber = serialNumber;
            FirstAccountID = firstAccountID;
            LastAccountID = lastAccountID;
            AmountTransfered = amountTransfered;
        }
    }
}
