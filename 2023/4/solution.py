from functools import reduce

final_total = 0

with open('data/test2.txt', 'r') as file:
    lines = file.read().split('\n')
    for y, row in enumerate(lines):
        parts = row.split(':')
        game_id = parts[0].split(' ')[1]
        numbers = parts[1].split('|')
        winning_nos = numbers[0].strip().split()
        numbers_you_have = numbers[1].strip().split()
        intersection = list(set(winning_nos) & set(numbers_you_have))
        winners = len(intersection)
        final_total += winners if winners <= 2 else reduce(
            lambda x, _: x * 2, range(winners - 1), 1)

print('final_total', final_total)
