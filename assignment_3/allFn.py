# A function named calculate_sum that takes a list of numbers as input and returns their sum.
def calculate_sum_custom():
    numList=list(map(float, input("Enter numbers to find sum of (separated by comma): ").split(',')))
    total=0
    for i in numList:
        total+=i
    print(f"\nSum of {numList} is: {total}\n")

# A function named find_max that takes a list of numbers as input and returns the largest number.
def find_max_custom():
    numList=list(map(float, input("Enter numbers to find greatest of (separated by comma): ").split(',')))
    largestNum=numList[0]
    for i in numList:
        if i>largestNum:
            largestNum=i
    print(f"\nLargest number in {numList} is: {largestNum}\n")

# A function named find_min that takes a list of numbers as input and returns the smallest number.
def find_min_custom():
    numList=list(map(float, input("Enter numbers to find smallest of (separated by comma): ").split(',')))
    smallestNum=numList[0]
    for i in numList:
        if i<smallestNum:
            smallestNum=i
    print(f"\nSmallest number in {numList} is: {smallestNum}\n")



########################################## Using builtin fn
# A function named calculate_sum that takes a list of numbers as input and returns their sum.
def calculate_sum():
    numList=input("Enter numbers to find sum of (separated by comma): ").split(',')
    # type casting each element from list numList to float and adding them using sum()
    result=sum(float(elements) for elements in numList)
    print(result)

# A function named find_max that takes a list of numbers as input and returns the largest number.
def find_max():
    numList=input("Enter numbers to find greatest of (separated by comma): ").split(',')
    largestNum=max(numList)
    print(largestNum)

# A function named find_min that takes a list of numbers as input and returns the smallest number.
def find_min():
    numList=input("Enter numbers to find smallest of (separated by comma): ").split(',')
    smallestNum=min(numList)
    print(smallestNum)
