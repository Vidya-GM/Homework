# Python class assignment Wednesday 11.09.2024
# Task 1 - Remove Duplicates
'''
Write a function is_palindrome(s) that takes a string s as input 
and returns True if the string is a palindrome, and False otherwise.

Your result should look like this:
is_palindrome("madam")

True
'''

def is_palindrome(s):
    count: int = 0
    #print(int(len(s)/2)) to understand how many times for loop is running
    for i in range(int(len(s)/2)):
        if s[i] == s[len(s)-i-1]: # for string length 7, s[0] == s[6], s[1] == s[5], s[2] == s[4], and s[3] is not compared as it is exactly middle of the string
            count += 1            # for string length 7, three iterations of loop, so count should be 3, which is int of half os the length of the string
    if count == int(len(s)/2):    # if count is equal half of the length of string every iteration is true else false
        print("True")
    else:
        print("False")
is_palindrome("meeieem")

