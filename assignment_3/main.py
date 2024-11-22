# A function named calculate_sum that takes a list of numbers as input and returns their sum.
def calculate_sum():
    numList=input("Enter numbers to find sum of (separated by comma): ").split(',')
    # print(numList)

    # type casting each element from list numList to float and adding them using sum()
    result=sum(float(elements) for elements in numList)
    print(result)

calculate_sum()

# A function named find_max that takes a list of numbers as input and returns the largest number.
def find_max():
    numList=input("Enter numbers to find greatest of (separated by comma): ").split(',')
    largestNum=max(numList)
    print(largestNum)

find_max()

# A function named find_min that takes a list of numbers as input and returns the smallest number.
def find_min():
    numList=input("Enter numbers to find smallest of (separated by comma): ").split(',')
    smallestNum=min(numList)
    print(smallestNum)

find_min()