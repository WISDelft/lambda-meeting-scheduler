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
PARTICIPANTS = ['Claudia', 'Arthur', 'Gustavo', 'Sara', 'Felipe', 'Peide', 'Nirmal', 'David']

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
    Where the magic happens. Solicits a list of active participants, and randomises the list.
    Prints the randomised list (which is the presenting order), and exits.
    """
    print(f"First, who is present?{os.linesep}Type the number next to individuals who are present, then push enter when finished.{os.linesep}")

    i = 1

    for participant in PARTICIPANTS:
        print(f"\t{i}: {participant}")
        i = i + 1
    
    print(f"{os.linesep}")
    active_participants = get_active_participants()
    print(f"{os.linesep}")
    
    if len(active_participants) == 0:
        print("E: You did not select any participants. Exiting...")
        return 1
    
    print(f"Complete. You have selected {len(active_participants)} participants.")
    print("The order for the meeting is:")

    random.shuffle(active_participants)

    for participant_id in active_participants:
        print(f"\t{PARTICIPANTS[participant_id]}")
    
    print(f"{os.linesep}Have fun!")
    
    return 0

if __name__ == '__main__':
    print(f"LAMBDA Online Meeting Scheduler{os.linesep}")
    sys.exit(main())