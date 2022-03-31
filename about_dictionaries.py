# learning about dictionaries.

programming_dictionary = {
  'bug': 'an error in the program that prevents the program from running.',
  'function': 'a piece of code that you can easily call over and over again.',
  'loop': 'the action of doing something over and over again.'
}

# a key is the variable name that holds the info and the item is the info, if u tap into dictionary and specify a key name, you can get that key item{info}
# how to retrieve specific info abut differentkeys in dictionary.
# print(programming_dictionary['bug'])

#an empty dictionary
empty_dictionary = {}

#erasing everything from a dictionary.
#programming_dictionary = {}
#print(programming_dictionary)\

#editing item in dictionary
programming_dictionary['bug'] =  'a moth in your computer.'
#print(programming_dictionary)

#looping through a dictionary
for key in programming_dictionary:
  print(key) # will obtain all the keys
  print(programming_dictionary[key]) # will obtain keys and items
  #btw, when u do thisk it just prints out the keys.
