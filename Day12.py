def FindPath(links, paths):
    for path in paths:
        if path[-1] == "end":
            continue
        else:
            for link in links[path[-1]]:
                if link.isupper() or (link.islower() and link not in path):
                    tempPath = path.copy()
                    paths.append(tempPath)
                    paths[-1].append(link)
                else:
                    continue

def Part1(input):
    links = {}
    paths = []
    with open(input) as f:
        for line in f:
            splitLine = line.strip('\n').split('-')
            if splitLine[0] in links.keys() and splitLine[0] != "end":
                links[splitLine[0]].append(splitLine[1])
            elif splitLine[0] != "end":
                links[splitLine[0]] = [splitLine[1]]
            if splitLine[1] in links.keys() and splitLine[1] != "end":
                links[splitLine[1]].append(splitLine[0])
            elif splitLine[1] != "end":
                links[splitLine[1]] = [splitLine[0]]

    paths.append(["start"])
    FindPath(links, paths)

    count = 0
    for path in paths:
        count += 1 if path[0] == "start" and path[-1] == "end" else 0

    print(f"Day 12, Part 01: {count}")


def LazyFunction(path):
    count = 0
    for s in path:
        count += 1 if s.islower() and list(path).count(s) > 1 else 0
    return count == 0


def FindPathP2(links, paths):
    fieldTripComplete = {}
    for path in paths:
        fieldTripComplete[str(path)] = False if str(path) not in fieldTripComplete else fieldTripComplete[str(path)]
        if path[-1] == "end":
            continue
        else:
            for link in links[path[-1]]:
                if link != "start" and (link.isupper()
                                        or (not fieldTripComplete[str(path)] and link.islower() and list(path).count(link) < 2)
                                        or (fieldTripComplete[str(path)] and link.islower() and link not in path)):
                    tempPath = path.copy()
                    paths.append(tempPath)
                    paths[-1].append(link)
                    fieldTripComplete[str(paths[-1])] = fieldTripComplete[str(path)] or link.islower() and list(paths[-1]).count(link) == 2
                else:
                    continue

def Part2(input):
    links = {}
    paths = []
    with open(input) as f:
        for line in f:
            splitLine = line.strip('\n').split('-')
            if splitLine[0] in links.keys() and splitLine[0] != "end":
                links[splitLine[0]].append(splitLine[1])
            elif splitLine[0] != "end":
                links[splitLine[0]] = [splitLine[1]]
            if splitLine[1] in links.keys() and splitLine[1] != "end":
                links[splitLine[1]].append(splitLine[0])
            elif splitLine[1] != "end":
                links[splitLine[1]] = [splitLine[0]]

    paths.append(["start"])
    FindPathP2(links, paths)

    count = 0
    for path in paths:
        count += 1 if path[0] == "start" and path[-1] == "end" else 0

    print(f"Day 12, Part 02: {count} <OPTIMIZE LATER>")
