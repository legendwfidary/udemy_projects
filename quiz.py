# small pizza is 15 $
# medium pizza is 20 $
# large pizza is $ 25
# pepporoni on small pizza is +$2
# pepporoni on medium or large pizza is +$3
# extra cheese for any size pizza is +$1

print('Welcome to python pizza!')
bill = 0

size = input('which size pizza do you want? s,m,l: ')

pepporoni = input('do you want pepporoni on that? y/n: ')
cheese = input('do you want extra cheese on your pizza? y/n: ')


if size.lower() == 's':
  bill += 15
  if pepporoni.lower() == 'y':
    bill += 2

  
  if cheese.lower() == 'y':
    bill += 1

elif size.lower() == 'm':
  bill += 20
  if pepporoni.lower() == 'y':
    bill += 3
  if cheese.lower() == 'y':
    bill += 1

else:
  bill += 25
  if pepporoni.lower() == 'y':
    bill += 3
  if cheese.lower() == 'y':
    bill += 1

print(f'the total bill for your pizza is ${bill}.')