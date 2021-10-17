import random
import time

#Reaction Speed Tester By Robin Barnes
#Might make an autoclicker next
#Need to port this to rust as well
#Then I might experiment with GUIs

lower_bound = 250
upper_bound = 5000
repeat = "true"


while "true":
    command = input("---------------------------------\n|Type settings to change config.|\n|Type start to begin.           |\n|Type end to finish.            |\n---------------------------------\n")
    if command == "start":
        pause_time = random.randint(int(lower_bound), int(upper_bound)) / 1000
        print("Time started.")
        start_time = time.time()
        time.sleep(pause_time)
        input("Time over - press enter\n")
        end_time = time.time()
        reaction_time = (end_time - start_time) - pause_time
        print("Your reaction speed was {} seconds".format(reaction_time))
    elif command == "settings":
        lower_bound = input("Enter the lower bound: ")
        upper_bound = input("Enter the upper bound: ")
    elif command == "end":
        break
    else:
        print("Invalid command.")
