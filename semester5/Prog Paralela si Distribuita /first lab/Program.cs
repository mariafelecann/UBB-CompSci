using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using Lab1PPD.Banks;
using Lab1PPD.Repository;
namespace Lab1PPD
{
    internal class Program
    {
        public static Bank bank = new Bank();
        private static Random random = new Random();

        private static readonly object randomLock = new object();
        static void RandomThreadOperations()
        {
            int randomNrOfOperations;
            lock (randomLock)
            {
                randomNrOfOperations = random.Next(1, 10); 
            }
            // Console.WriteLine("Thread executing:" + randomNrOfOperations + " operations");
            for (int counter=0; counter<randomNrOfOperations; counter++)
            {
                // Console.WriteLine("Operation " + counter);
                int randomSourceAccountId, randomTargetAccountId, randomAmount;
                lock (randomLock)
                {
                    randomSourceAccountId = random.Next(0, 8);
                    randomTargetAccountId = random.Next(0, 8);
                    randomAmount = random.Next(1, 100); 
                }
                while (randomSourceAccountId == randomTargetAccountId)
                {
                    lock (randomLock)
                    {
                        randomTargetAccountId = random.Next(0, 8);
                    }
                }

                // Console.WriteLine("transfer between " + randomSourceAccountId + " and " + randomTargetAccountId + " of amount " + randomAmount);
                bank.Transfer(randomSourceAccountId, randomTargetAccountId, randomAmount);
            }
        }
        static void Main(string[] args)
        {
            
            List<Thread> threads = new List<Thread>();
            for(int count = 1; count<=10; count ++)
            {
                Thread new_thread = new Thread(new ThreadStart(RandomThreadOperations));
                threads.Add(new_thread);
                new_thread.Start();
            }

            foreach(Thread thread in threads)
            {
                thread.Join();
            }

            bank.ConsistencyCheck();
            Console.ReadKey();
        }
    }
}
