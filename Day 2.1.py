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