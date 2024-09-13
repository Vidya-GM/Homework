# Python class assignment Wednesday 11.09.2024
# Task 5 - summing two integers

'''
Your task is to fix program non-working correctly. The problem:

sum the two prompted integers
however, if the sum is between 15 to 20 (both numbers included) it should be calculated to 20
calculate what result should be and what you get after running the program
'''

x = int(input("First number: ")) # input needs to be integer
y = int(input("Second number: "))

result = x + y

if result >= 15 and result <= 20: # Result should be more than equal to 15 and (but it should also be) less than or equal to 20
    result = 20                   
print("Calculated sum is ", result)