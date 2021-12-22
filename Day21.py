import copy
from timer import Timer


dieRoll = 0
rollCount = 0
def Roll():
    global dieRoll
    global rollCount
    dieRoll = (dieRoll % 100) + 1
    rollCount += 1
    return dieRoll


def Part1(input):
    positions = []
    with open(input) as f:
        for line in f:
            positions.append(int(line.split(" ")[-1]))

    players = [0 for i in positions]
    winner = False
    while not winner:
        for i in range(len(players)):
            roll = 0
            for j in range(3):
                roll += Roll()
            positions[i] = ((positions[i] + roll - 1) % 10) + 1
            #positions[i] = (positions[i] + roll) % 10 if positions[i] + roll >= 10 else positions[i] + roll
            players[i] += positions[i]
            if players[i] >= 1000:
                winner = True
                break

    print(f"Day 21, Part 1: {min(players) * rollCount}")


def NukaQuantum(playerPositions, playersScores, activePlayer, totalRoll = 0, winThreshold = 21):
    if totalRoll != 0:
        playerPositions[activePlayer] = ((playerPositions[activePlayer] + totalRoll - 1) % 10) + 1
        playersScores[activePlayer] += playerPositions[activePlayer]
        if playersScores[activePlayer] >= winThreshold:
            return (1, 0) if activePlayer == 0 else (0, 1)

    winRecord = (0, 0)
    for roll1 in range(1, 4, 1):
        for roll2 in range(1, 4, 1):
            for roll3 in range(1, 4, 1):
                uniquePlayerPositions = copy.deepcopy(playerPositions)
                uniquePlayerScores = copy.deepcopy(playersScores)
                winRecord = tuple(map(lambda i, j: i + j, winRecord, NukaQuantum(uniquePlayerPositions, uniquePlayerScores, (activePlayer + 1) % 2, roll1 + roll2 + roll3, winThreshold)))
    return winRecord


def NukaQuantum(player1Position, player2Position, player1Score, player2Score, activePlayer, totalRoll = 0, winThreshold = 21):
    if totalRoll != 0:
        if activePlayer == 0:
            player1Position = ((player1Position + totalRoll - 1) % 10) + 1
            player1Score += player1Position
            if player1Score >= winThreshold:
                return 1, 0
        elif activePlayer == 1:
            player2Position = ((player2Position + totalRoll - 1) % 10) + 1
            player2Score += player2Position
            if player2Score >= winThreshold:
                return 0, 1

    winRecord = (0, 0)
    for roll1 in range(1, 4, 1):
        for roll2 in range(1, 4, 1):
            for roll3 in range(1, 4, 1):
                winRecord = tuple(map(lambda i, j: i + j, winRecord, NukaQuantum(player1Position, player2Position, player1Score, player2Score, (activePlayer + 1) % 2, roll1 + roll2 + roll3, winThreshold)))
    return winRecord


def Part2(input):
    positions = []
    with open(input) as f:
        for line in f:
            positions.append(int(line.split(" ")[-1]))
    for i in range(5, 15, 1):
        timer = Timer()
        timer.Start()
        #print(f"Day 21, Part 2: {NukaQuantum([4, 8], [0, 0], 1, winThreshold=i)}")  # Active player of 1 (which means 2) to force Player 1 to take the first turn
        print(f"Day 21, Part 2: {NukaQuantum(4, 8, 0, 0, 1, winThreshold=i)}")  # Active player of 1 (which means 2) to force Player 1 to take the first turn
        print(f"Execution Time: {timer.Stop()}")
