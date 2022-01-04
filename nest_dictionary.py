# how to nest lists and dictionaries into other dictionaries

# nesting list in a dictionary
travel_log = {
  'Germany': ['Berlin', 'Stuttgart']
  # btw, if you want to keep multiple values for one key, put them in a list.
}

# nesting dictionary in a dictionary
travel_log = {
  'India': {'cities_visited': ['New Delhi', 'Mumbai', 'Chennai']},
  'America': ['New York', 'Los Angeles', 'San Francisco']
}

new_travel_log = {
  'America': {'cities_visited': ['Boston', 'New York', 'Seattle'], 'no_of_visits': [2, 4, 3]},
  'France': {'cities_visited': ['Paris', 'Lille', 'Dijion'], 'no_of_visits': [2, 1, 1]}
}

# nesting dictionary in a list

travel_log = [
  {
    'country': 'Germany', 
    'cities_visited': ['Berlin', 'Stuttgart', 'Hamburg'], 
    'total_visits': 12
  },

  {
    'country': 'America', 
    'cities_visited': ['Boston', 'New York', 'Chicago'], 
    'total_visits': 13
  }
]
