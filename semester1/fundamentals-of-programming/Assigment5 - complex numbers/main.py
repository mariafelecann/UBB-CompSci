import cmath

def create_complex_number(real,imag):
    return [real,imag]

#def create_complex_number(real,imag):
    #return {'real': real, 'imag': imag}

def complexGenerator(real, imag):
    a = complex(real, imag)
    return a

def getReal(x):
    return x.real

def getImag(x):
    return x.imag


def readComplexNumber(x):
    x = complex(input(""))
    return x


def createList(x, n):

    """"
    term : one complex element
    x: the list of complex elements
    return: the list of complex elements
    """

    x = []
    term = [0 for i in range(2)]
    for i in range(n):
        real = int(input("Please enter the real part of the number:"))
        imag = int(input("Please enter the imaginary part of the number: "))
        term = create_complex_number(real, imag)
        x.append(term)
    return x


def readNumbers(numbers):
    for i in range(len(numbers)):
        numbers[i] = readComplexNumber(numbers[i])
    return numbers


def showNumbers(numbers):
    print(numbers)


def modulus(a):
    y = cmath.sqrt((a.real) ** 2 + (a.imag ** 2))
    return y.real


def longestSubarray(numbers):

    """"
    il: the beggining of the longest subarray
    jl: the end of the longest subarray
    maxlength: the maximum length found in the initial array
    numbers: the list of complex numbers
    return: the longest subarray
    """
    il = 0
    jl = 0
    i = 0
    j = 0
    maxlength = -1

    while i < len(numbers):

        j = i
        a = complexGenerator(getRealPartList(numbers,j), getImagPartList(numbers,j))
        #a = complexGenerator(getRealPartDict(numbers,j), getImagPartDict(numbers, j))
        if modulus(a) >= 0 and modulus(a) <= 10:
            while modulus(a) >= 0 and modulus(a) <= 10:
                j += 1
                a = complexGenerator(getRealPartList(numbers, j), getImagPartList(numbers, j))
                #a = complexGenerator(getRealPartDict(numbers, j), getImagPartDict(numbers, j))
            if j - i + 1 > maxlength:
                jl = j
                il = i
                maxlength = j - i + 1
            i = j
        else:
            i += 1
    LongestSubarray = numbers[il:jl + 1]
    LongestSubarray.append(maxlength)
    return LongestSubarray


def subsets(numbers):
    if numbers == []:
        return [[]]
    x = subsets(numbers[1:])
    return x + [[numbers[0]] + y for y in x]


def subsets_of_given_size(numbers, n):
    return [x for x in subsets(numbers) if len(x) == n]


def is_solution(set):
    """"
    This function verifies if a given set is a solution
    set: a list of numbers
    return: 1 if true, 0 otherwise
    """
    for i in range(len(set) - 1):
        if i % 2 == 0 and set[i] > set[i + 1]:
            return 0
        elif i % 2 == 1 and set[i] < set[i + 1]:
            return 0
    return 1


def alternatingSequence(numbers):
    """"
    sets: list that contains all the sequences that satisfy the conditions
    set: all the subsets of a specific range
    sol: one element of the set list
    solution: the sequence in the list sets that has the maximum length
    maximumLength: contains the maximum length of the solution
    return: solution
    """
    sets = []
    for i in range(1, len(numbers)):
        set = subsets_of_given_size(numbers, i)
        for j in range(0, len(set) - 1):
            sol = set[j]
            if is_solution(sol):
                sets.append(sol)

    maximumLength = -1

    solution = []

    for i in range(len(sets)):
        if len(sets[i]) > maximumLength:
            maximumLength = len(sets[i])
            solution = sets[i]
    solution.append(maximumLength)
    return solution



