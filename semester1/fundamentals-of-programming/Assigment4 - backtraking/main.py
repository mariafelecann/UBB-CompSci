#Backtracking

#Problem 12

""""
Consider the natural number n (n<=10) and the natural numbers a1, ..., an.
Determine all the possibilities to insert between all numbers a1, ..., an the operators + and –
such that by evaluating the expression the result is positive.
"""

def is_solution_rec(x,n,a):
    s=0

    for j in range(0,n):
        if x[j]==0 : s=s+a[j]
        else: s=s-a[j]
    if s>0 :
        print("the sum is ",s," and the terms are:")
        for j in range(0,n):
            if x[j]==0 : print(" + ", a[j])
            else: print(" - ",a[j])


def is_consistent_rec(k,n,x,a):
    semi_sum_1=0
    for i in range(0,k):
        if x[i]==0:
          semi_sum_1=semi_sum_1+a[i]
        else:
            semi_sum_1=semi_sum_1-a[i]
    semi_sum_2=0
    for i in range(k,n):
        semi_sum_2=semi_sum_2+a[i]
    if(semi_sum_1 + semi_sum_2>0):
        return 1
    else:
        return 0

"This is the recursive algorithm:"


def back_rec(k,n,x,a):
    if k == n:
        is_solution_rec(x, n, a)
    for i in range(0,2):
        x[k]=i               #we store the values 0 and 1 on n positions,
                             #1 representing negative numbers and 0 positive ones.
        if k<n and is_consistent_rec(k,n,x,a):
          back_rec(k+1,n,x,a)


"This is the iterative algorithm:"


def is_consistent_iter(state, numbers):
    sum = 0
    for i in range(len(state) - 1):
        sum += state[i] * numbers[i]

    for i in range(len(state)-1, len(numbers)):
        sum += numbers[i]

    if sum>0:
        return 1
    else:
        return 0

def get_sum(numbers):
    sum = 0
    for i in range(len(numbers)):
        sum=sum+numbers[i]
    return sum


def back_iter(a):
    n = len(a)
    x = [1,0]

    s=(-1)*a[0]
    for i in range(1,len(a)):
        s=s+a[i]
    if (s > 0):
        print("The sum is ", s, " and the terms are:")
        print((-1)*a[0], [ a[i] for i in range(1, len(a))])

    while len(x) > 0:
        if len(x) == n + 1:
            s=get_sum([x[i] * a[i] for i in range(len(a))])
            if(s>0):
                print("The sum is ", get_sum([x[i] * a[i] for i in range(len(a))])," and the terms are:")
                print([x[i] * a[i] for i in range(len(a))])
            x = x[:-1]
        else:
            if is_consistent_iter(x, a):
                if x[-1] == 0:
                    x[-1] = 1
                    x.append(0)
                elif x[-1] == 1:
                    x[-1] = -1
                    if len(x) == 1:
                        break
                    x.append(0)
                else:
                    x = x[:-1]
            else:
                x = x[:-1]


while(True):
    print("MAIN MENU")
    print("Option 1: Recursive backtracking")
    print("Option 2: Iterative backtracking")
    print("Option 3: Exit")
    choice=int(input("Please enter your choice:"))
    if(choice!=3):
        n = int(input("Please eneter the n, the number of elements in the list, and then the elements from the list:"))
        a = []
        for i in range(n):
            a.append(int(input()))
        x = []
        x = [0 for i in range(n + 1)]
        if(choice==1):
            back_rec(0, n, x, a)
        elif(choice==2):
            back_iter(a)
    elif(choice==3):
        break
    else:
        print("Oops! Invalid choice. :(")




