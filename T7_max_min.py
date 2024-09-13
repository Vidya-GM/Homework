# Python class assignment Wednesday 11.09.2024
# Task 7 - max and min values

'''
Your task is to fix program non-working correctly. 

The problem:

prompt three float numbers and determine the largest and the smallest one
calculate what result should be and what you get after running the program
'''
x = float(input("First number: "))
y = float(input("Second number: "))
z = float(input("Third number: "))

print("The maximum value is ", max(x, y ,z))
print("The minimum value is ", abs(min(x, y ,z)))
