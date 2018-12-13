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
for n in lines:
    nums.append(int(n))

#sum up the list
ans = sum(nums)
print(ans)