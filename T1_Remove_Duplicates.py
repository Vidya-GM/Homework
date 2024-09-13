# Python class assignment Wednesday 11.09.2024
# Task 1 - Remove Duplicates

'''
Write a function remove_duplicates(s) that takes a string s as input 
and returns a string with all duplicate characters removed.

Your result could look like this:
remove_duplicates("hello")

"helo"'''

def remove_duplicates(s):

    my_str: str = s[0]             # my_str is initialized with first character of s
    for i in range(len(s)-1):      # len() function gives length of string, range(x) function gives no from 0,1,2,...,x
        if s[i] != s[i+1]:  
            my_str += s[i+1]     
    print(my_str)
    
remove_duplicates("hhhelllooo")
