# Python class assignment Thrusday, 05.09.2024
# Task 4 - checking type of value (version 2) 
# result should look like
"""
Is 123  an instance of int?:  True
Is 43.23  an instance of bool?: False
Is (4-1j)  an instance of complex?: True
Is True  an instance of bool?: True
Is 'How are you?'  an instance of float?: False
"""

number_int = 123
number_float = 43.23
number_complex = (4 - 1j)
sentence = "How are you?"
your_words = "an instance of"

print("Is", number_int, your_words, "int?:", isinstance(number_int, int), sep = ' ')
print("Is", number_float, your_words, "bool?:", isinstance(number_float, bool), sep = ' ')
print("Is", number_complex, your_words, "complex?:", isinstance(number_complex, complex), sep = ' ')
print("Is", isinstance(number_int, int), your_words, "bool?:", isinstance(number_int, int), sep = ' ')
print("Is", sentence, your_words, "float?:", isinstance(sentence, float), sep = ' ')
#print("Is", isinstance(number_int, int), your_words, "int?:", isinstance(isinstance(number_int, int), int), sep = ' ')