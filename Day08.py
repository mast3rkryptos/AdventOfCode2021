import re

def Part1(input):
    digits = ["", "", "", "", "", "", "", "", "", ""]
    count = 0
    with open(input) as f:
        pattern = "(\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) \| (\w+) (\w+) (\w+) (\w+)"
        for line in f:
            match = re.match(pattern, line)
            if match is not None:
                for i in range(11, 15):
                    if len(match[i]) == 2 or len(match[i]) == 4 or len(match[i]) == 3 or len(match[i]) == 7:
                        count += 1
    print(f"Day 08, Part 1: {count}")


def Part2(input):
    digits = ["", "", "", "", "", "", "", "", "", ""]
    sum = 0
    with open(input) as f:
        pattern = "(\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) \| (\w+) (\w+) (\w+) (\w+)"
        for line in f:
            digits = ["", "", "", "", "", "", "", "", "", ""]
            match = re.match(pattern, line)
            if match is not None:
                # Uniques
                for i in range(1, 11):
                    if len(match[i]) == 2:
                        digits[1] = match[i]
                    elif len(match[i]) == 4:
                        digits[4] = match[i]
                    elif len(match[i]) == 3:
                        digits[7] = match[i]
                    elif len(match[i]) == 7:
                        digits[8] = match[i]
                # Non-uniques (excluding 5 and 2)
                for i in range(1, 11):
                    if len(match[i]) == 5 and (digits[7][0] in match[i] and digits[7][1] in match[i] and digits[7][2] in match[i]):
                        digits[3] = match[i]
                    elif len(match[i]) == 6 and not (digits[1][0] in match[i] and digits[1][1] in match[i]):
                        digits[6] = match[i]
                    elif len(match[i]) == 6 and (digits[4][0] in match[i] and digits[4][1] in match[i] and digits[4][2] in match[i] and digits[4][3] in match[i]):
                        digits[9] = match[i]
                    elif len(match[i]) == 6:
                        digits[0] = match[i]
                for i in range(1, 11):
                    if len(match[i]) == 5 and (match[i][0] in digits[6] and match[i][1] in digits[6] and match[i][2] in digits[6] and match[i][3] in digits[6] and match[i][4] in digits[6]):
                        digits[5] = match[i]
                    elif match[i] not in digits:
                        digits[2] = match[i]
                tempSum = 0
                for i in range(11, 15):
                    for digit in digits:
                        if sorted(match[i]) == sorted(digit):
                            tempSum += digits.index(digit) * pow(10, abs(i - 14))
                sum += tempSum
    print(f"Day 08, Part 2: {sum}")
