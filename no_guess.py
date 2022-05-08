#   Number Guessing Game

import random

no_of_guesses = 10


# random no from 1 to 100
no = random.randint(1, 100)

print('Welcome to the Number Guessing Game!')
print("I'm thinking of a no between 1 and 100")
# print(no)



def play_game():
  
  is_game_over = False
  level = input('do you want easy or hard level? ')
  if level.lower() == 'easy':
    no_of_guesses = 10
  else:
    no_of_guesses = 5
  
  while not is_game_over:
    if no_of_guesses == 0:
      print("You're out of guesses, You lose!")
      is_game_over = True
      return
    
    print(f'you have {no_of_guesses} attempts left.')
    guess = int(input('make a guess: '))
  
    if guess == no:
      print(f'You got it! the answer was {guess}.')
      is_game_over = True
      
    else:
      print('Wrong!')
      if guess < no:
        print('Too Low!')
      elif guess > no:
        print('Too High!')
      no_of_guesses -= 1
    

play_game()

# local scope: it is for variables or functions that are made within other functions so it can only be accessed inside said function which means that variable or function has local scope.
# global scope: it is a function or variable that is accessible both inside and outside functions.
# namespace: anything you give a name to has a namespace and each namespace has a certain scope.
# note: there is no block scope in python i.e: if you create a variable in a loop or a statement, it can be accessed both inside and outside it (it's a gloabl variable) but when it's in a function, it becomes a local variable.

# Modifying global scope
# note: as much as you can, avoid modifying variables inside functions, instead try to use return.
'''enemies = 1

def increase_enemies():
  global enemies
  enemies += 1
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")
'''

# Global constants
