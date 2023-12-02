games = []

with open("test2.txt", "r") as file:
    lines = file.read().split("\n")
    for line in lines:
        game_id = line.split(":")[0].split(" ")[1]
        picks = line.split(":")[1].split(";")
        count_dict = {'red': 0, 'green': 0, 'blue': 0}
        for i, pick in enumerate(picks):
            count_and_colors = pick.split(",")
            for count_and_color in count_and_colors:
                (count, color) = count_and_color.strip().split(" ")
                count = int(count)
                if count > count_dict[color]:
                    count_dict[color] = count
        games.append(count_dict['red'] * count_dict['green'] * count_dict['blue'])

print(sum(games))
