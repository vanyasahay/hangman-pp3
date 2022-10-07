import random

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


def randomWord():
  myword = random.choice(open ('/words.txt').read().split().strip())
  return myword

def board(hangman_display, skippedLetters, correctLetters, hiddenWord):
  print(hangman_diagram[len(skippedLetters)])
  print()

  print('Missed Letters:', end='')
  for letter in skippedLetters:
    print(letter, end='')
  print("\n")

  blanks = '_' * len(hiddenWord)

  for i in range(len(hiddenWord)):
    if hiddenWord[i] in correctLetters:
      blanks = blanks[:i] + hiddenWord[i] + blanks[i+1:]
      for letter in blanks:
        print(letter, end='')
      print("\n")

