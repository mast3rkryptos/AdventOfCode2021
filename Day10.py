import math


def Part1(input):
    stack = []
    points = {')':3, ']':57, '}':1197, '>':25137}
    score = 0
    with open(input) as f:
        for line in f:
            for c in line:
                if c == '\n':
                    continue
                else:
                    if c == '(' or c == '[' or c == '{' or c == '<':
                        stack.append(c)
                    elif (c == ')' and stack[-1] == '(') or \
                         (c == ']' and stack[-1] == '[') or \
                         (c == '}' and stack[-1] == '{') or \
                         (c == '>' and stack[-1] == '<'):
                        stack.pop(-1)
                    else:
                        score += points[c]
                        break
    print(f"Day 10, Part 1: {score}")

def Part2(input):
    points = {'(':1, '[':2, '{':3, '<':4}
    scores = []
    with open(input) as f:
        for line in f:
            stack = []
            score = 0
            corrupted = False
            line = line.strip('\n')
            for c in line:
                if c == '(' or c == '[' or c == '{' or c == '<':
                    stack.append(c)
                elif (c == ')' and stack[-1] == '(') or \
                     (c == ']' and stack[-1] == '[') or \
                     (c == '}' and stack[-1] == '{') or \
                     (c == '>' and stack[-1] == '<'):
                    stack.pop(-1)
                else:
                    corrupted = True
                    break
            if corrupted:
                continue
            while len(stack) != 0:
                score = (score * 5) + points[stack.pop(-1)]
            scores.append(score)
    scores.sort()
    print(f"Day 10, Part 2: {scores[math.trunc(len(scores) / 2)]}")
