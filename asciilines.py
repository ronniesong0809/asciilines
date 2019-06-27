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
canvas = [['.'*y]*x]
print(canvas)