from replit import clear
from art_two import logos
# tips: recursion - this is used in programming where you call the function inside the same function you are calling, what this will do is it will when the code for calling the function is run, it restarts the function and erases all previous data, eg: line 45.
# be careful with recursing as it may result in infinite loop, therefore keep it in a condition.
#Calculator
def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

print(logos)
def calculator():
  
  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  
  should_continue = True
  
  while should_continue:
    operation_symbol = input("Pick an operation: ") 
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    
    print(f"{num1} {operation_symbol} {num2} = {answer}")
  
    next_time = input(f'do you want to keep calculating with {answer} or start new calculation? y/n: ')
    if next_time.lower() == 'y':
      num1 = answer
    else:
      should_continue = False
      clear()
      calculator()
calculator()