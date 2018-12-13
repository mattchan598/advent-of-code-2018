#Get inputs and put them into lines
try:
    f = open("Day_1_input.txt", "r")
    try:
        lines = f.readlines()
    finally:
        f.close()
except IOError:
    pass

#Convert strings in lines to ints
nums = []
for x in lines:
    nums.append(int(x))

#sum up the list
sum = 0
for i in nums:
    sum += i

print(sum)