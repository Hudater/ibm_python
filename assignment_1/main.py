# Create a list containing the numbers 1 to 5 and print it.
numList = [1, 2, 3, 4, 5]
print("\n" "The list contains: ", numList,)
print("numList is of type: ", type(numList), "\n")


# Convert the list into a tuple and print it.
numTuple = tuple(numList)
print("\n" "The tuple contains: ", numTuple,)
print("numTuple is of type: ", type(numTuple), "\n")


# Create a set from the tuple and print it.
numSet = set(numTuple)
print("\n" "The set contains: ", numSet,)
print("numSet is of type: ", type(numSet), "\n")


# Create a dictionary with keys as the numbers 1 to 5 and values as their squares, and print it
numDict = {x: x**2 for x in range(1,6)}
print("\n" "The dictionary contains: ", numDict,)
print("numDict is of type: ", type(numDict), "\n")
