array = []
with open("file.txt") as f:
    array = f.read().splitlines()
#with open("file.txt", "r") as f:
 # for line in f:
  #  array.append(line)
lines = [line.rstrip('\n') for line in open('file.txt')]
print lines
