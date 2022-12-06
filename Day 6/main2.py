ReadFile = open('./input.txt', 'r')

def unrepeated(zestaw):
    for x in zestaw:
        if zestaw.count(x) > 1:
            return False
    return True

n = 0
dane = []
for line in ReadFile:
    line = line.rstrip()
    dane = list(line)

    for index in range(14,len(dane)):
        test = (dane[index-14:index])
        if (unrepeated(test)):
            n = index
            break
    print(n)