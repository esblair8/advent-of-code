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

def map_seed(seed, maps):
    for destination, source, range_length in maps:
        if seed >= source and seed < source + range_length:
            return seed + destination - source
    return seed

for s in seeds:
    for m in parsed_maps:
        s = map_seed(s, m)
    min_seeds.append(s)

print(min(min_seeds))