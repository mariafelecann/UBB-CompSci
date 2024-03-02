
def iteration(n , η, c):

    a=0
    b=0
    arr=[0 for i in range(20)]
    l=0
    for i in range(n):
       if c==1:
          b = a - η * ( 6 * a + 6)
       else:
           b = a - η * (3 * a * a - 8 * a - 5)
       arr[l] = b
       l += 1
       a = b

    return arr

def globalminimum(η):

    values = iteration(20,η,1)
    for i in range(len(values)):
        print(values[i])
    print("The global minimum is obtained by the formula -delta/(4*a)")
    print("In our case, the global minimum is -12/(4*3), which is 1.")
    print("We can see that the terms approach 1 .")

def fasterconvergence(η):
    values = iteration(20, η,1)
    for i in range(len(values)):
        print(values[i])
    print("The global minimum is obtained by the formula -delta/(4*a)")
    print("In our case, the global minimum is -12/(4*3), which is 1.")
    print("We can observe how the terms approach the value 1 faster than in option 1.")

def divergence(η):
    values = iteration(20, η,1)
    for i in range(len(values)):
        print(values[i])
    print("We can observe that the values are very big and that the iteration diverges.")

def localminimum(η):
    print("Let us consider a different function, that is non-convex.")
    print("f(x) =x^3 - 4 x^2 - 5 x - 7, with the derivative f'(x) = 3x^2 - 8x - 5")
    print("For this function, the local minimum is min{x^3 - 4 x^2 - 5 x - 7} = 1/27 (-497 - 62 sqrt(31)) at x = 4/3 + sqrt(31)/3")
    values = iteration(20, η, 2)
    for i in range(len(values)):
        print(values[i])

while(True):
    print("Welcome! :)")
    print("This algorithm studies the convergence of the iteration:")
    print("x(n+1) = x(n) -  η * f'(x))")
    print("where f(x) is a convex, differentiable function.")
    print("Let us consider f(x) be  3 * x^2 + 6 * x + 2  .")
    print("Then f'(x) is 6 * x + 6.")
    print(" ")
    print("OPTIONS:")
    print("Option 1: See how for a small η the iteration converges to the global minimum.")
    print("Option 2: See that by increasing η the algorithm will converge faster.")
    print("Option 3: See that a too large η might lead to divergence.")
    print("Option 4: See how if we change f to be nonconvex, the algorithm gets stuck to the local minimum.")
    print("Option 5: Exit")
    choice=int(input("Please enter your choice:"))
    if(choice!=5):
        if choice == 1 :
            η = float(input("Please enter a small value for η(between 0 and 0.3): "))
            globalminimum(η)
        elif choice == 2:
            η = float(input("Please enter a small value for η(between 0.3 and 0.5): "))
            fasterconvergence(η)
        elif choice == 3:
            η = float(input("Please enter a large value for η: "))
            divergence(η)
        elif choice == 4:
            η = float(input("Please enter a value for η: "))
            localminimum(η)
        else:
            print("Oops! Invalid choice :( ")
    else:
        break