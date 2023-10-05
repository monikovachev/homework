cards_string = input().split()
count_shuffles = int(input())

for shuffle in range(count_shuffles):
    middle_deck = len(cards_string) // 2
    left_part = cards_string[0:middle_deck]
    right_part = cards_string[middle_deck:]
    deck_shuffled = []
    for card_index in range(len(left_part)):
        deck_shuffled.append(left_part[card_index])
        deck_shuffled.append(right_part[card_index])

    cards_string = deck_shuffled

print(deck_shuffled)


