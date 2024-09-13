# Python class assignment Wednesday 11.09.2024
# Task 10 - Grading System
'''
Design A grading system such that, a user can input their score in a course and 
the system tells them their grade and a message.

100 - 80 : A (Excellent Result)
79 - 70 : B (Very Good Result)
69 - 60 : C (Good Result)
59 - 50 : D (Fair Result)
49 - 40 : E (improvable Result)
39 - 0 : F (Need More Hardwork)

Your result should look like this:
What is you score for Maths Class?:  85
Grade : A
Message : Excellent Result!
'''
Grade:str = "Enter valid score"
Message:str = "Score not in range 0-100"
score: int = int(input("What is your score for Maths Class: "))
if score in range(80, 101):
    Grade = 'A'
    Message = "Excellent Result!"
elif score in range(70, 80):
    Grade = 'B'
    Message = "Very Good Result!"
elif score in range(60, 70):
    Grade = 'C'
    Message = "Good Result!"
elif score in range(50, 60):
    Grade = 'D'
    Message = "Fair Result!"
elif score in range(40, 50):
    Grade = 'E'
    Message = "Improvable Result!"
elif score in range(0, 40):
    Grade = 'F'
    Message = "Need More Hardwork!"
else:
    print("Invalid Score!")

print("Grade : ",Grade)
print("Message : ",Message)