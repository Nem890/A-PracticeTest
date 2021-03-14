# Created by Michael Alestock
# elmatic @ GitHub
# https://github.com/elmatic

# Import Random Module
import random

# Declare the instructions


def show_instructions():
    print("Welcome to n3tbi0s' CompTIA A+ Core 1 Practice Test\n")
    print("Good luck!!\n")


show_instructions()  # Display the instructions


# Game Loop
while True:

    # Quiz Questions
    test_data = [
        {
            "question": "The printer in the accounting department has stopped all printing processes. The print queue "
                        "shows that there are seven jobs in the queue that are waiting to be printed. Which of the "
                        "following would be the BEST next troubleshooting step?",
            "choices": {"a": "Send a test job to the printer and move it to the top of the queue",
                        "b": "Restart the printer's spooler",
                        "c": "Install an updated version of the printer driver",
                        "d": "Delete everything in the queue and resend the print jobs"},
            "answer": "b"
        },
        {
            "question": "What port does DHCP Server use?",
            "choices": {"a": "21", "b": "143", "c": "67", "d": "110"},
            "answer": "c"
        },
        {
            "question": "What port does IMAP4 use?",
            "choices": {"a": "21", "b": "143", "c": "67", "d": "110"},
            "answer": "b"
        },
        {
            "question": "What port does POP3 use?",
            "choices": {"a": "21", "b": "143", "c": "67", "d": "110"},
            "answer": "d"
        },

    ]

    # Random Choice Selection
    q = random.choice(test_data)

    # Practice Test Syntax
    print(q.get("question"))
    answer = input(q.get("choices")).lower()

    if answer == q.get("answer"):
        print("Correct")
    else:
        print("Wrong")
