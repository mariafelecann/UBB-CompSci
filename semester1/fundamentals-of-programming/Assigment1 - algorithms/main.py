#print("This function reads a naturan number n and then returns a new minimal natural number that is
# formed with the same digits as the input")
number=int(input("Please enter n:"))

def CreateNewNumber(n):
    FrequencyList=[0,0,0,0,0,0,0,0,0,0]
    while(n):
        FrequencyList[int(n%10)]=FrequencyList[int(n%10)]+1
        n=n/10
    m=0
    for i in range(0,10):
        while(FrequencyList[i]!=0):
            m=m*10+i
            FrequencyList[i]=FrequencyList[i]-1
    return m

#print(CreateNewNumber(number))


#print("This function reads a natural number n and then computes the smallest natural number greater than n
# that is an element of the Fibonacci sequence.")
number=int(input("Please enter n:"))

def NextFibonacciNumber(n):
    a=1
    b=1
    m=a+b
    while(m<n):
        a=b
        b=m
        m=a+b
    return m

#print(NextFibonacciNumber(number))

#print("This function determines the n-th element of a given sequence (1,2,3,2,2,5,2,2,3,3,3,7,2,2,3,3,3)")
number=int(input("Please enter n:"))

def IsItPrime(n):
    if n==2:
        return True
    if n<=1 or n%2==0:
        return False
    for i in range(2,int(n/2)):
        if n%i==0:
            return False
    return True


def nthNumberofSequence(n):
    counter=0
    a=1
    while(counter<n):

        if IsItPrime(a)==True:
            counter=counter+1
        else:
            if(a==1):
                counter=counter+1
            else:
                d=2
                cop=a
                while(d<=cop):
                    if int(cop%d)==0:
                       for i in range(d):
                           counter=counter+1
                           if counter==n: return d

                       while(int(cop%d)==0):
                           cop=int(cop/d)

                    d=d+1
        if counter==n: return a
        a=a+1


print(nthNumberofSequence(number))
