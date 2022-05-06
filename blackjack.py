############### Blackjack Project

import random
from replit import clear
from art_three import logo

def deal_card():
  # returns a random card from the deck.
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
  # checks for blackjack and returns score as 0 if yes.
  if sum(cards) == 21 and len(cards) == 2:
    return 0
    
  # checking if busted over and ace, replacing ace with 1 and returning new score if satisfied.
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
    return sum(cards)
  # return the sum of the cards in the current hand.
  return sum(cards)

# compares the user score and computer score and returns the result.
def compare(user_score, computer_score):
  if user_score == computer_score:
    return "Draw!"
  elif computer_score == 0:
    return "Computer has Blackjack, User loses!"
  elif user_score == 0:
    return "User has Blackjack, User wins!"
  elif user_score > 21:
    return "User score is over 21, User loses!"
  elif computer_score > 21:
    return "Computer score is over 21, User wins!"
  elif user_score > computer_score:
    return "User score is higher than computer score, User wins!"
  else:
    return "Computer score is higher than user score, User loses!"

def play_game():
  # prints art logo.
  print(logo)
  
  user_cards = []
  computer_cards = []
  is_game_over = False
  
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
   
  while not is_game_over:
    # takes a list of cards and returns score calculated from cards.
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
  
    # prints the cards and scores of players.
    print(f"User's cards: {user_cards}, score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")
  
    # checks if players have blackjack or user has busted out, ends game if true.
    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
      
    # asks user to draw card, if yes draws a new card, updates score and checks again.
    else:
      draw_card = input('do you want to draw another card? y/n: ')
      if draw_card.lower() == 'y':
        user_cards.append(deal_card())
        
      else:
        is_game_over = True
        
    # after user plays, computer keeps getting card until score is 17 or higher unless it has blackjack before
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  # after both players finish their turns, they print the final cards and result of each player and then starts to compare their scores for a result.
  print(f"Your final cards: {user_cards}, final score: {user_score}")
  print(f"Computer's final cards: {computer_cards}, final score: {computer_score}")
  # comapres the player's score and returns a result.
  print(compare(user_score, computer_score))

while input('do you want to start a new game? y/n: ') == 'y':
  # asks player to restart game, if y, then clear the screen and restart the game using the play_game() function.
  clear()
  play_game()