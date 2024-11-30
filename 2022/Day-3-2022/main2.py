ReadFile = open("./Input.txt", 'r')
resultCollection = []
FinishResult = 0

def CountPoints(p, d, t):
    CommonCollection = []
    result = 0
    for x in p:
        if x in d and x in t:
            CommonCollection.append(x)
    for x in CommonCollection:
        asciii = ord(x)
        if asciii >= 97:
            asciii -= 96
        else:
            asciii -= 38
        result += asciii
    return result

def AppendMark(list):
    collection = []
    for mark in list:
        if mark not in collection:
            collection.append(mark)
    return collection

Elf_number = 1
p = []  #first Elf
d = []  #second Elf
t = []  #third Elf

for line in ReadFile:
    row = line.rstrip()
    if Elf_number == 1:
        p = AppendMark(row).copy()
    if Elf_number == 2:
        d = AppendMark(row).copy()
    if Elf_number == 3:
        t = AppendMark(row).copy()
        FinishResult += CountPoints(p,d,t)
        p = p.clear()
        d = d.clear()
        t = t.clear()
        Elf_number = 0
    Elf_number += 1
print(FinishResult)

