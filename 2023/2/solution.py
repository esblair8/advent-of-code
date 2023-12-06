with open('data/test2.txt', 'r') as file:
    valid_games = []
    lines = file.read().split('\n')
    for line in lines:
        data = line.split(':')
        game_id = data[0].split(' ')[1]
        picks = data[1].split(';')
        games = []
        valid_picks = []
        for i, pick in enumerate(picks):
            count_and_colors = pick.split(',')
            for count_and_color in count_and_colors:
                count, color = count_and_color.strip().split(' ')
                count = int(count)
                if (color == 'red' and count <= 12) or (color == 'green' and count <= 13) or (color == 'blue' and count <= 14):
                    valid_picks.append(True)
                else:
                    valid_picks.append(False)
        if (all(valid_picks)):
            valid_games.append(game_id)
    print(sum(map(int, valid_games)))
