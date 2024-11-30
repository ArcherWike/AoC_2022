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

point = {
    'X': 1,
    'Y': 2,
    'Z': 3
}
# "Pierwsza kolumna to to, co zagra twój przeciwnik: " \
# "dla Rocka, dla papieru i dla nożyczek. Druga kolumna... .ABC
#
# Druga kolumna, rozumujesz, musi być tym, co powinieneś zagrać w odpowiedzi:
# X dla Skały, Y dla Papieru i Z dla Nożyczek. .XYZ

for line in readFile:
    roundPoints = 0
    text = (line.rstrip()).split(" ")
    roundPoints += point[text[1]]       #Punkt za kształt

    if strategyDraw[text[0]] == text[1]: # remis
        roundPoints += 3
    if strategyWin[text[0]] == text[1]: #wygrana
        roundPoints += 6

    result += roundPoints

print(result)
