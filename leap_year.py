# this program helps us find no of days in months in years!
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(any_year, any_month):
  if any_month > 12 or any_month < 1:
    return 'invalid inPUt!'.title()
    
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  is_leap_year = is_leap(any_year)

  if is_leap_year == True:
    month_days[1] = 29
    return f'there are {month_days[any_month - 1]} days in this month in this year.'
  else:
    return f'there are {month_days[any_month - 1]} days in this month in this year.'
  
  
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
