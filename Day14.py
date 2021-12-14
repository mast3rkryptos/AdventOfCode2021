import re


def Part1(input):
    with open(input) as f:
        polymer = f.readline().strip('\n')
        rules = {}
        for line in f:
            pattern = "(\w\w) -> (\w)"
            match = re.match(pattern, line)
            if match is not None:
                rules[match[1]] = match[2]

    tempPolymer = polymer
    for i in range(10):
        j = 0
        while j < len(polymer) - 1:
            polymer = polymer[0:j+1] + rules[polymer[j:j+2]] + polymer[j+1:len(polymer)]
            j += 2

    lce = -1
    mce = 0
    for c in range(ord('A'), ord('Z')+1):
        if lce == -1 and chr(c) in polymer:
            lce = polymer.count(chr(c))
        lce = polymer.count(chr(c)) if polymer.count(chr(c)) < lce and chr(c) in polymer else lce
        mce = polymer.count(chr(c)) if polymer.count(chr(c)) > mce else mce

    print(f"Day 14, Part 01: {mce - lce}")

def Part2(input):
    pairCounts = {}
    with open(input) as f:
        polymer = f.readline().strip('\n')
        rules = {}
        for line in f:
            pattern = "(\w\w) -> (\w)"
            match = re.match(pattern, line)
            if match is not None:
                rules[match[1]] = match[2]
                pairCounts[match[1]] = 0

    # Set initial counts
    for j in range(len(polymer) - 1):
        pairCounts[polymer[j:j+2]] += 1

    for i in range(40):
        tempPairCounts = pairCounts.copy()
        for pair in pairCounts.keys():
            count = pairCounts[pair]
            tempPairCounts[pair[0] + rules[pair]] += count
            tempPairCounts[rules[pair] + pair[1]] += count
            tempPairCounts[pair] -= count
            pairCounts[pair] = 0
            #print(count, pair[0] + rules[pair], rules[pair] + pair[1], pair, pairCounts, tempPairCounts)
        pairCounts = tempPairCounts.copy()
        #print(i + 1, pairCounts)

    counts = {}
    for c in range(ord('A'), ord('Z')+1):
        counts[chr(c)] = 0 if chr(c) != polymer[0] and chr(c) != polymer[-1] else 1 #everything except the first and last polymer character are double-counted, adjust accordingly
        for pair in pairCounts.keys():
            counts[chr(c)] += (pairCounts[pair] * pair.count(chr(c))) if (chr(c)) in pair else 0
    minVal = max(counts.values())
    for value in counts.values():
        minVal = value if value < minVal and value != 0 else minVal
    print(f"Day 14, Part 02: {int((max(counts.values()) - minVal) / 2)}")
