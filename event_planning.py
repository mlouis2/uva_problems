import sys
import re

caseInfo = sys.stdin.readline().strip()
while (caseInfo != ''):
    minCost = 0;
    (numParticipants, budget, numHotels, numWeeks) = caseInfo.split(" ")
    for i in range(0, int(numHotels)):
        priceOfOnePerson = sys.stdin.readline().strip()
        availableBeds = sys.stdin.readline().strip().split(" ")
        for bedsInWeekend in availableBeds:
            if (int(bedsInWeekend) >= int(numParticipants)):
                if (minCost == 0 or minCost > int(priceOfOnePerson) * int(numParticipants)):
                    if(int(priceOfOnePerson) * int(numParticipants) <= int(budget)):
                        minCost = int(priceOfOnePerson) * int(numParticipants)
    if (minCost != 0):
        print(minCost)
    else:
        print('stay home')
    caseInfo = sys.stdin.readline().strip()
