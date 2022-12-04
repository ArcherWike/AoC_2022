ReadFile = open("./message.txt", 'r')
resultCollection = []
result = 0

for line in ReadFile:
    row = line.rstrip()

    m = []          #first rucksack's compartments
    for index in range(0, int(len(row) / 2)):
        if row[index] not in m:
            m.append(row[index])

    n = []          #second rucksack's compartments
    for index in range(int(len(row) / 2), int(len(row))):
        if row[index] not in n:
            n.append(row[index])

    k = len(m)
    for x in m:
        if x in n:
            resultCollection.append(x)
        k -= 1
    if k > 0:
        print("LUIL")


for x in resultCollection:
    asciii = ord(x)
    if asciii >= 97:
        asciii -= 96
    else:
        asciii -= 38
    result += asciii
print(result)