import re
import pprint

matches = []
with open('data/test2.txt', 'r') as file:
    lines = file.read().split('\n')
    for y, row in enumerate(lines):
        parts = row.split(':')
        game_id = int(re.findall(rf'\d+', parts[0])[0])
        numbers = parts[1].split('|')
        winning_nos = numbers[0].strip().split()
        numbers_you_have = numbers[1].strip().split()
        intersection = list(set(winning_nos) & set(numbers_you_have))
        winners = len(intersection)
        matches.append(winners)

totalsTracker = [1] * len(matches)

for i, n in enumerate(matches):
    for j in range(i + 1, i + n + 1):
        totalsTracker[j] += totalsTracker[i]

print(sum(totalsTracker))
