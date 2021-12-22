name1 = input('enter your name: ').lower()
name2 = input('enter their name: ').lower()

total = name1 + name2


count1 = total.count('t')
count2 = total.count('r')
count3 = total.count('u')
count4 = total.count('e')
first = count1 + count2 + count3 + count4
tcount1 = total.count('l')
tcount2 = total.count('o')
tcount3 = total.count('v')
tcount4 = total.count('e')
second = tcount1 + tcount2 + tcount3 + tcount4

percentage = int(str(first) + str(second))


if percentage < 10 or percentage > 90:
  print(f'your score is {percentage}%, you go together like coke and mentos,')
elif percentage >= 40 and percentage <= 50:
  print(f'your score is {percentage}%, you are alright together.')

else:
  print(f'your score is {percentage}%')

