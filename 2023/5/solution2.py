almanac = open('data/test.txt').read().split('\n\n')
seeds = list(map(int, almanac[0].split()[1:]))
maps = almanac[1:]
part_two_seed = list(range(seeds[0], seeds[0] + seeds[1])) + list(range(seeds[2], seeds[2] + seeds[3]))
min_seeds = []
parsed_maps = []

for m in maps:
    mp = []
    for line in m.split('\n')[1:]:
        mp.append(list(map(int, line.split(' '))))
    parsed_maps.append(mp)


def map_seed(seeds, maps):
    
    for destination, source, range_length in maps:
        if seed >= source and seed < source + range_length:
            return seed + destination - source
    return seed


for s in part_two_seed:
    for m in parsed_maps:
        s = map_seed(s, m)
    min_seeds.append(s)

print(min(min_seeds))
