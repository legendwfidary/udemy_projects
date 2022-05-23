# Higher Lower Game Project
from game_data import data
from art_four import logo, vs
import random
from replit import clear

def format_data(account):
  ''''takes the account data and returns them in a printasble format.'''
  account_name = account['name']
  account_descr = account['description']
  account_country = account['country']
  return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
  '''takes the user's guess and follower accounts and returns if they got it right.'''
  if a_followers > b_followers:
    return guess == 'a'
    # here, it checks if our guess is a and if right, it returns true or it returns false. same for b
  if b_followers > a_followers:
    return guess == 'b'

# display the game logo when the game starts.
'''prints the logo in the start of the game.'''
print(logo)
score = 0
game_should_continue = True
b = random.choice(data)

# make the game repeatable.
while game_should_continue:

  # generate a random account from the game data.
  '''gets 2 random accounts and makes sure both are different.'''
  a = b
  b = random.choice(data)
  
  while a == b:
    b = random.choice(data)
  
  '''prints out both the accounts and calls the function to format them into the one in the game.'''
  print(f"Compare A: {format_data(a)}")
  # display vs logo inbetween the account displays.
  print(vs)
  print(f"Against B: {format_data(b)}")
  
  # Ask user for a guess.
  guess = input("Who has more followers? A or B: ").lower()
  
  
  # check if user is correct.
  ## get follower_count of each account.
  a_follower_account = a['follower_count']
  b_follower_account = b['follower_count']
  is_correct = check_answer(guess, a_follower_account, b_follower_account)

  # clear the screen before rounds.
  clear()
  print(logo)
  
  # give user feedback on their guess.
  # score keeping.
  
  if is_correct:
    score += 1
    print(f'You are right! Current score: {score}.')
    
  else:
    print(f'You are wrong! Final score: {score}.')
    game_should_continue = False
