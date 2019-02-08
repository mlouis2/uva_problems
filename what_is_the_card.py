import sys

non_values_of_ten = ['2', '3', '4', '5', '6', '7', '8', '9']
numTestCases = sys.stdin.readline().strip()

def get_card_value(card):
    if card[0] in non_values_of_ten:
        return int(card[0])
    else:
        return 10

for i in range(0, int(numTestCases)):
    numCards = 0
    cards = []
    while (numCards != 52):
        cardsInLine = sys.stdin.readline().strip().split()
        numCards += len(cardsInLine)
        cards.extend(cardsInLine)
    cards.reverse()
    in_my_hand = cards[0:25]
    cards = cards[25:52]
    y = 0
    for j in range(0, 3):
        y = y + get_card_value(cards[0])
        for k in range(-1, 10 - get_card_value(cards[0])):
            cards.pop(0)
    in_my_hand.extend(cards)
    print("Case " + str(i + 1) + ": " + in_my_hand[len(in_my_hand) - y])
