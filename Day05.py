import re


def recordPoint(points, x, y):
    if (x, y) not in points.keys():
        points[(x, y)] = 1
    else:
        points[(x, y)] += 1


def Part1(input):
    pattern = "(\d+),(\d+) -> (\d+),(\d+)"
    points = {}
    with open(input) as f:
        for line in f:
            match = re.match(pattern, line)
            if match is not None and (match[1] == match[3] or match[2] == match[4]):
                x = int(match[1])
                y = int(match[2])
                # Initial point
                recordPoint(points, x, y)
                # Horizontal line
                while x < int(match[3]):
                    x += 1
                    recordPoint(points, x, y)
                while x > int(match[3]):
                    x -= 1
                    recordPoint(points, x, y)
                # Vertical line
                while y < int(match[4]):
                    y += 1
                    recordPoint(points, x, y)
                while y > int(match[4]):
                    y -= 1
                    recordPoint(points, x, y)
                # Final point covered by while loops
    count = 0
    for point in points:
        if points[point] > 1:
            count += 1
    print(f"Day 05, Part 1: {count}")


def Part2(input):
    pattern = "(\d+),(\d+) -> (\d+),(\d+)"
    points = {}
    with open(input) as f:
        for line in f:
            match = re.match(pattern, line)
            if match is not None and (match[1] == match[3] or match[2] == match[4]):
                x = int(match[1])
                y = int(match[2])
                # Initial point
                recordPoint(points, x, y)
                # Horizontal line
                while x < int(match[3]):
                    x += 1
                    recordPoint(points, x, y)
                while x > int(match[3]):
                    x -= 1
                    recordPoint(points, x, y)
                # Vertical line
                while y < int(match[4]):
                    y += 1
                    recordPoint(points, x, y)
                while y > int(match[4]):
                    y -= 1
                    recordPoint(points, x, y)
                # Final point covered by while loops
            elif match is not None:
                x = int(match[1])
                y = int(match[2])
                # Initial point
                recordPoint(points, x, y)
                # NE line
                while x < int(match[3]) and y < int(match[4]):
                    x += 1
                    y += 1
                    recordPoint(points, x, y)
                # SE line
                while x < int(match[3]) and y > int(match[4]):
                    x += 1
                    y -= 1
                    recordPoint(points, x, y)
                # SW line
                while x > int(match[3]) and y > int(match[4]):
                    x -= 1
                    y -= 1
                    recordPoint(points, x, y)
                # NW line
                while x > int(match[3]) and y < int(match[4]):
                    x -= 1
                    y += 1
                    recordPoint(points, x, y)
                 # Final point covered by while loops
    count = 0
    for point in points:
        if points[point] > 1:
            count += 1
    print(f"Day 05, Part 2: {count}")
