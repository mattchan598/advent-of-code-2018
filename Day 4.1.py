from collections import defaultdict
import re
lines = []

# Get input and sort lines by time
for line in open("Day_4_input.txt"):
    lines.append(line.strip())
lines.sort()

timeAsleep = defaultdict(int)
guardTimeAsleep = defaultdict(int)

guard = None
sleepTime = None
bestGuard = None
for line in lines:
    words = line.split(" ", 2)

    date = words[0].strip("[")
    time = words[1].rstrip("]")
    message = words[2]
    if "begins shift" in line:
        guard = int(re.search("\d+", message).group())
    elif "falls asleep" in line:
        sleepTime = int(time[3:])
    elif "wakes up" in line:
        wakeTime = int(time[3:])
        guardTimeAsleep[guard] += wakeTime - sleepTime
        for t in range(sleepTime, wakeTime):
            timeAsleep[(guard, t)] += 1

# Search for best guard by which minute they were asleep the most
maxTimeAsleep = 0
maxTimeAsleepGuard = None
print(guardTimeAsleep)
for k,v in guardTimeAsleep.items():
    if v > maxTimeAsleep:
        maxTimeAsleep = v
        maxTimeAsleepGuard = k
print(timeAsleep)
for k,v in timeAsleep.items():
    if bestGuard is None or (v > timeAsleep[bestGuard] and k[0] == maxTimeAsleepGuard):
        bestGuard = k

print("Guard:", bestGuard)
print(bestGuard[0] * bestGuard[1])