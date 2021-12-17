import math


def Part1(input):
    grid = []
    with open(input) as f:
        for line in f:
            grid.append([])
            for c in line.strip('\n'):
                grid[-1].append(int(c))

    # nodes: [(x, y)] : (visited, distance)
    nodes = {}
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            nodes[(x, y)] = (False, math.inf)
    nodes[(0, 0)] = (False, 0)

    y = 0
    x = 0
    while not nodes[(len(grid[0]) - 1, len(grid) - 1)][0]:
        for ty in range(y - 1, y + 2, 1):
            for tx in range(x - 1, x + 2, 1):
                # Adding abs() to limit to cardinal movement only
                if ty >= 0 and ty < len(grid) and tx >= 0 and tx < len(grid[0]) and (abs(x - tx) + abs(y - ty) == 1) and not nodes[(tx, ty)][0]:
                    nodes[(tx, ty)] = (False, nodes[(x, y)][1] + grid[ty][tx] if nodes[(x, y)][1] + grid[ty][tx] < nodes[(tx, ty)][1] else nodes[(tx, ty)][1])
                else:
                    continue
        nodes[(x, y)] = (True, nodes[(x, y)][1])
        minVal = math.inf
        nextX = 0
        nextY = 0
        for ty in range(len(grid)):
            for tx in range(len(grid[0])):
                if ty >= 0 and ty < len(grid) and tx >= 0 and tx < len(grid[0]) and not nodes[(tx, ty)][0] and nodes[(tx, ty)][1] < minVal:
                    minVal = nodes[(tx, ty)][1]
                    nextX = tx
                    nextY = ty
                else:
                    continue
        x = nextX
        y = nextY

    print(f"Day 15, Part 1: {nodes[(len(grid[0]) - 1, len(grid) - 1)][1]} <OPTIMIZE LATER>")


def Part2(input):
    grid = []
    with open(input) as f:
        for line in f:
            grid.append([])
            for i in range(5):
                for c in line.strip('\n'):
                    grid[-1].append(int(c) + i if int(c) + i < 10 else (int(c) + i) % 10 + 1)
    tempGrid = []
    for i in range(5):
        for y in range(len(grid)):
            tempGrid.append([])
            for x in range(len(grid[0])):
                tempGrid[-1].append(grid[y][x] + i if grid[y][x] + i < 10 else (grid[y][x] + i) % 10 + 1)
    grid = tempGrid.copy()

    # nodes: [(x, y)] : (visited, distance)
    nodes = {}
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            nodes[(x, y)] = (False, math.inf)
    nodes[(0, 0)] = (False, 0)

    y = 0
    x = 0
    unvisitedSeenNodes = {}
    while not nodes[(len(grid[0]) - 1, len(grid) - 1)][0]:
        for ty in range(y - 1, y + 2, 1):
            for tx in range(x - 1, x + 2, 1):
                # Adding abs() to limit to cardinal movement only
                if ty >= 0 and ty < len(grid) and tx >= 0 and tx < len(grid[0]) and (abs(x - tx) + abs(y - ty) == 1) and not nodes[(tx, ty)][0]:
                    nodes[(tx, ty)] = (False, nodes[(x, y)][1] + grid[ty][tx] if nodes[(x, y)][1] + grid[ty][tx] < nodes[(tx, ty)][1] else nodes[(tx, ty)][1])
                    unvisitedSeenNodes[(tx, ty)] = nodes[(tx, ty)]
                else:
                    continue
        nodes[(x, y)] = (True, nodes[(x, y)][1])
        if x == len(grid[0]) - 1 and y == len(grid) - 1:
            continue
        minVal = math.inf
        #nextX = 0
        #nextY = 0
        next = ()
        #for ty in range(len(grid)):
            #for tx in range(len(grid[0])):
        for key in unvisitedSeenNodes.keys():
            if unvisitedSeenNodes[key][1] < minVal:
                minVal = unvisitedSeenNodes[key][1]
                #nextX = tx
                #nextY = ty
                next = key
            else:
                continue
        unvisitedSeenNodes.pop(next)
        x = next[0]
        y = next[1]

    print(f"Day 15, Part 2: {nodes[(len(grid[0]) - 1, len(grid) - 1)][1]} <OPTIMIZE LATER>")
