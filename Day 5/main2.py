ReadFile = open('./input.txt','r')
SupplyStacks = []

#______________________[ FUNCTION ]______________________________________________
def ShowAnswer(a):
    result = ''
    for x in range(len(a)):
        result += (a[x][-1])
    return result

def reversDane(list):
    reversList = []
    for iterator in range(len(list)):
        reversList.append(list[len(list) -1 - iterator])
    return reversList

#_____________________________________________________________________________
StackSorted = False
for line in ReadFile:   ##Loading Input
    if "[" in line:
        line = line.rstrip()
        x = 0
        for i in range(1,len(line),4):
            if line[i] != " ":
                z = len(SupplyStacks)
                if len(SupplyStacks) < x:
                    while len(SupplyStacks)-2< x:
                        SupplyStacks.append([])
                SupplyStacks[x].append(line[i])
            x += 1
    if line[0] == "m":          #Move crates
        if StackSorted == False:
            for x in range(len(SupplyStacks)):
                SupplyStacks[x] = reversDane(SupplyStacks[x])
            StackSorted = True
        line.rstrip("\n")
        command = line.split(" ")

        Move = int(command[5]) - 1
        From = int(command[3]) - 1
        Amount = int(command[1])

        StackAmount = len(SupplyStacks[From]) - Amount
        if StackAmount <= 0:
            StackAmount = 0
        joinList = []
        if StackAmount <= 0:
            StackAmount = 0
        for index in range(StackAmount, len(SupplyStacks[From])):
            joinList.append(SupplyStacks[From][index])
        for index in joinList:
            SupplyStacks[Move].append(index)
        del SupplyStacks[From][int(StackAmount):len(SupplyStacks[From])]
print(ShowAnswer(SupplyStacks))
#Your puzzle answer was MHQTLJRLB.