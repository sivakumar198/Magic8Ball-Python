#import modules

import sys
import random

#initial variables
questions = True  # This controls the while loop

responses = [
    "IT IS CERTAIN",
    "YOU MAY RELY ON IT",
    "AS I SEE IT, YES",
    "OUTLOOK LOOKS GOOD",
    "MOST LIKELY",
    "IT IS DECIDEDLY SO",
    "WITHOUT A DOUBT",
    "YES, DEFINITELY"
]

#while loop
while questions:
    
#write the code that will recieve the user input
    user_input = input("Ask the Magic 8-Ball a question (or type 'exit' to quit): ")

#return the random response

    if user_input.lower() == "exit":
        print("Goodbye!")
        sys.exit() # Exits the program
    

    print("Magic 8-ball says: " + random.choice(responses))
    
#and quit the application

    
