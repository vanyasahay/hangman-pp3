import random
import sys
wordlist = "words.txt"

selection = None
while selection !="0":
    print('''
    -------------------
    Welcome to Hangman
    -------------------
    Please select  a menu option:
    0 - Exit
    1 - Play Game

''')

selection=input("Do you want to play?:")

if selection == "0":
    sys.exit("Bye Bye")
    elif selection =="1":





hangman_diagram = ["""
SAVE ME PLEASE- YOU HAVE 6 LIFELINES

   +---+
   |   |
       |
       |
       |
       |
=========""", """
YOU CAN SAVE ME- 5 TURNS TO GO

  +---+
  |   |
  O   |
      |
      |
      |
=========""", """
STILL HOPING- 4 MORE TURNS

  +---+
  |   |
  O   |
  |   |
      |
      |
=========""", """
YOU CAN DO THIS - 3 MORE

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""", """
I BELIEVE IN YOU - 2 MORE

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""", """

YOU ARE THE BEST - LAST CHANGE
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""", """
BYE BYE- TAKE CARE!

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========="""]
