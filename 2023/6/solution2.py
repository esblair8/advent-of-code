import re
from functools import reduce
import time

start = time.time()
print('start', start)

def calculate(race_time, distance):
    distances = []
    for i in range(0, race_time + 1):
        time_left = race_time - i
        distance_travelled = time_left * i
        if distance_travelled > distance:
            distances.append(distance_travelled)
    return distances

with open('data/test2.txt', 'r') as file:
    lines = file.read().replace(' ', '').split('\n')
    race_time, distance = [int(re.findall(rf'\d+', line)[0]) for line in lines]
    print(len(calculate(race_time, distance)))

end_time = time.time()
print('end', end_time)
print('time', end_time - start)