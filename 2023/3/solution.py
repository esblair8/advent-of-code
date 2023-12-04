part_numbers = []


def get_coordinates(y, x):
    return [(y, x+1), (y+1, x-1), (y+1, x),
            (y+1, x+1), (y, x-1),
            (y-1, x-1), (y-1, x), (y-1, x+1)
    ]


def check_neighbours(y, x, data_list):
    rows = len(data_list)
    cols = len(data_list[0])
    for i, coords in enumerate(get_coordinates(y, x)):
        (neighbor_y, neighbor_x) = coords
        if 0 <= neighbor_y < rows and 0 <= neighbor_x < cols:
            neighbour = (data_list[neighbor_y][neighbor_x])
            if neighbour in '*#!@£$%^&*()?+=[];:|\/<>~`±§#¢∞_-¶ªº':
                return True
    return False


with open('data/test2.txt', 'r') as file:
    lines = file.read().split('\n')
    for y_coord, row in enumerate(lines):
        row = row + '.'
        number = ''
        for x_coord, char in enumerate(row):
            if char.isdigit():
                number += char
                if not row[x_coord + 1].isdigit():
                    print(number)
                    if check_neighbours(y_coord, x_coord, lines) or check_neighbours(y_coord, x_coord - 1, lines) or ((len(number) > 2 and check_neighbours(y_coord, x_coord-2, lines))):
                        part_numbers.append(number)
                    number = ''

print(part_numbers)
print('SUM ALL PART NUMBERS', sum(map(int, part_numbers)))
