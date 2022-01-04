<<<<<<< HEAD

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(country, total_visits, cities_visited):
  new_dict = {}

  new_dict['country'] = country
  new_dict['visits'] = total_visits
  new_dict['cities'] = cities_visited
  travel_log.append(new_dict)


#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)


=======
>>>>>>> origin/main
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for student in student_scores:
  score = student_scores[student]
  if score > 90:
    student_grades[student] = 'Outstanding'
  elif score > 80:
    student_grades[student] = 'Exceeds Expectations'
  elif score > 70:
    student_grades[student] = 'Acceptable'
  else:
    student_grades[student] = 'Fail'



# 🚨 Don't change the code below 👇
<<<<<<< HEAD

print(student_grades)


print(student_grades)

=======
print(student_grades)
>>>>>>> origin/main
