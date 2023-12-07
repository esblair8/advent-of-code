import pprint

grouped_hands = [[], [], [], [], [], [], []]

card_map = {
    'J': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'Q': 12,
    'K': 13,
    'A': 14
}


def get_card_counts(string):
    count_dict = {}
    for char in string:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1
    return count_dict


def score_hand(hand, bet):
    card_counts = get_card_counts(hand)
    #    added for part 2 to handle the jokers
    if 1 in card_counts.keys() and len(card_counts) > 1:
        no_of_jokers = card_counts[1]
        del card_counts[1]
        max_value = max(card_counts.values())
        max_keys = max([key for key, value in card_counts.items() if value == max_value])
        card_counts[max_keys] += no_of_jokers
   
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


def convert_face_cards(hand):
    return [card_map[card] for card in hand]


with open('data/test2.txt', 'r') as file:
    lines = file.read().split('\n')
    for line in lines:
        hand, bet = line.split(' ')
        hand = convert_face_cards(hand)
        score_hand(hand, bet)

    for i, group in enumerate(grouped_hands):
        if (len(group) == 0):
            continue
        elif (len(group) == 1):
            grouped_hands[i] = group
        else:
            grouped_hands[i] = sorted(group, key=lambda x: x[0])

    flat_grouped_hands = [
        hand for sublist in grouped_hands for hand in sublist]

#   pprint.pprint(flat_grouped_hands)
    print(sum([int(hand[1]) * (i + 1)
          for i, hand in enumerate(flat_grouped_hands)]))
