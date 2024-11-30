readFile = open('./input.txt', 'r')
result = 0

strategyDraw = {
    'A': 'X',
    'B': 'Y',
    'C': 'Z'
}

strategyWin = {
    'A': 'Y',
    'B': 'Z',
    'C': 'X'
}

strategyLose = {
    'A': 'Z',
    'B': 'X',
    'C': 'Y'
}

point = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

x = 0
for line in readFile:
    roundPoints = 0
    text = (line.rstrip()).split(" ")

    if text[1] == "X":
        text[1] = strategyLose[text[0]]
    elif text[1] == "Y":
        roundPoints += 3
        text[1] = strategyDraw[text[0]]
    elif text[1] == "Z":
        roundPoints += 6
        text[1] = strategyWin[text[0]]

    roundPoints += point[text[1]]
    result += roundPoints
print(result)
