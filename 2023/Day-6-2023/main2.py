ReadFile = open('input6.txt', 'r')

time = (ReadFile.readline().rstrip()).split()
time = time[1:len(time)]
time = int("".join(time))

record_distance = (ReadFile.readline().rstrip()).split()
record_distance = record_distance[1:len(record_distance)]
record_distance = int("".join(record_distance))

result = 1

ways = 0
for velocity in range(1, time):
    distance = (time - velocity) * velocity
    if distance > record_distance:
        ways += 1
result *= ways
print(result)