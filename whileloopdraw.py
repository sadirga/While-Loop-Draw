# This is the first one: left side triangle
line = '*'
max_length = 5

while len(line) <= max_length:
    print(line)
    line += "*"
print()

# This is the second one: 
line = '*'
max_length = 5

while len(line) <= max_length:
    print(line)
    line += "*"
    
while len(line) > 0:
    print(line)
    line = line[:-1]
print()

# This is the third one:
line = '*'
max_length = 5

while len(line) <= max_length:
    if len(line) == max_length:
        break
    print(" "*(max_length-len(line)) + "*"*len(line))
    line += "*"
while len(line) > 0:
    print(" "*(max_length-len(line)) + "*"*len(line))
    line = line[:-1]
print()

# This is the last one: Diamond
line = '*'
max_length = 5

while len(line) <= max_length:
    if len(line) == max_length:
        break
    print(" "*(max_length-len(line)) + "* "*len(line))
    line += "*"
print(len(line))
while len(line) > 0:
    print(" "*(max_length-len(line)) + "* "*len(line))
    line = line[:-1]
