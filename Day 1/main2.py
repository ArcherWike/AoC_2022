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
totalBestElf = 0
for index in range(0, 3):
    totalBestElf += totalElfCalories[index]
print(totalBestElf)