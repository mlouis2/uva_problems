import sys
for i in range(int(sys.stdin.readline().strip())):
    numsInLine = sys.stdin.readline().strip().split(' ')
    highestNum = 0
    for j in range(1, (int(numsInLine[0])) + 1):
        highestNum = max(int(numsInLine[j]), highestNum)
    print('Case ' + str(i + 1) + ': ' + str(highestNum))
