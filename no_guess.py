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