import sys
count = 0
first = True

def getSurroundingSpots(map, row, col):
    surroundingSpots = []
    if (row != 0):
        if (col != 0):
            surroundingSpots.append([row - 1, col - 1])
        surroundingSpots.append([row - 1, col])
        if (col != len(map[0]) - 1):
            surroundingSpots.append([row - 1, col + 1])
    if (col != len(map[0]) - 1):
        surroundingSpots.append([row, col + 1])
        if (row != len(map) - 1):
            surroundingSpots.append([row + 1, col + 1])
    if (row != len(map) - 1):
        surroundingSpots.append([row + 1, col])
        if (col != 0):
            surroundingSpots.append([row + 1, col - 1])
    if (col != 0):
        surroundingSpots.append([row, col - 1])
    return surroundingSpots

numRows, numCols = sys.stdin.readline().strip().split()
while (numRows != '0'):
    if (not first):
        print('')
    count = count + 1
    map = [[0] * int(numCols) for i in range(int(numRows))]
    finalMap = [['0'] * int(numCols) for i in range(int(numRows))]
    for i in range(0, int(numRows)):
        map[i] = sys.stdin.readline().strip()
    # for each map go through n look for mines !
    for j in range(0, int(numRows)):
        for k in range(0, int(numCols)):
            if (map[j][k] == '*'):
                finalMap[j][k] = '*'
                surroundingSpots = getSurroundingSpots(map, j, k)
                for l in range(0, len(surroundingSpots)):
                    if (map[surroundingSpots[l][0]][surroundingSpots[l][1]] != '*'):
                        finalMap[surroundingSpots[l][0]][surroundingSpots[l][1]] = str(int(finalMap[surroundingSpots[l][0]][surroundingSpots[l][1]]) + 1)
    print('Field #' + str(count) + ":")
    for m in range(0, int(numRows)):
        row = ''
        for n in range(0, int(numCols)):
            row = row + finalMap[m][n]
        print(row)
    first = False
    numRows, numCols = sys.stdin.readline().strip().split()
