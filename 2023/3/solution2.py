# WIP

part_numbers = []

def check_neighbours(y, x, data_list):
    rows = len(data_list)
    cols = len(data_list[0])
    for i, coords in enumerate([(y, x+1), (y+1, x-1), (y+1, x), (y+1, x+1), (y, x-1), (y-1, x-1), (y-1, x), (y-1, x+1)]):
        neighbor_y, neighbor_x = coords
        if 0 <= neighbor_y < rows and 0 <= neighbor_x < cols:
            neighbour = (data_list[neighbor_y][neighbor_x])
            if neighbour.isdigit():
                return True
    return False

with open('data/test.txt', 'r') as file:
    lines = file.read().split('\n')
    for y_coord, row in enumerate(lines):
        row = row + '.'
        number = ''
        for x_coord, char in enumerate(row):
            if char == '*':
                print((y_coord, x_coord), 'has neighbouring number:',
                      check_neighbours(y_coord, x_coord, lines))'

# print(sum(map(int, part_numbers)))
