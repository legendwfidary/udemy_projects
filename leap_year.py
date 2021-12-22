# ages 45-55 typically go through mid life crisis.
height = int(input('what is your height (in cm): '))
bill = 0
mid_crisis = False

if height >= 12:
  print('you can ride on the rollercoaster.')
  age = int(input('please enter your age: '))

  if age <= 12:
    bill = 5
    print('children tickets are 5 rs.')
  elif age < 21:
    bill = 7
    print('teenagers tickets are 7 rs')

  elif age >= 45 and age <= 55:
    
    print('since you are going through mid life crisis, your tickets are free.')
    mid_crisis = True
  
  else:
    bill = 12
    print('adult tickets are 12 rs.')
  
  photo = input('do you want a photo taken? y/n: ')

  if photo.lower() == 'y':
    if mid_crisis:
      bill = 0
    else:
      bill += 3
    print('enjoy the ride!')
    print(f'the total bill is {bill} rs.')
  else:
    print('enjoy the ride!')
    print(f'the total bill is {bill} rs.')



else:
  print('you cannot go to the ride.')