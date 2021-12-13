_1D_SIZE = 5


def Flash(grid, y, x):
    retVal = 0
    if grid[y][x] >= 9:
        grid[y][x] = -1
        retVal += 1
        for ty in range(y - 1, y + 2, 1):
            for tx in range(x - 1, x + 2, 1):
                if ty >= 0 and ty < len(grid) and tx >= 0 and tx < len(grid[0]):
                    retVal += Flash(grid, ty, tx)
    elif grid[y][x] >= 0:
        grid[y][x] += 1
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

    print(f"Before any steps:")
    for y in range(_1D_SIZE):
        print(grid[y])
    print()
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

        # Print out grid
        print(f"After step {i + 1}:")
        for y in range(_1D_SIZE):
                print(grid[y])
        print()

    print(f"Day 11, Part 01: {count}")


def Part2(input):
    return None
