import timeit

#defining the functions:

def RandomListGenerator(n):
    import random
    RandomList = []
    for i in range(0,n+1):
        element = random.randint(0,100)
        RandomList.append(element)
    return RandomList

def Option2_InsertSort(List):

    counter=0
    for i in range(1,len(List)):
        number=List[i]
        j=i-1
        while j>=0 and List[j]>number:
            List[j+1]=List[j]
            j-=1
        List[j+1]=number



def Option3_GnomeSort(List):
    counter=0
    index=0
    while index < len(List) :
        if index==0:
            index=index+1
        if List[index]>=List[index-1]:
            index=index+1
        else:
            List[index-1],List[index]=List[index],List[index-1]
            index=index-1


def Option1_ShowList(List):
    print(List)


def CreateLists(n):
    lists=[]
    for i in range(5):
        lists.append(RandomListGenerator(n))
        n*=2
    return lists

def WorstCase(lists):
    print("The worst case scenario for insertion sort as well as for gnome sort is when the list is ")
    print("reversly sorted in the beggining,so that the complexity is O(n^2)")

    for list in lists:
        list.sort(reverse=True)

    for numbers in lists:
        start_Insertion=timeit.default_timer()
        Option2_InsertSort(numbers.copy())
        end_Insertion=timeit.default_timer()
        start_Gnome=timeit.default_timer()
        Option3_GnomeSort(numbers.copy())
        end_Gnome=timeit.default_timer()
        print(str(len(numbers)) + " elements:  " +
            "Insertion sort: " + str(end_Insertion - start_Insertion) +
            "    Gnome sort: " + str(end_Gnome - start_Gnome))

def AverageCase(lists):
    print("The average case for time complexity for both insertion and gnome sort is O(n^2)")

    for numbers in lists:
        start_Insertion=timeit.default_timer()
        Option2_InsertSort(numbers.copy())
        end_Insertion=timeit.default_timer()
        start_Gnome=timeit.default_timer()
        Option3_GnomeSort(numbers.copy())
        end_Gnome=timeit.default_timer()
        print(str(len(numbers)) + " elements:  " +
            "Insertion sort: " + str(end_Insertion - start_Insertion) +
            "    Gnome sort: " + str(end_Gnome - start_Gnome))

def BestCase(lists):
    print("The best case scenario for time complexity for both insertion and gnome sort is O(n)")
    print("This happens when the lists are already sorted and only one iteration takes place.")

    for list in lists:
        list.sort()

    for numbers in lists:
        start_Insertion=timeit.default_timer()
        Option2_InsertSort(numbers.copy())
        end_Insertion=timeit.default_timer()
        start_Gnome=timeit.default_timer()
        Option3_GnomeSort(numbers.copy())
        end_Gnome=timeit.default_timer()
        print(str(len(numbers)) + " elements:  " +
            "Insertion sort: " + str(end_Insertion - start_Insertion) +
            "    Gnome sort: " + str(end_Gnome - start_Gnome))


#printing the starting lines

print("~ WELCOME! ~")
print("This program analyzes time complexity for different sorting types :)")

#creating the options

while(True):

    print("/nMAIN MENU")
    print("Option 1: View a list of n random natural numbers")
    print("Option 2: Insertion Sort")
    print("Option 3: Gnome Sort")
    print("Option 4: Analyze the WORT CASE scenario")
    print("Option 5: Analyze the AVERAGE CASE scenario")
    print("Option 6: Analyze the BEST CASE scenario")
    print("Option 0: Exit")

    choice= int(input("Enter your choice:"))
    if choice!=4 and choice!=5 and choice!=6:
        if choice==0:
            break
        n = int(input("Enter n: (the number of elements in the generated list)"))
        List = RandomListGenerator(n)
        if(choice==1):
            print("The random generated list:")
            Option1_ShowList(List)
        elif(choice==2):
            print("The random generated List before sorting:")
            Option4_ShowList(List)
            Option2_InsertSort(List)
        elif choice==3:
            print("The random generated List before sorting:")
            Option4_ShowList(List)
            Option3_GnomeSort(List)
    elif choice==4 or choice==5 or choice==6:
        lists = CreateLists(100)
        if choice==4:
            WorstCase(lists)
        elif choice==5:
            AverageCase(lists)
        elif choice==6:
            BestCase(lists)
    elif(choice==0):
            break
    else:
        print("Oops! Invalid choice!")