import random
words = ['ardvark', 'baboon', 'camel']

chosen_word = random.choice(words)
guess = input('guess a letter: ').lower()

for letter in chosen_word:
  if guess == letter:
    print('right!')
  else:
    print('wrong!')