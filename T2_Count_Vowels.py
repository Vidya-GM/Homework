# Python class assignment Wednesday 11.09.2024
# Task 2 - Count Vowels

'''
Write a function count_vowels(s) that takes a string s as input 
and returns the count of vowels in the string.

Your result could look like this:
count_vowels("hello")

Output: 2
'''

# def count_vowels(s):
#     count: int = 0  # initialize count to 0
#     vowels: str = "aeiouAEIOU"
#     for character in s:
#         if character in vowels:
#             count += 1
#     print(count)

# count_vowels("helloooooo")

def count_vowels(s):
    count: int = 0
    vowels: str = "aeiouAEIOU"
    for i in range(len(s)):
        if s[i] in vowels:
            count += 1
    print(count)

count_vowels("helloooooo")



