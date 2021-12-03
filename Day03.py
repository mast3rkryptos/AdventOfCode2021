def Part1(input):
    with open(input) as f:
        onesCount = []
        lineCount = 0
        for line in f:
            if len(onesCount) == 0:
                for i in range(len(line)-1):
                    onesCount.append(0)
            for i in range(len(line)):
                if line[i] == "1":
                    onesCount[i] += 1
            lineCount += 1
        gammaRate = 0
        flipPattern = 0
        for i in range(len(onesCount)):
            flipPattern += pow(2, len(onesCount) - i - 1)
            if onesCount[i] > lineCount / 2:
                gammaRate += pow(2, len(onesCount) - i - 1)
    print(f"Day 03, Part 1: {gammaRate * (gammaRate ^ flipPattern)}")


def Part2(input):
    with open(input) as f:
        lineCount = 0
        bitCount = 0
        masterValues = []
        for line in f:
            lineCount += 1
            bitCount = len(line)
            masterValues.append(int(line, 2))

        # Oxygen Generator
        onesCount = 0
        bitPosition = bitCount - 1
        ratingIndices = []
        for i in range(len(masterValues)):
            ratingIndices.append(i)
        while len(ratingIndices) > 1:
            # Count ones
            onesCount = 0
            for i in range(len(ratingIndices)):
                onesCount += 1 if (masterValues[ratingIndices[i]] >> bitPosition) & 0x1 == 1 else 0
            # Remove or keep ones
            keepOnes = onesCount >= len(ratingIndices) / 2
            ratingIndicesTemp = ratingIndices.copy()
            for i in range(len(ratingIndices)):
                if keepOnes and (masterValues[ratingIndices[i]] >> bitPosition) & 0x1 == 0 or not keepOnes and (masterValues[ratingIndices[i]] >> bitPosition) & 0x1 == 1:
                    ratingIndicesTemp[i] = None
            while None in ratingIndicesTemp:
                ratingIndicesTemp.remove(None)
            ratingIndices = ratingIndicesTemp
            bitPosition -= 1
        oxyRating = masterValues[ratingIndices[0]]

        # CO2 Scrubber
        onesCount = 0
        bitPosition = bitCount - 1
        ratingIndices = []
        for i in range(len(masterValues)):
            ratingIndices.append(i)
        while len(ratingIndices) > 1:
            # Count ones
            onesCount = 0
            for i in range(len(ratingIndices)):
                onesCount += 1 if (masterValues[ratingIndices[i]] >> bitPosition) & 0x1 == 1 else 0
            # Remove or keep ones
            keepOnes = onesCount < len(ratingIndices) / 2
            ratingIndicesTemp = ratingIndices.copy()
            for i in range(len(ratingIndices)):
                if keepOnes and (masterValues[ratingIndices[i]] >> bitPosition) & 0x1 == 0 or not keepOnes and (
                        masterValues[ratingIndices[i]] >> bitPosition) & 0x1 == 1:
                    ratingIndicesTemp[i] = None
            while None in ratingIndicesTemp:
                ratingIndicesTemp.remove(None)
            ratingIndices = ratingIndicesTemp
            bitPosition -= 1
        co2Rating = masterValues[ratingIndices[0]]

        print(f"Day 03, Part 2: {oxyRating * co2Rating}")
