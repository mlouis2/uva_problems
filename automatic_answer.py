import sys
for i in range(int(sys.stdin.readline().strip())):
    value = (int(sys.stdin.readline().strip()));
    value = value * 567;
    value = value // 9;
    value = value + 7492;
    value = value * 235;
    value = value // 47;
    value = value - 498;
    value = abs(value);
    value = value // 10;
    value = value % 10;
    print(value)
