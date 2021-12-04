import re

def hasBingo(board):
    # check columns
    for i in range(5):
        if board[i] == "X" and board[i+5] == "X" and board[i+10] == "X" and board[i+15] == "X" and board[i+20] == "X":
            return True
    # check rows
    for i in range(0, 25, 5):
        if board[i] == "X" and board[i+1] == "X" and board[i+2] == "X" and board[i+3] == "X" and board[i+4] == "X":
            return True


def sumBoard(board):
    sum = 0
    for number in board:
        if number != "X":
            sum += int(number)
    return sum


def Part1(input):
    with open(input) as f:
        numbers = f.readline().strip('\n').split(",")
        boards = []
        line = f.readline() #skip first empty line
        line = f.readline()
        board = []
        while line != "":
            pattern = "\s*(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)"
            match = re.match(pattern, line)
            if match is not None:
                board.append(match[1])
                board.append(match[2])
                board.append(match[3])
                board.append(match[4])
                board.append(match[5])
            else:
                boards.append(board)
                board = []
            line = f.readline()
        boards.append(board)

    # Play bingo
    for number in numbers:
        for board in boards:
            if number in board:
                board[board.index(number)] = "X"
                if hasBingo(board):
                    print(f"Day 04, Part 1: {int(number) * sumBoard(board)}")
                    return

def Part2(input):
    with open(input) as f:
        numbers = f.readline().strip('\n').split(",")
        boards = []
        line = f.readline()  # skip first empty line
        line = f.readline()
        board = []
        while line != "":
            pattern = "\s*(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)"
            match = re.match(pattern, line)
            if match is not None:
                board.append(match[1])
                board.append(match[2])
                board.append(match[3])
                board.append(match[4])
                board.append(match[5])
            else:
                boards.append(board)
                board = []
            line = f.readline()
        boards.append(board)

    # Play bingo
    bingoOrder = []
    for number in numbers:
        for board in boards:
            if number in board:
                board[board.index(number)] = "X"
                if hasBingo(board) and boards.index(board) not in bingoOrder:
                    bingoOrder.append(boards.index(board))
                    if len(bingoOrder) == len(boards):
                        print(f"Day 04, Part 2: {int(number) * sumBoard(board)}")
                        return
