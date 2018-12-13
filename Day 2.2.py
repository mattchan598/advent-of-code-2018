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

ids = []

for line in lines:
    ids.append(line.strip())


# Part 2
for x in ids:
    for y in ids:
        diff = 0
        for i in range(len(x)):
            if x[i] != y[i]:
                diff += 1
        if diff == 1:
            ans = []
            for i in range(len(x)):
                if x[i] == y[i]:
                    ans.append(x[i])

print(''.join(ans))