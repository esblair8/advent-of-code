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
    lines = file.read().replace(' ', '').split('\n')
    time, distance = [re.findall(rf'\d+', line) for line in lines]
    print(len(calculate(int(time[0]), int(distance[0]))))
