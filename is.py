print('welcome to treasure island!')
print('')
print('A mysterious guy tells you that there is an island that has hidden gold and gems but you have to overcome life-threatening obstacles to get the gold.')
print('Good Luck!')

direction = input('you arrive at a crossroad, do you wanna go left or right? ')

if direction.lower() == 'left':
  print('you took the right path!')
  lake = input('you reach a lake, do you wanna wait for a boat or swim across to the island? ')

  if lake.lower() == 'swim':
    print('you get bitten by an aquatic cobra. Game Over :(')
  
  elif lake.lower() == 'wait':
    print('a boat comes by and takes you to the island but at a cost, the ferry-man tells you when you reach the island, you have to choose a door to go through.')
    print('')
    door = input('each door has a color on it, red, yellow and blue, which door should you go through? ')
    if door.lower() == 'red':
      print('a witch traps you in an unescapable maze. Game Over :(')
    elif door.lower() == 'blue':
      print('the mysterious man greets you like a friend before killing you. Game Over :(')
    elif door.lower() =='yellow':
      print('you find the hidden gold along with rubies, diamonds, sapphires and emeralds and then as you go outside, the mysterious man greets you outside with a smile on his face.')

elif direction.lower() == 'right':
  print('you take the wrong path and face monsters. Game Over :(')
