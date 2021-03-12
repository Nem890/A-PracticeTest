# Michael Alestock

# Import Practice Test Library

import practiceLibrary

# Display Instructions to the Student
def show_instructions():
    print("Welcome to n3tbi0s' CompTIA A+ Core 1 Practice Test\n")
    print("You have 90 minutes to finish the test\n")
    print("Good luck!!\n")

show_instructions()  # Calling the function

# Declare Test Questions & Answers

practiceLibrary.question1 = ["110", "143", "443", "21"]
attempts = list(range(2))

while (1):
    print("What port does FTP use?\n110\n143\n443\n21 ")
    answer = input("Answer: ")
    if answer == "21":
        answer = answer[0]
        print("Correct!")
        exit(0)
    else:
        attempts.pop(0)
        print("Incorrect")
        print("You have", attempts, "attempts left")
    if len(attempts) == 0:
        exit(0)
