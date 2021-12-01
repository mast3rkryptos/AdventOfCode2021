def Part1(input):
    with open(input, "r") as f:
        increaseCount = 0
        previous = int(f.readline())
        for line in f:
            increaseCount += 1 if int(line) > previous else 0
            previous = int(line)
    print(f"Day 01, Part 1: {increaseCount}")


def pushQueue(queue, value):
    queue[2] = queue[1]
    queue[1] = queue[0]
    queue[0] = value


def sumQueue(queue):
    return queue[0] + queue[1] + queue[2]


def Part2(input):
    with open(input, "r") as f:
        increaseCount = 0
        previous = [-1, -1, -1]
        current = [-1, -1, -1]
        for line in f:
            if previous[2] == -1:
                pushQueue(previous, int(line))
                pushQueue(current, int(line))
                continue
            else:
                pushQueue(current, int(line))
                increaseCount += 1 if sumQueue(current) > sumQueue(previous) else 0
                pushQueue(previous, int(line))
        print(f"Day 01, Part 2: {increaseCount}")
