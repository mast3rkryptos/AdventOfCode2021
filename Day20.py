import copy

def GetIndex(image, x, y, infiniteSpaceValue):
    index = 0
    for ty in range(y - 1, y + 2, 1):
        for tx in range(x - 1, x + 2, 1):
            if 0 <= ty < len(image) and 0 <= tx < len(image[0]):
                index = (index << 1) + image[ty][tx]
            else:
                index = (index << 1) + infiniteSpaceValue
    return index


def PrintImage(image):
    for y in range(len(image)):
        line = ""
        for x in range(len(image[0])):
            line += "#" if image[y][x] == 1 else "."
        print(line)


def Part1(input):
    algorithm = []
    whitePixels = []
    x = 0
    y = 0
    with open(input) as f:
        for line in f:
            if len(algorithm) == 0:
                for c in line.strip('\n'):
                    algorithm.append(1 if c == "#" else 0)
            elif line == "\n":
                continue
            else:
                for x in range(len(line)):
                    if line[x] == "#":
                        whitePixels.append((x, y))
                y += 1

    image = [[0 for tx in range(x + 5)] for ty in range(y + 4)]
    transformedImage = copy.deepcopy(image)
    for whitePixel in whitePixels:
        image[whitePixel[1] + 2][whitePixel[0] + 2] = 1
    #print("Image:")
    #PrintImage(image)

    infiniteSpaceValue = 0
    for i in range(2):
        for ty in range(len(image)):
            for tx in range(len(image[0])):
                transformedImage[ty][tx] = algorithm[GetIndex(image, tx, ty, infiniteSpaceValue)]
        #print("Transformed Image:")
        #PrintImage(transformedImage)

        # Reset for next iteration
        infiniteSpaceValue = (infiniteSpaceValue + 1) % 2 if algorithm[0] != 0 else 0
        image = [[infiniteSpaceValue for tx in range(len(transformedImage[0]) + 4)] for ty in range(len(transformedImage) + 4)]
        for ty in range(len(transformedImage)):
            for tx in range(len(transformedImage[0])):
                image[ty + 2][tx + 2] = transformedImage[ty][tx]
        transformedImage = [[infiniteSpaceValue for tx in range(len(image[0]))] for ty in range(len(image))]

    count  = 0
    for ty in range(len(image)):
        for tx in range(len(image[0])):
            count += image[ty][tx]

    print(f"Day 20, Part 1: {count}")
    # 6225 is too high
    # 6013 is too high


def Part2(input):
    algorithm = []
    whitePixels = []
    x = 0
    y = 0
    with open(input) as f:
        for line in f:
            if len(algorithm) == 0:
                for c in line.strip('\n'):
                    algorithm.append(1 if c == "#" else 0)
            elif line == "\n":
                continue
            else:
                for x in range(len(line)):
                    if line[x] == "#":
                        whitePixels.append((x, y))
                y += 1

    image = [[0 for tx in range(x + 5)] for ty in range(y + 4)]
    transformedImage = copy.deepcopy(image)
    for whitePixel in whitePixels:
        image[whitePixel[1] + 2][whitePixel[0] + 2] = 1
    #print("Image:")
    #PrintImage(image)

    infiniteSpaceValue = 0
    for i in range(50):
        for ty in range(len(image)):
            for tx in range(len(image[0])):
                transformedImage[ty][tx] = algorithm[GetIndex(image, tx, ty, infiniteSpaceValue)]
        #print("Transformed Image:")
        #PrintImage(transformedImage)

        # Reset for next iteration
        infiniteSpaceValue = (infiniteSpaceValue + 1) % 2 if algorithm[0] != 0 else 0
        image = [[infiniteSpaceValue for tx in range(len(transformedImage[0]) + 4)] for ty in
                 range(len(transformedImage) + 4)]
        for ty in range(len(transformedImage)):
            for tx in range(len(transformedImage[0])):
                image[ty + 2][tx + 2] = transformedImage[ty][tx]
        transformedImage = [[infiniteSpaceValue for tx in range(len(image[0]))] for ty in range(len(image))]

    count = 0
    for ty in range(len(image)):
        for tx in range(len(image[0])):
            count += image[ty][tx]

    print(f"Day 20, Part 2: {count}")
