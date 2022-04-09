# running functions with outputs


# note: if you want to make all the words in a string title case (ie first letter upper case and other letters lower case), write the variable and add a .title() to it.
# before: my name is karthik.
# after: My Name Is Karthik.
# see docs for more info.

def format_name(f_name, l_name):
  if f_name == '' or l_name == '':
    return 'provide something!'
  format_f = f_name.title()
  format_l = l_name.title()
  # note: here, the function that gets called outside is replaced with the output (function that is returned). so now, we can hold a variable for it and use it.
  return f'{format_f} {format_l}'
  # everything after return replaces the function called outside. also return function ends the function, so keep it at end.
  

formatted_string = format_name(input('what is your first name? '), input('what is your last name? '))
print(formatted_string)
# return function in functions are like break in loops.
# so, if you want to skip over a function cuz info is not given or is wrong, you can simply check the info and write return to skip over the rest of the function.