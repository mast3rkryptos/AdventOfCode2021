def expand(hexString):
    binString = ""
    for c in hexString:
        binString += bin(int(c, base=16))[2:].zfill(4)
    return binString


def DoOperation(packetType, operands):
    retVal = -1
    if packetType == 0:
        retVal = sum(operands)
    elif packetType == 1:
        retVal = 1
        for operand in operands:
            retVal *= operand
    elif packetType == 2:
        retVal = min(operands)
    elif packetType == 3:
        retVal = max(operands)
    elif packetType == 5 and len(operands) == 2:
        retVal = 1 if operands[0] > operands[1] else 0
    elif packetType == 6 and len(operands) == 2:
        retVal = 1 if operands[0] < operands[1] else 0
    elif packetType == 7 and len(operands) == 2:
        retVal = 1 if operands[0] == operands[1] else 0
    else:
        print("Invalid operator/operands combination, exit")
        exit()
    return retVal


def ParsePacket(packet):
    # (versionSum, packetLength, result)
    retVal = (0, 0, 0)
    if not ('1' not in packet and packet != "0000000000000000000000") and packet != "":
        packetVersion = int(packet[0:3], base=2)
        packetType = int(packet[3:6], base=2)
        if packetType == 4:
            tempVal = ParseLiteralValue(packet[6:])
            retVal = (packetVersion, 6 + tempVal[0], tempVal[1])
        else:
            tempVal = ParseOperator(packet[6:], packetType)
            retVal = (packetVersion + tempVal[0], 6 + tempVal[1], tempVal[2])
    return retVal


def ParseLiteralValue(packet):
    i = 0
    value = 0
    while True:
        temp = packet[i + 1:i + 5]
        value = (value << 4) + int(packet[i + 1:i + 5], base=2)
        if packet[i] == '0':
            i += 5
            break
        else:
            i += 5
    return i, value


def ParseOperator(packet, packetType):
    retVal = (0, 0, 0)
    operands = []
    if packet[0] == '0':
        retVal = (0, 16, 0)
        length = int(packet[1:16], base=2)
        offset = 16
        while (offset - 16) < length:
            tempVal = ParsePacket(packet[offset:])
            offset += tempVal[1]
            operands.append(tempVal[2])
            retVal = (retVal[0] + tempVal[0], retVal[1] + tempVal[1], 0)
        retVal = (retVal[0], retVal[1], DoOperation(packetType, operands))
    else:
        retVal = (0, 12)
        count = int(packet[1:12], base=2)
        offset = 12
        for i in range(count):
            tempVal = ParsePacket(packet[offset:])
            offset += tempVal[1]
            operands.append(tempVal[2])
            retVal = (retVal[0] + tempVal[0], retVal[1] + tempVal[1], 0)
        retVal = (retVal[0], retVal[1], DoOperation(packetType, operands))
    return retVal



def Part1(input):
    with open(input) as f:
        for line in f:
            binData = expand(line.strip('\n'))
            versionSum = ParsePacket(binData)[0]
            print(f"Day 16, Part 1: {versionSum}")


def Part2(input):
    with open(input) as f:
        for line in f:
            binData = expand(line.strip('\n'))
            result = ParsePacket(binData)[2]
            print(f"Day 16, Part 2: {result}")
