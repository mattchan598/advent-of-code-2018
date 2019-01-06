import string
# function that determines if two units are the opposite polarity (two letters are opposite case)
def isOppositePolarity(unit1, unit2):
    return abs(ord(unit1) - ord(unit2)) == 32

# Get input
with open("Day_5_input.txt", "r") as myfile:
    polymer = myfile.read()

copyString = ""

while copyString != polymer:
    copyString = polymer
    for char in string.ascii_lowercase:
        lowerUpperPair = char + char.upper()
        upperLowerPair = char.upper() + char
        polymer = polymer.replace(lowerUpperPair, "")
        polymer = polymer.replace(upperLowerPair, "")

print(len(polymer))