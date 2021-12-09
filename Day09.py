def IsLowPoint(map, x, y):
    adjacentValues = []
    if x == 0 and y == 0:
        return map[y][x] < map[y + 1][x] and map[y][x] < map[y][x + 1]
    elif x == len(map[0]) - 1 and y == len(map) - 1:
        return map[y][x] < map[y - 1][x] and map[y][x] < map[y][x - 1]
    if x == 0 and y == len(map) - 1:
        return map[y][x] < map[y - 1][x] and map[y][x] < map[y][x + 1]
    elif x == len(map[0]) - 1 and y == 0:
        return map[y][x] < map[y + 1][x] and map[y][x] < map[y][x - 1]
    elif x == 0:
        return map[y][x] < map[y + 1][x] and map[y][x] < map[y][x + 1] and map[y][x] < map[y - 1][x]
    elif x == len(map[0]) - 1:
        return map[y][x] < map[y + 1][x] and map[y][x] < map[y][x - 1] and map[y][x] < map[y - 1][x]
    elif y == 0:
        return map[y][x] < map[y + 1][x] and map[y][x] < map[y][x + 1] and map[y][x] < map[y][x - 1]
    elif y == len(map) - 1:
        return map[y][x] < map[y - 1][x] and map[y][x] < map[y][x + 1] and map[y][x] < map[y][x - 1]
    else:
        return map[y][x] < map[y + 1][x] and map[y][x] < map[y][x + 1] and map[y][x] < map[y - 1][x] and map[y][x] < map[y][x - 1]

def Part1(input):
    map = []
    sum = 0
    with open(input) as f:
        for line in f:
            map.append([])
            for c in line.strip('\n'):
                map[-1].append(int(c))
    for x in range(len(map[0])):
        for y in range(len(map)):
            if IsLowPoint(map, x, y):
                sum += 1 + map[y][x]
    print(f"Day 09, Part 1: {sum}")

def CountBasin(map, y, x):
    size = 1
    if y == -1 or x == -1 or y == len(map) or x == len(map[0]):
        return 0
    elif map[y][x] == -1 or map[y][x] == 9:
        return 0
    else:
        map[y][x] = -1
        size += CountBasin(map, y + 1, x)
        size += CountBasin(map, y - 1, x)
        size += CountBasin(map, y, x + 1)
        size += CountBasin(map, y, x - 1)
        return size

def Part2(input):
    map = []
    answer = 1
    with open(input) as f:
        for line in f:
            map.append([])
            for c in line.strip('\n'):
                map[-1].append(int(c))
    basins = []
    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] == -1 or map[y][x] == 9:
                continue
            else:
                basins.append(CountBasin(map, y, x))
    basins.sort()
    print(f"Day 09, Part 2: {basins[-1] * basins[-2] * basins[-3]} ")
