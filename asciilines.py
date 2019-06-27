import sys

# read from file
filename = sys.argv[1]
file = open(filename)

strings = file.readlines()
print(strings)

# convert to list of list
list=[]
for char in strings:
  char_split = char.split()
  list.append(char_split)
# print(list)

# init canvas
x = int(list[0][0])
y = int(list[0][1])
# print(x,y)

# fill with .
canvas = [['.']*y]*x
# print(canvas)

# render canvas
for line in list[1:]:
  character = line[0] # a character to render with
  row = int(line[1]) # a row position to start at
  column = int(line[2]) # a column position to start at
  direction = line[3] # a direction of horizontal or vertical
  length = int(line[4]) # a length for the rendered line

  for i in range(length):
    # horizontal
    if direction == 'h':
      print(row, column)
      canvas[row][column+i] = character
    # vertical
    if direction == 'v':
      print(row, column)
      canvas[row+i][column] = character
print(canvas)