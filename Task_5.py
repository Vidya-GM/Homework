# Python class assignment Thrusday, 05.09.2024
# Task 5 - using comments in code
# For this task code of "Task_4" python file is used
 
 
# Initialize variables
number_int = 123
number_float = 43.23
number_complex = (4 - 1j)
sentence = "How are you?"
your_words = "an instance of"

# printing the variable and checking its type

 
print("Is", number_int, your_words, "int?:", isinstance(number_int, int), sep = ' ') # This should print "Is 123 an instance of int?: True"
print("Is", number_float, your_words, "bool?:", isinstance(number_float, bool), sep = ' ') # This should print "Is 43.23 an instance of bool?: False"
print("Is", number_complex, your_words, "complex?:", isinstance(number_complex, complex), sep = ' ') # This should print "Is (4-1j) an instance of complex?: True"
print("Is", isinstance(number_int, int), your_words, "bool?:", isinstance(number_int, int), sep = ' ') # This should print "Is True an instance of bool?: True"
print("Is", sentence, your_words, "float?:", isinstance(sentence, float), sep = ' ') # This should print "Is How are you? an instance of float?: False"


#print("Is", isinstance(number_int, int), your_words, "int?:", isinstance(isinstance(number_int, int), int), sep = ' ')