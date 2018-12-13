import time
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
appeared = {0}
ans = 0
t0 = time.time()
while not found:
    for i in nums:
        sum += i
        if sum not in appeared:
            appeared.add(sum)
        else:
            ans = sum
            found = True
            break
t1 = time.time()
print(ans)
print(t1-t0)
