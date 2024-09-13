# Python class assignment Wednesday 11.09.2024
# Task 9 - divisible number
''' 
Your task is to fix program non-working correctly. 

The problem:

accept (prompt) two integers values from the user
check whether a first number is divisible by second number and vice versa
display results
'''

x = int(input("First number: "))
y = int(input("Second number: "))

if x % y == 0:
    print("First number is divisible by second number, result =", x / y)
elif y % x == 0:
    print("Second number is divisible by first number, result =", y / x)
else:
    print("Numbers are non-divisable!")