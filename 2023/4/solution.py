def get_score(winners):
    total = 1
    for x in range(1, winners):
        total *= 2
    return total


final_total = 0

with open('data/test2.txt', 'r') as file:
    lines = file.read().split('\n')
    for y, row in enumerate(lines):
        parts = row.split(':')
        card_no = parts[0][-1]
        numbers = parts[1].split('|')
        winning_nos = numbers[0].strip().split()
        numbers_you_have = numbers[1].strip().split()
        intersection = list(set(winning_nos) & set(numbers_you_have))
        score = 0
        winners = len(intersection)
        if winners > 0:
            if winners == 1:
                score += 1
            elif winners == 2:
                score += 2
            else:
                score += get_score(winners)
        print(intersection, winners, score)
        final_total += score
print('final_total', final_total)
