using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace Lab2PPD
{
    internal class Program
    {
        int[] a = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
        int[] b = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
        int sum = 0;
        bool hasValue = false;
        int currentProduct;
        readonly object lockObject = new object();
        public void ProducerProduct()
        {
            for(int i=0;i<a.Length; i++)
            {
                lock (lockObject)
                {
                    while (hasValue)
                    {
                        Monitor.Wait(lockObject);
                    }
                    currentProduct = a[i] * b[i];
                    Console.WriteLine("Current product : " + currentProduct);
                    hasValue = true;
                    Monitor.Pulse(lockObject);
                }
            }
        }

        public void ConsumerSum()
        {
            for(int i=0; i<a.Length;i++)
            {
                lock(lockObject)
                {
                    while (!hasValue)
                    {
                        Monitor.Wait(lockObject);
                    }
                    sum = sum + currentProduct;
                    Console.WriteLine("Current sum: " + sum);
                    hasValue = false;
                    Monitor.Pulse(lockObject);
                }
                
            }
        }
        static void Main(string[] args)
        {
            Program program = new Program();

            Thread producerThread = new Thread(program.ProducerProduct);
            Thread consumerThread = new Thread(program.ConsumerSum);
            producerThread.Start();
            consumerThread.Start();

            producerThread.Join();
            consumerThread.Join();

            Console.WriteLine("Scalar product of the vectors: " + program.sum);
            Console.ReadKey();

        }
    }
}
