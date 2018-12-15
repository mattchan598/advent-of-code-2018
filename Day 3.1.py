import re
# Initialize 1000x1000 grid with empty arrays
fabric = [[[] for y in range(1000)] for x in range(1000)]

regClaimID = "#[\d]+"
regClothPlacement = "[\d]+,[\d]+"
regClothSize = "[\d]+x[\d]+"

for line in open("Day_3_input.txt"):
    claimID = re.search(regClaimID, line).group()
    clothPlacement = re.search(regClothPlacement, line).group()
    clothSize = re.search(regClothSize, line).group()

    claimID = int(claimID.lstrip("#"))
    clothPlacementX = int(clothPlacement.split(",")[0])
    clothPlacementY = int(clothPlacement.split(",")[1])
    clothSizeX = int(clothSize.split("x")[0])
    clothSizeY = int(clothSize.split("x")[1])

    for i in range(clothPlacementX, clothPlacementX + clothSizeX):
        for j in range(clothPlacementY, clothPlacementY + clothSizeY):
            fabric[i][j].append(claimID)

sum = 0
for x in range(1000):
    for y in range(1000):
        if len(fabric[x][y]) > 1:
            sum += 1

print(sum)
