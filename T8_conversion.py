# Python class assignment Wednesday 11.09.2024
# Task 8 - convertion

'''Your task is to fix program non-working correctly. 

The problem:

prompt value from the user and assign it to some variable
if given value is 0 (zero) convert it to False and if given value is 1 convert it to True
display results 
'''
x: str = input("Type your value: ")

if x == '0':
    x = "false"
elif x == '1':
    x = "true"
else:
    pass

print("Your entered value is now ", x)