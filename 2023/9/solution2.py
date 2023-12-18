def calculate_diffs(line_list):
    diffs = [line_list[i+1] - line_list[i] for i in range(len(line_list) - 1)]
    return diffs


sums = []
with open('data/test2.txt', 'r') as file:
    lines = file.read().split('\n')
    for line in lines:
        diffs = []
        line_list = list(map(int, line.split(' ')))
        diffs.append(line_list)
        current_diffs = calculate_diffs(line_list)
        diffs.append(current_diffs)
        while not all([diff == 0 for diff in current_diffs]):
            current_diffs = calculate_diffs(current_diffs)
            diffs.append(current_diffs)
        diffs.reverse()
        print(diffs)
        for i, diff in enumerate(diffs):
            if i != 0:
                previous_row_last_value = diffs[i-1][0]
                current_last_value = diff[0]
                print(previous_row_last_value, current_last_value)
                diff.insert(0, current_last_value - previous_row_last_value)
        sums.append(diffs[-1][0])
print(sums)
print(sum(sums))
