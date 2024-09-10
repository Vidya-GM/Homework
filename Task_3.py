# Python class assignment Thrusday, 05.09.2024
# Task 3 - checking type of a value
# Result should look like
'''
True
False
True
True
False
''' 

number_int = 123
number_float = 43.23
number_complex = (4 - 1j)
sentence = "How are you?"

print(isinstance(number_int, int))
print(isinstance(number_int, float))
print(isinstance(number_float, float))
print(isinstance(number_complex, complex))
print(isinstance(sentence, str))
print(isinstance(sentence, bool))