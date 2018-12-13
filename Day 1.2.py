# Get inputs and put them into lines
lines = []
try:
    f = open("Day_1_input.txt", "r")
    try:
        lines = f.readlines()
    finally:
        f.close()
except IOError:
    pass

# Convert strings in lines to ints
nums = []
for x in lines:
    nums.append(int(x))

# sum up the list and try to find a matching number
sum = 0
found = False
appeared = []
ans = 0
while not found:
    for i in nums:
        sum += i
        print(sum)
        if sum not in appeared:
            appeared.append(sum)
        else:
            ans = sum
            found = True
            break
print(ans)
