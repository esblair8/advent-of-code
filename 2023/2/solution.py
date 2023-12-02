import pprint

RED = 12
GREEN = 13
BLUE = 14
valid_games = []

with open("test2.txt", "r") as file:
    lines = file.read().split("\n")
    for line in lines:
        game_id = line.split(":")[0].split(" ")[1]
        picks = line.split(":")[1].split(";")
        games = []
        valid_picks = []
        for i, pick in enumerate(picks):
            count_and_colors = pick.split(",")
            for count_and_color in count_and_colors:
                (count, color) = count_and_color.strip().split(" ")
                count = int(count)
                if (color == 'red' and count <= RED) or (color == 'green' and count <= GREEN) or (color == 'blue' and count <= BLUE):
                    valid_picks.append(True)
                else:
                    valid_picks.append(False)
        if (all(valid_picks)):
            valid_games.append(game_id)
print(valid_games)
print(sum(map(int, valid_games)))
