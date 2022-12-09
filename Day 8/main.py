ReadFile = open('./input.txt', 'r')

Tree = []
Result = 0

def TreeFromList(lista):
    newList = []
    lista = lista[0]
    for x in range(len(lista)):
        newList.append(lista[x])
    return newList

def GetDirectionTrees(lista, direction, column, FromTree):
    TreesList = []
    for row in range(len(lista)):
        if row > FromTree and direction == "Down":
            TreesList.append(lista[row][column])
        elif row < FromTree and direction == "Up":  # Up
            TreesList.append(lista[row][column])
    return TreesList

def Check_All_smallest(TreeList, heightActiveTree):
    heightActiveTree = int(heightActiveTree)
    for tree in TreeList:
        tree = int(tree)
        if tree >= heightActiveTree:
            return False
    return True

def Is_the_tallest_Tree(Tree, row, column):
    heightActiveTree = Tree[row][column]
    Left = Tree[row][0:column]
    Right = Tree[row][column + 1:len(Tree[row])]
    Down = GetDirectionTrees(Tree, 'Down', column, row)
    Up = GetDirectionTrees(Tree, 'Up', column, row)
    L = Check_All_smallest(Left, heightActiveTree)
    R = Check_All_smallest(Right, heightActiveTree)
    D = Check_All_smallest(Down, heightActiveTree)
    U = Check_All_smallest(Up, heightActiveTree)

    if (L == R == D == U == False):
        return False
    return True


for line in ReadFile:
    line = line.rstrip()
    line = line.split(" ")
    Tree.append(TreeFromList(line))
ReadFile.close()
for row in range(1, len(Tree)-1):
    for column in range(1, len(Tree[row])-1):
        print(Tree[row][column], end="")
        if (Is_the_tallest_Tree(Tree,row,column)):
            Result +=1
            print(True)
        else:
            print(False)

Result += (len(Tree)*2 + (len(Tree)-2)*2)
print(Result)