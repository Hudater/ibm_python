# Asks the user to enter a number.
numIn = int(input("Please enter a number (ints only): "))
# print(f" The number entered is: {numIn} \n And of type {type(numIn)}")

############################################################### Solution 1; doesn't work with -ve numbers
# ## printing a simple newline for readability
# print("\n")

# # Checks if the number is even or odd using an if-else statement.
# # If the number is even, print all even numbers from 1 to that number using a loop.
# if numIn%2 == 0:
#     print(f"{numIn} is Even")
#     print(f"All even number between 1 and {numIn} are:")
#     for i in range(2, numIn+1, 2):
#         print(i)

# #If the number is odd, print all odd numbers from 1 to that number using a loop.
# else:
#     print(f"{numIn} is Odd")
#     print(f"All odd number between 1 and {numIn} are:")
#     for i in range(1, numIn+1, 2):
#         print(i)
############################################################### Solution 1 complete
############################################################### Solution 2; more compute; doesn't work with -ve numbers
# start=1
# if numIn%2 == 0:
#     print(f"{numIn} is Even")
#     print(f"All even number between {start} and {numIn} are:")
#     for i in range(start, numIn+1):
#         if i%2==0:
#             print(i)
# else:
#     print(f"{numIn} is Odd")
#     print(f"All odd number between {start} and {numIn} are:")
#     for i in range(start, numIn+1):
#         if i%2!=0:
#             print(i)
############################################################### Solution 2 complete
############################################################### Solution 3; more comprehensive; works with -ve numbers
####### Includes +ve, -ve and 0
if numIn>0:
    if numIn%2 == 0:
        print(f"{numIn} is Even and all even number between 1 and {numIn} are:")
        for i in range(2, numIn+1, 2):
            print(i)
    else:
        print(f"{numIn} is Odd and all odd number between 1 and {numIn} are:")
        for i in range(1, numIn+1, 2):
            print(i)
elif numIn==0:
    print("0 is Even")
elif numIn<0:
    if numIn%2 == 0:
        print(f"{numIn} is Even and all even number between 1 and {numIn} are:")
        for i in range(numIn, 2, 2):
            print(i)
    else:
        print(f"{numIn} is Odd and all odd number between 1 and {numIn} are:")
        for i in range(numIn, 2, 2):
            print(i)
else:
    print("Somehow you input an invalid option. Please report it via a github issue :)")
############################################################### Solution 3 complete
