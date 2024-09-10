
# Python class assignment Thrusday, 05.09.2024
# Task 2 - printing type of given value 
# result should look like
""" 
123 is type of <class 'int'>
43.23 is type of <class 'float'>
(4-1j) is type of <class 'complex'>
How are you? is type of<class 'str'>
True is type of <class 'bool'>
"""


number_int = 123
number_float = 43.23
number_complex = (4 - 1j)
sentence = "How are you?"

print(number_int, type(number_int), sep = ' is type of ')
print(number_float, type(number_float), sep = ' is type of ')
print(number_complex, type(number_complex), sep = ' is type of ')
print(sentence, type(sentence), sep = ' is type of ')
print(isinstance(number_int, int), type(isinstance(number_int, int)), sep = ' is type of ')