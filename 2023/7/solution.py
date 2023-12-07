import pprint
grouped_hands = [[], [], [], [], [], [], []]

card_map = {
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14
}


def get_card_counts(hand):
    count_dict = {}
    for card in hand:
        if card in count_dict:
            count_dict[card] += 1
        else:
            count_dict[card] = 1
    return count_dict


def score_hand(hand, bet):
    card_counts = get_card_counts(hand)
    if 5 in card_counts.values():
        grouped_hands[6].append((hand, bet, 'five of a kind'))
    elif len(card_counts) == 2:
        if 4 in card_counts.values():
            grouped_hands[5].append((hand, bet, 'four of a kind'))
        else:
            grouped_hands[4].append((hand, bet, 'full house'))
    elif len(card_counts) == 3:
        if 3 in card_counts.values():
            grouped_hands[3].append((hand, bet, 'three of a kind'))
        else:
            grouped_hands[2].append((hand, bet, 'two pair'))
    elif len(card_counts) == 4:
        grouped_hands[1].append((hand, bet, 'one pair'))
    elif len(card_counts) == 5:
        grouped_hands[0].append((hand, bet, 'high card'))


def convert_card_to_list_of_ints(hand):
    return [card_map[card] for card in hand]


with open('data/test2.txt', 'r') as file:
    lines = file.read().split('\n')
    for line in lines:
        hand, bet = line.split(' ')
        cards = convert_card_to_list_of_ints(hand)
        score_hand(cards, bet)

    for i, group in enumerate(grouped_hands):
        if (len(group) == 0):
            continue
        elif (len(group) == 1):
            grouped_hands[i] = group
        else:
            grouped_hands[i] = sorted(group, key=lambda x: x[0])

    flat_grouped_hands = [
        hand for sublist in grouped_hands for hand in sublist]

    print(sum([int(hand[1]) * (i + 1)
          for i, hand in enumerate(flat_grouped_hands)]))
