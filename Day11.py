_1D_SIZE = 10


def Flash(grid, y, x, flashOccurred = False):
    retVal = 0
    if grid[y][x] > 9:
        grid[y][x] = -1
        retVal += 1
        for ty in range(y - 1, y + 2, 1):
            for tx in range(x - 1, x + 2, 1):
                if ty >= 0 and ty < len(grid) and tx >= 0 and tx < len(grid[0]):
                    retVal += Flash(grid, ty, tx, True)
    elif flashOccurred and grid[y][x] >= 0:
        grid[y][x] += 1
        retVal += Flash(grid, y, x)
    return retVal


def Part1(input):
    grid = []
    with open(input) as f:
        y = -1
        for line in f:
            y += 1
            grid.append([])
            for x in range(_1D_SIZE):
                grid[y].append(int(line[x]))

    count = 0
    for i in range(100):
        # Initial energy increase
        for y in range(_1D_SIZE):
            for x in range(_1D_SIZE):
                grid[y][x] += 1

        # Initial flash checks
        for y in range(_1D_SIZE):
            for x in range(_1D_SIZE):
                count += Flash(grid, y, x)

        # Post-flash reset
        for y in range(_1D_SIZE):
            for x in range(_1D_SIZE):
                grid[y][x] = 0 if grid[y][x] == -1 else grid[y][x]

    print(f"Day 11, Part 01: {count}")


def Part2(input):
    grid = []
    with open(input) as f:
        y = -1
        for line in f:
            y += 1
            grid.append([])
            for x in range(_1D_SIZE):
                grid[y].append(int(line[x]))

    count = 0
    keepLooking = True
    while keepLooking:
        count += 1

        # Initial energy increase
        for y in range(_1D_SIZE):
            for x in range(_1D_SIZE):
                grid[y][x] += 1

        # Initial flash checks
        for y in range(_1D_SIZE):
            for x in range(_1D_SIZE):
                Flash(grid, y, x)

        # Post-flash reset
        for y in range(_1D_SIZE):
            for x in range(_1D_SIZE):
                grid[y][x] = 0 if grid[y][x] == -1 else grid[y][x]

        # Check for simultaneous flash
        allZeroes = True
        for y in range(_1D_SIZE):
            for x in range(_1D_SIZE):
                allZeroes &= grid[y][x] == 0
        keepLooking = not allZeroes

    print(f"Day 11, Part 02: {count}")
