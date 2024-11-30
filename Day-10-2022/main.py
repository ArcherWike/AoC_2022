ReadFile = open('./input.txt', 'r')

SignalStrengthTestValue = [20, 60, 100, 140, 180, 220]

X = 1 #register
nrOfCycle = 1
result = 0

for line in ReadFile:
    line = line.rstrip()
    if line == 'noop':
        iterator = 1
        V = 0

    elif line[0:4] == 'addx':
        line = line.split(' ')
        iterator = 2
        V = int(line[1]) #value
    for i in range(iterator):
        if nrOfCycle in SignalStrengthTestValue:
            value = nrOfCycle*X
            result += value
        nrOfCycle += 1
    X += V
print(result)



