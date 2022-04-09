from replit import clear
import art
#HINT: You can call clear() to clear the output in the console.

print(art.gavel_logo)
print('welcome to the secret auction program.')

# make empty dict
bid_records = {}
bidding_finished = False

def find_highest_bidder(bidding_records):
  highest_bidder = 0
  winner = ''
  
  for bidder in bidding_records:
    bid_amount = bidding_records[bidder]
    if bid_amount > highest_bidder:
      highest_bidder = bid_amount
      winner = bidder
  print(f'the winner of the secret auction is {winner} with a bid of ${highest_bidder}.')
  
    

while not bidding_finished:
  name = input('what is your name? ')
  bid = int(input('what is your bid? $'))
  
  # saving record to dict
  bid_records[name] = bid
  
  bidders = input('are there any other bidders? yes/no? ')
  if bidders.lower() == 'no':
    bidding_finished = True
    find_highest_bidder(bid_records)
  
  elif bidders.lower() == 'yes':
    clear()



