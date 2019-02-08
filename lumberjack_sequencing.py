import sys
import re

first = True
for line in sys.stdin:
    line = line.strip()
    if (first):
        print('Lumberjacks:')
        first = False
    else:
        ascending = True;
        descending = True;
        nums = re.split(r'\s+', line)
        nums = [int(x) for x in nums]
        if (nums == sorted(nums) or nums == sorted(nums, reverse=True)):
            print('Ordered')
        else:
            print('Unordered')