def find_longest_alternating_sequence(A):
    '''
        Input: list A of complex numbers
        L - 2 dimensional array to store temporary data
        Effect: computes the length of longest alternating subsequence
    '''
    # base case
    if not A or len(A) <= 1:
        return len(A)

    if len(A) == 2:
        if getReal(A[0]) == getReal(A[1]):
            return 1

    # lookup table to store solutions to sub-problems
    L = [[0] * 2 for r in range(len(A) + 1)]

    '''
        `L[i][0]` stores the longest alternating subsequence till `A[0…i]`
        where `A[i]` is greater than `A[i-1]`

        `L[i][1]` stores the longest alternating subsequence till `A[0…i]`
        where `A[i]` is smaller than `A[i-1]`
    '''

    # stores result
    result = 1

    # base case: the first element will always be part of LAS
    L[0][0] = L[0][1] = 1

    # fill the lookup table in a bottom-up manner
    for i in range(1, len(A)):

        # do for each element `A[j]` before `A[i]`
        for j in range(i):

            # If `A[i]` is greater than `A[j]`, update `L[i][0]`
            if getReal(A[i]) > getReal(A[j]):
                print(A[i], A[j])
                L[i][0] = max(L[i][0], L[j][1] + 1)

            # If `A[i]` is smaller than `A[j]`, update `L[i][1]`
            if getReal(A[i]) < getReal(A[j]):
                print(A[i], A[j])
                L[i][1] = max(L[i][1], L[j][0] + 1)

        # update result by taking a maximum of both values
        if result < max(L[i][0], L[i][1]):
            result = max(L[i][0], L[i][1])

    return result

def run_menu():

    numbers = [create_complex_number(2, 5), create_complex_number(3, 4), create_complex_number(10, 7),
               create_complex_number(14, 3), create_complex_number(17, 9), create_complex_number(13, 8),
               create_complex_number(12, 3)]

    s = []

    while (True):
        print(" ")
        print("~~ M A I N  M E N U ~~")
        print(" ")
        print("This application works with complex numbers :)")
        print("Check these options out for learning more about these numbers! ")
        print(" ")
        print("OPTIONS:")
        print("Option 1 : Read complex numbers")
        print("Option 2 : Show the numbers")
        print(
            "Option 3 : Length and elements of a longest subarray of numbers where each number's modulus is in the [0, 10] range.")
        print(
            "Option 4 : The length and elements of a longest alternating subsequence, when considering each number's real part")
        print("Option 5 : Exit")
        print(" ")
        choice = int(input("Please enter your choice :) :  "))
        if choice != 5:

            if choice == 1:
                n = int(input("Please enter the number of terms in the list:"))
                s.clear()
                s = createList(s, n)
            elif choice == 2:
                if(len(s)==0):
                  showNumbers(numbers)
                else:
                    showNumbers(s)
            elif choice == 3:
                if(len(s)==0):
                    arr = longestSubarray(numbers)
                    print("the maximum length is: ", arr[-1])
                    arr = arr[:-1]
                    print(arr)
                else:
                    arr = longestSubarray(s)
                    print("the maximum length is: ", arr[-1])
                    arr = arr[:-1]
                    print(arr)
            elif choice == 4:
                s.clear()
                w = int(input("Do you wish to use a generated list (1), the program's list(2) or a dictionary(3): "))
                if w == 1:
                    n = input('How many complex numbers do you wish to insert: ')
                    if not n.isdigit():
                        print('Not a valid number')
                        continue

                    l1 = []
                    l1.clear()
                    l2 = []
                    l2.clear()

                    for i in range(n):
                        x = input('real part:')
                        l1.append(x)
                        x = input('imaginary part:')
                        l2.append(x)
                    readList(s, n, l1, l2)
                    ans = create_the_subsequence(s)
                    print('The length of the longest alternating subsequence is', find_longest_alternating_sequence(s))
                    print('Longest alternating subsequence is:', ans)
                if w == 2:
                    ans = create_the_subsequence(t)
                    print('The length of the longest alternating subsequence is', find_longest_alternating_sequence(s))
                    print('Longest alternating subsequence is:', ans)
                if w == 3:
                    s.clear()
                    n = input('How many complex numbers do you wish to insert: ')
                    if not n.isdigit():
                        print('Not a valid number')
                        continue
                    n = int👎
                    l1 = []
                    l1.clear()
                    l2 = []
                    l2.clear()
                    for i in range(n):
                        x = input('real part:')
                        l1.append(x)
                        x = input('imaginary part:')
                        l2.append(x)
                    l = create_dictionary(l1, l2, n)
                    print_dictionary(l)
                    readList(s, n, l1, l2)
                    ans = create_the_subsequence(s)
                    print('The length of the longest alternating subsequence is', find_longest_alternating_sequence(s))
                    print('Longest alternating subsequence is:', ans)
        elif choice == 5:
            break
        else:
            print("Oops! Invalid choice!")

run_menu()