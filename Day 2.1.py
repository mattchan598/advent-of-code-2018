import string
# Get inputs and put them into lines
lines = []
try:
    f = open("Day_2_input.txt", "r")
    try:
        lines = f.readlines()
    finally:
        f.close()
except IOError:
    pass

# Create a dictionary of lowercase letters
d = dict.fromkeys(string.ascii_lowercase, 0)
num_twos = 0
num_threes = 0

for line in lines:
    for letter in line.strip():
        d[letter] += 1
    if 2 in d.values():
        num_twos += 1
    if 3 in d.values():
        num_threes += 1
    d = dict.fromkeys(string.ascii_lowercase, 0)
print(num_twos)
print(num_threes)
print(num_twos*num_threes)