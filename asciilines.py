import sys

if len(sys.argv) != 2:
  print("Please included a test case. USAGE: python3 asciilines.py tests/test1.tvg")
  exit()

# read from file
filename = sys.argv[1]
file = open(filename)

strings = file.readlines()
# print(strings)

# convert to list of list
list=[]
for char in strings:
  char_split = char.split()
  list.append(char_split)
# print(list)

# init canvas
if len(list[0])!=2:
  print("Invalid input, the " + str(list[0]) + " sizing command need to containing only 2 characters.")
  exit()

# if list[0][0]!=int or list[0][1]!=int:
#   print("Invalid input, the " + str(list[0]) + " rendering command need to containing [int] [int].")
#   exit()

x = int(list[0][0])
y = int(list[0][1])
# print(x,y)

# fill with .
canvas= []
for i in range(x):
  canvas_row = []
  for j in range(y):
    canvas_row.append('.')
  canvas.append(canvas_row)
# print(canvas)

# render canvas
for line in list[1:]:
  if len(line)!=5:
    print(line)
    print("Invalid input, the " + str(line) + " rendering command need to containing only 5 characters.")
    exit()

  # if line[0]!=str or line[1]!=int or line[2]!=int or line[3]!=str or line[4]!=int:
  #   print('Invalid input, the " + str(line) + " rendering command need to containing [char] [int] [int] [char] [int].')
  #   exit()

  character = line[0] # a character to render with
  row = int(line[1]) # a row position to start at
  column = int(line[2]) # a column position to start at
  direction = line[3] # a direction of horizontal or vertical
  length = int(line[4]) # a length for the rendered line

  if length<0:
    print("Invalid length, the length [" + str(length) +"] for the rendered line need to be positive.")
    exit()

  for i in range(length):
    # horizontal
    if direction == 'h':
      if column+i < y:
        canvas[row][column+i] = character
    # vertical
    elif direction == 'v':
      if row+i < x:
        canvas[row+i][column] = character
  # print(canvas)

# display
for line in canvas:
  for c in line:
    print(c, end='')
  print(end='\n')
