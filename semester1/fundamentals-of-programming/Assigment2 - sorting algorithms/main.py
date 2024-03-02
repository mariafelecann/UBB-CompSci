#defining the functions:

def Option1_RandomListGenerator(n):   #this function generates a random list of numbers
    import random
    RandomList = []
    for i in range(1,n+1):
        element = random.randint(0,100)
        RandomList.append(element)
    return RandomList

def Option2_InsertSort(List,steps):

    counter=0
    for i in range(1,len(List)):
        number=List[i]
        j=i-1
        counter=counter+1
        if counter==steps:
            counter=0
            Option4_ShowList(List)
        while j>=0 and List[j]>number:  #the current element is compared with its predecessor, and if it is smaller
                                        #than it, it is compared with the elements before
            List[j+1]=List[j]           #the greater elements are moved one position up in order to make space
                                        #for the element
            j-=1
        List[j+1]=number                #the element is placed in its right place
    print("The sorted list:")
    Option4_ShowList(List)

def Option3_GnomeSort(List,steps):
    counter=0
    index=0
    while index < n :                     #the instructions are repeated until we get to the end of the list
        counter=counter+1
        if(counter==steps):
            counter=0
            Option4_ShowList(List)
        if index==0:                      #if we are at the first element, then we move to the second element
            index=index+1
        if List[index]>=List[index-1]:
            index=index+1                 #if the current element is greater than the previous one, then we
                                          #move to the next element
        else:
            List[index-1],List[index]=List[index],List[index-1]   #if not, we interchange these two elements
            index=index-1                                         #and than go one step backwards
    print("The sorted list:")
    Option4_ShowList(List)

def Option4_ShowList(List):
    print(List)

#printing the starting lines

print("~ WELCOME! ~")
print("This program generates a random list and then uses two sorting methods :)")

#creating the options

while(True):

    print("MAIN MENU")
    print("Option 1: Generate a list of n random natural numbers!")
    print("Option 2: Insert Sort")
    print("Option 3: Gnome Sort")
    print("Option 4: View list")
    print("Option 0: Exit")

    choice= int(input("Enter your choice:"))
    if(choice==1):
        n = int(input("Enter n: (the number of elements in the generated list)"))
        List = Option1_RandomListGenerator(n)
        print("The random generated list:")
        Option4_ShowList(List)
    elif(choice==2):
        n = int(input("Enter n: (the number of elements in the generated list)"))
        List = Option1_RandomListGenerator(n)
        print("The random generated List before sorting:")
        Option4_ShowList(List)
        steps=int(input("Please enter the number of steps:"))
        Option2_InsertSort(List,steps)
    elif(choice==3):
        n = int(input("Enter n: (the number of elements in the generated list)"))
        List = Option1_RandomListGenerator(n)
        print("The random generated List before sorting:")
        Option4_ShowList(List)
        steps = int(input("Please enter the number of steps:"))
        Option3_GnomeSort(List,steps)
    elif(choice==4):
        n = int(input("Enter n: (the number of elements in the generated list)"))
        Option4_ShowList(n)
    elif(choice==0):
        break
    else:
        print("Oops! Invalid choice!")




