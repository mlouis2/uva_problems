import sys
import re

first = True
for line in sys.stdin:
    line = line.strip()
    if not first:
        x, y = re.split(r'\s+', line)
        x = int(x)
        y = int(y)
        if (x < y):
            print ('<')
        elif (x > y):
            print('>')
        else:
            print('=')
    first = False
