from os import system, name
import random
import time

#Reaction Speed Tester By Robin Barnes
#Might make an autoclicker next
#Need to port this to rust as well
#Then I might experiment with GUIs

lower_bound = 250
upper_bound = 5000
repeat = "true"

###Trying to modularise my code into functions here for easier scaling###

def reset():
    lower_bound = 250
    upper_bound = 5000
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
        
def cake():
  print("The cake was a lie")

def settings():
  lower_bound = input("Enter the lower bound: ")
  upper_bound = input("Enter the upper bound: ")
  

def start():
  pause_time = random.randint(int(lower_bound), int(upper_bound)) / 1000
  print("Time started.")
  start_time = time.time()
  time.sleep(pause_time)
  input("Time over - press enter\n")
  end_time = time.time()
  reaction_time = (end_time - start_time) - pause_time
  print("Your reaction speed was {} seconds".format(reaction_time))

while "true":
    command = input("---------------------------------\n|Type settings to change config.|\n|Type start to begin.           |\n|Type end to finish.            |\n|Type reset to reset and clear. |\n---------------------------------\n")
    if command == "cake":
       cake()
    elif command == "reset":
      reset()
    elif command == "start":
      start()
    elif command == "settings":
      settings()
    elif command == "end":
        break
    else:
        print("Invalid command.")
