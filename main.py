weight = float(input('please enter your height in kg: '))
height = float(input('please enter your height in m: '))

bmi = weight / (height ** 2)
bmi = round(bmi)


if bmi  < 18.5:
  print(f'your bmi is {bmi}, you are underweight.')
elif bmi < 25:
  print(f'your bmi is {bmi}, you are normal weight.')
elif bmi < 30:
  print(f'your bmi is {bmi}, you are overweight.')
elif bmi < 35:
  print(f'your bmi is {bmi}, you are obese.')

else:
  print(f'your bmi is {bmi}, you are clinically obese.')