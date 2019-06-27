import sys

# read from file
filename = sys.argv[1]
file = open(filename)

strings = file.readlines()
print(strings)