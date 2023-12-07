import re
from functools import reduce

def calculate(time, distance):
    distances = []
    for i in range(0, time + 1):
        time_left = time - i
        distance_travelled = time_left * i
        if distance_travelled > distance:
            distances.append(distance_travelled)
    return distances

with open('data/test2.txt', 'r') as file:
    lines = file.read().split('\n')
    time_and_distances = [(re.findall(rf'\d+', line)) for line in lines]
    print(reduce(lambda acc, race: acc * len(calculate(int(race[0]), int(race[1]))), zip(time_and_distances[0], time_and_distances[1]), 1))
