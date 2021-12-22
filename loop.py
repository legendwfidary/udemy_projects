# don't use len or sum function.
# len = max index of list - 1
heights = input('input list of student heights: ').split(', ')

for n in range(0, len(heights)):
  heights[n] = int(heights[n])

print(heights)

total_height = 0

for x in heights:
  total_height += x




no = 0
for n in heights:
  no += 1

mean = total_height / no
print(f'{int(mean)} is the average height of all the students.')