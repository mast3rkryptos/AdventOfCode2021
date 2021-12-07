def CountMove(count):
    total = 0
    if count % 2 == 0:
        # even
        total = (count / 2) * (count + 1)
    else:
        total = CountMove(count - 1) + count
    return total

def Part1(input):
    with open(input) as f:
        crabSubs = {}
        splitLine = f.readline().split(",")
        for token in splitLine:
            if int(token) in crabSubs.keys():
                crabSubs[int(token)] += 1
            else:
                crabSubs[int(token)] = 1
        fuelAmount = {}
        minPos = min(crabSubs.keys())
        maxPos = max(crabSubs.keys())
        for i in range(minPos, maxPos+1):
            fuelAmount[i] = 0
            for j in crabSubs.keys():
                fuelAmount[i] += abs(i - j) * crabSubs[j]
        print(f"Day 07, Part 1: {min(fuelAmount.values())}")



def Part2(input):
    with open(input) as f:
        crabSubs = {}
        splitLine = f.readline().split(",")
        for token in splitLine:
            if int(token) in crabSubs.keys():
                crabSubs[int(token)] += 1
            else:
                crabSubs[int(token)] = 1
        fuelAmount = {}
        minPos = min(crabSubs.keys())
        maxPos = max(crabSubs.keys())
        for i in range(minPos, maxPos + 1):
            fuelAmount[i] = 0
            for j in crabSubs.keys():
                fuelAmount[i] += CountMove(abs(i - j)) * crabSubs[j]
        print(f"Day 07, Part 2: {int(min(fuelAmount.values()))}")
