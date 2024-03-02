
def Changed_terms(n):
    sum=0
    i=1
    while i<n/2:
        sum=sum+pow(-1,i+1)/i
        sum=sum+pow(-1,n-i+1)/i
        i+=1
    return sum

def Compute_sum(n):
    sum=0
    for i in range(1,n):
        sum=sum+pow(-1,i+1)/i
    return sum

while(True):
    print("WELCOME!")
    print("This program computes the sum ∑(−1)^(n+1)/n (n>=1) in order to prove that it equals ln 2.")
    print("It also illustrates that changing the order of summation in this series can lead to a different sum.")

    print("Option 1: Compute the sum in the basic order")
    print("Option 2: Analyze the changes in the result from changing the order of the terms")
    print("Option 3: Exit")
    choice=int(input("Please enter your choice:"))
    if choice!=3:
        n=int(input("Please enter n:"))
        if choice==1:
            s=Compute_sum(n)
            print(s)
        elif choice==2:
            s=Changed_terms(n)
            print(s)
    else:
        break