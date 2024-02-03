deck_of_cards = input().split()
count_of_shuffles = int(input())

for current_shuffle in range(count_of_shuffles):
    half_of_the_deck = len(deck_of_cards) // 2
    left_side = deck_of_cards[:half_of_the_deck]
    right_side = deck_of_cards[half_of_the_deck:]
    shuffled_deck = []
    for current_card in range(half_of_the_deck):
        shuffled_deck.append(left_side[current_card])
        shuffled_deck.append(right_side[current_card])
    deck_of_cards = shuffled_deck

print(shuffled_deck)
