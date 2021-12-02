def Part1(input):
    horizonatalPos = 0
    depth = 0
    with open(input) as f:
        for line in f:
            splitLines = line.split(" ")
            if splitLines[0] == "forward":
                horizonatalPos += int(splitLines[1])
            elif splitLines[0] == "up":
                depth -= int(splitLines[1])
            elif splitLines[0] == "down":
                depth += int(splitLines[1])
    print(f"Day 02, Part 1: {horizonatalPos * depth}")


def Part2(input):
    horizonatalPos = 0
    depth = 0
    aim = 0
    with open(input) as f:
        for line in f:
            splitLines = line.split(" ")
            if splitLines[0] == "forward":
                horizonatalPos += int(splitLines[1])
                depth += int(splitLines[1]) * aim
            elif splitLines[0] == "up":
                aim -= int(splitLines[1])
            elif splitLines[0] == "down":
                aim += int(splitLines[1])
    print(f"Day 02, Part 2: {horizonatalPos * depth}")
