import re


def Part1(input):
    with open(input) as f:
        line = f.readline()
        pattern = "target area: x=(\-*\d+)..(\-*\d+), y=(\-*\d+)\.\.(\-*\d+)"
        match = re.match(pattern, line)
        if match is not None:
            start = (0, 0)
            targetMinimum = (int(match[1]), int(match[3]))
            targetMaximum = (int(match[2]), int(match[4]))

            # Figure out potential initial-x-vectors
            vectorsX = []
            for i in range(targetMaximum[0] + 1):
                velocityX = i
                positionX = 0
                stepCount = 0
                while velocityX != -1:
                    stepCount += 1
                    positionX += velocityX
                    velocityX -= 1
                    if targetMinimum[0] <= positionX <= targetMaximum[0]:
                        vectorsX.append((i, stepCount))
            #maxXSteps = 0
            #for vector in vectorsX:
            #    maxXSteps = vector[1] if vector[1] > maxXSteps else maxXSteps


            # Figure potential initial y-vectors
            #vectorsY = []
            #for i in range(-1000, 1000, 1):
            #    velocityY = i
            #    positionY = 0
            #    stepCount = 0
            #    while not (targetMinimum[1] <= positionY <= targetMaximum[1]) and stepCount <= maxXSteps:
            #        stepCount += 1
            #        positionY += velocityY
            #        velocityY -= 1
            #    if targetMinimum[1] <= positionY <= targetMaximum[1]:
            #        vectorsY.append((i, stepCount))

            # Find max y position
            maxYPosition = 0
            vectors = []
            for vectorX in vectorsX:
                for i in range(-1000, 1000, 1):
                    tempMaxYPosition = 0
                    velocityX = vectorX[0]
                    velocityY = i
                    positionX = 0
                    positionY = 0
                    stepCount = 0
                    while not (targetMinimum[0] <= positionX <= targetMaximum[0] and targetMinimum[1] <= positionY <= targetMaximum[1]) and not (velocityX == 0 and positionY < targetMinimum[1]):
                        stepCount += 1
                        positionX += velocityX
                        positionY += velocityY
                        tempMaxYPosition = positionY if positionY > tempMaxYPosition else tempMaxYPosition
                        velocityX -= 1 if velocityX > 0 else 0
                        velocityY -= 1
                    if targetMinimum[0] <= positionX <= targetMaximum[0] and targetMinimum[1] <= positionY <= targetMaximum[1]:
                        vectors.append((vectorX[0], i)) if (vectorX[0], i) not in vectors else None
                        maxYPosition = tempMaxYPosition if tempMaxYPosition > maxYPosition else maxYPosition

            print(f"Day 17, Part 1&2: {maxYPosition} {len(vectors)}")


def Part2(input):
    return None
