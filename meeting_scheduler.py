import os
import sys
import random

#
# Simple scheduler for LAMBDA meetings.
# Mark who is present, then a random order for presenting is shown.
#
# Author: David
# Date: 2020-03-23
#

# Add people as required.
PARTICIPANTS = ['Claudia', 'Arthur', 'Gustavo', 'Sara', 'Manuel', 'Felipe', 'Peide', 'Nirmal', 'David']

def get_active_participants():
    """
    Interactive function that asks for input from the user.
    Marks who is present, and returns a list of all participants marked as present.
    """
    input_str = "0"
    active_participants = []

    while input_str != "":
        input_str = input("\tEnter a number: ")
        
        if input_str.isnumeric():
            input_int = int(input_str)

            if input_int < 1 or input_int > len(PARTICIPANTS):
                print("\tE: Enter a number listed above!")
            elif input_int - 1 in active_participants:
                print(f"\tE: You have already added {PARTICIPANTS[input_int - 1]}!")
            else:
                print(f"\tAdded {PARTICIPANTS[input_int - 1]}")
                active_participants.append(input_int - 1)
        else:
            if input_str == "":
                continue
            
            print("\tE: Enter a number!")
    
    return active_participants


def main():
    """
    Where the magic happens. Randomises the list.
    Prints the randomised list (which is the presenting order), and exits.
    """
    print(f"There are {len(PARTICIPANTS)} participants.")
    print("The order for the meeting is:")
    print()

    participants = PARTICIPANTS
    random.shuffle(participants)

    for participant in participants:
        print(f"{participant}")
    
    print(f"{os.linesep}Have fun!")
    
    return 0

if __name__ == '__main__':
    print(f"LAMBDA Online Meeting Scheduler{os.linesep}")
    sys.exit(main())