# Python class assignment Wednesday 11.09.2024
# Task 6 - swapping variables

'''
Your task is to fix program non-working correctly. 

The problem:

prompt two values and assign them to variables a and b
write the Python program to swap these two variables
calculate what result should be and what you get after running the program

'''
a = input("First value: ")
b = input("Second value: ")

print("Before swapping: a =", a, ", b = ", b)

temp = a                            # value of a is given to temp
a = b                               # now value of b is given to a
b = temp                            # now b can have value of a which is stored in temp

print("After swapping: a =", a, ", b =", b)
