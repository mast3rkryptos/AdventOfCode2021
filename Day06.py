

def advanceDay(school):
    newFishCount = 0
    for i in range(len(school)):
        if school[i] == 0:
            school[i] = 6
            newFishCount += 1
        else:
            school[i] -= 1
    for i in range(newFishCount):
        school.append(8)


def Part1(input):
    school = []
    with open(input) as f:
        splitLine = f.readline().split(",")
        for fish in splitLine:
            school.append(int(fish))
    for i in range(80):
        advanceDay(school)
    print(f"Day 06, Part 1: {len(school)}")


def advanceDayPart2(school):
    zeroDayFishCount = school[0]
    for i in range(len(school) - 1):
        school[i] = school[i + 1]
    school[6] += zeroDayFishCount
    school[8] = zeroDayFishCount


def Part2(input):
    school = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    with open(input) as f:
        splitLine = f.readline().split(",")
        for fish in splitLine:
            school[int(fish)] += 1
    for i in range(256):
        advanceDayPart2(school)
    sum = 0
    for value in school:
        sum += value
    print(f"Day 06, Part 2: {sum}")
