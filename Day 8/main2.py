ReadFile = open('./input.txt', 'r')

Tree = []
Result = 0

def TreeFromList(lista):
    newList = []
    lista = lista[0]
    for x in range(len(lista)):
        newList.append(lista[x])
    return newList
def reversDane(list):
    reversList = []
    for iterator in range(len(list)):
        reversList.append(list[len(list) -1 - iterator])
    return reversList

def GetDirectionTrees(lista, direction, column, FromTree):
    TreesList = []
    for row in range(len(lista)):
        if row > FromTree and direction == "Down":
            TreesList.append(lista[row][column])
        elif row < FromTree and direction == "Up":  # Up
            TreesList.append(lista[row][column])
    return TreesList

def Count_see_Tree(TreeList, heightActiveTree):
    heightActiveTree = int(heightActiveTree)
    count = 0
    for tree in TreeList:
        tree = int(tree)
        if tree < heightActiveTree:
            count += 1
        elif tree >= heightActiveTree:
            count += 1
            return count
    return count

def Is_the_tallest_Tree(Tree, row, column):
    heightActiveTree = Tree[row][column]
    Left = reversDane(Tree[row][0:column])
    Right = Tree[row][column + 1:len(Tree[row])]
    Down = GetDirectionTrees(Tree, 'Down', column, row)
    Up = reversDane(GetDirectionTrees(Tree, 'Up', column, row))
    L = Count_see_Tree(Left, heightActiveTree)
    R = Count_see_Tree(Right, heightActiveTree)
    D = Count_see_Tree(Down, heightActiveTree)
    U = Count_see_Tree(Up, heightActiveTree)
    return int(L*R*D*U)


for line in ReadFile:
    line = line.rstrip()
    line = line.split(" ")
    Tree.append(TreeFromList(line))
ReadFile.close()
for row in range(0, len(Tree)):
    for column in range(0, len(Tree[row])):
        points = Is_the_tallest_Tree(Tree,row,column)
        if Result < points:
            Result = points
print(Result)
