def Part1(input):
    dots = []
    maxX = 0
    maxY = 0
    with open(input) as f:
        folding = False
        for line in f:
            if line == "\n":
                folding = True
                continue
            if not folding:
                maxX = int(line.split(',')[0]) if int(line.split(',')[0]) > maxX else maxX
                maxY = int(line.split(',')[1].strip('\n')) if int(line.split(',')[1].strip('\n')) > maxX else maxY
                dots.append((int(line.split(',')[0]), int(line.split(',')[1].strip('\n'))))
            else:
                location = int(line.split(' ')[2].split('=')[1].strip('\n'))
                direction = line.split(' ')[2].split('=')[0]
                tempDots = []
                if direction == 'y':
                    for dot in dots:
                        if dot[1] > location:
                            tempDots.append((dot[0], location - (dot[1] - location))) if (dot[0], location - (dot[1] - location)) not in tempDots else None
                        else:
                            tempDots.append((dot[0], dot[1])) if (dot[0], dot[1]) not in tempDots else None
                elif direction == 'x':
                    for dot in dots:
                        if dot[0] > location:
                            tempDots.append((location - (dot[0] - location), dot[1])) if (location - (dot[0] - location), dot[1]) not in tempDots else None
                        else:
                            tempDots.append((dot[0], dot[1])) if (dot[0], dot[1]) not in tempDots else None
                dots = tempDots.copy()
                break

    print(f"Day 13, Part 1: {len(dots)}")


def Part2(input):
    dots = []
    maxX = 0
    maxY = 0
    with open(input) as f:
        folding = False
        for line in f:
            if line == "\n":
                folding = True
                continue
            if not folding:
                maxX = int(line.split(',')[0]) if int(line.split(',')[0]) > maxX else maxX
                maxY = int(line.split(',')[1].strip('\n')) if int(line.split(',')[1].strip('\n')) > maxX else maxY
                dots.append((int(line.split(',')[0]), int(line.split(',')[1].strip('\n'))))
            else:
                location = int(line.split(' ')[2].split('=')[1].strip('\n'))
                direction = line.split(' ')[2].split('=')[0]
                tempDots = []
                if direction == 'y':
                    for dot in dots:
                        if dot[1] > location:
                            tempDots.append((dot[0], location - (dot[1] - location))) if (dot[0], location - (dot[1] - location)) not in tempDots else None
                        else:
                            tempDots.append((dot[0], dot[1])) if (dot[0], dot[1]) not in tempDots else None
                elif direction == 'x':
                    for dot in dots:
                        if dot[0] > location:
                            tempDots.append((location - (dot[0] - location), dot[1])) if (location - (dot[0] - location), dot[1]) not in tempDots else None
                        else:
                            tempDots.append((dot[0], dot[1])) if (dot[0], dot[1]) not in tempDots else None
                dots = tempDots.copy()

    print("Day 13, Part 2: ")
    maxX = 0
    maxY = 0
    for dot in dots:
        maxX = dot[0] if dot[0] > maxX else maxX
        maxY = dot[1] if dot[1] > maxY else maxY
    for y in range(maxY + 1):
        line = "   "
        for x in range(maxX + 1):
            line += "#" if (x, y) in dots else " "
        print(line)
