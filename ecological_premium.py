import sys
import re
numCases = sys.stdin.readline().strip()
for i in range(0, int(numCases)):
    numFarmers = sys.stdin.readline().strip()
    total = 0
    for j in range(0, int(numFarmers)):
        (sizeOfFarmyard, numAnimalsOwned, environmentalFriendliness) = sys.stdin.readline().split(" ")
        total += (int(sizeOfFarmyard) * int(environmentalFriendliness))
    print(total)
