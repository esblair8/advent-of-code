# WIP

import time

start = time.time()
print('start', start)

almanac = open('data/test2.txt').read().split('\n\n')
seeds = list(map(int, almanac[0].split()[1:]))
maps = almanac[1:]

min_seeds = []
parsed_maps = []

for m in maps:
    mp = []
    for line in m.split('\n')[1:]:
        mp.append(list(map(int, line.split(' '))))
    parsed_maps.append(mp)
print('parsed_maps')


def map_seed(seed, maps):
    for destination, source, range_length in maps:
        if seed >= source and seed < source + range_length:
            return seed + destination - source
    return seed


min_seed = float('inf')

for i in range(0, len(seeds), 2):
    print('i', i)
    seed_range = range(seeds[i], seeds[i] + seeds[i + 1])
    for s in seed_range:
        if s > min_seed:
            print('break 1')
            break
        for m in parsed_maps:
            s = map_seed(s, m)
            # check if s is less than min seed value already calculated
            # filter list so that anytonh above s is removed
            # continue to next seed
            if s < min_seed:
                print('s', s)
                min_seed = s
                print('break 2')
                break
        if s < min_seed:
            print('s', s)
            min_seed = s
            print('break 3')
            break

print('min',min_seed)
end = time.time()
print('end', end)
print('time', time.time() - start)
