ReadFile = open('input6.txt', 'r')

time = (ReadFile.readline().rstrip()).split()
time = list(map(int, (time[1:len(time)])))
record_distance = (ReadFile.readline().rstrip()).split()
record_distance = list(map(int, (record_distance[1:len(record_distance)])))

result = 1

for race_index in range(len(time)):
    ways = 0
    for velocity in range(1, time[race_index]):
        distance  = (time[race_index] - velocity) * velocity
        if distance  > record_distance[race_index]:
            ways += 1
    result *= ways
print(result)

