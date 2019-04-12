import sys
from collections import OrderedDict

case_num = 0

while True:
    num_drinks = sys.stdin.readline().strip()
    if not num_drinks:
        print('')
        break
    if case_num != 0:
        print('')
    case_num += 1
    drinks = OrderedDict()

    for i in range(0, int(num_drinks)):
        drink = sys.stdin.readline().strip()
        drinks[drink] = [0, []]

    num_orderings = int(sys.stdin.readline().strip())

    for i in range(0, num_orderings):
        drinkA, drinkB = sys.stdin.readline().strip().split()
        drinks[drinkA][1].append(drinkB)
        drinks[drinkB][0] += 1

    beverage_order = ""
    while (len(drinks) > 0):
        for key, value in drinks.items():
            if (value[0] == 0):
                for successor in range(0, len(value[1])):
                    drinks.get(value[1][successor])[0] -= 1
                beverage_order = beverage_order + ' ' + key
                drinks.pop(key)
                break

    sys.stdin.readline().strip()

    print('Case #' + str(case_num) + ': Dilbert should drink beverages in this order:' + beverage_order + '.')
