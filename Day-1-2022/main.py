openFile = open('./input.txt', 'r')
totalElfCalories = []
sum = 0
for line in openFile:
    value = line.rstrip()
    if line != "\n":
        sum += int(value)
    else:
        totalElfCalories.append(sum)
        sum = 0

totalElfCalories.sort(reverse=True)
print(totalElfCalories[0])
