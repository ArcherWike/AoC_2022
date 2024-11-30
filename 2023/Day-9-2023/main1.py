ReadFile = open('input9.txt', 'r')


result = 0

for line in ReadFile:
    #line = line.rstrip().split()
    line = list(map(int, line.strip().split()))
    sensor = []
    sensor.append(line)

    #generated data - prediction of the next value
    while True:
        generated_data = []
        zero_num = 0
        for i in range(len(sensor[len(sensor) - 1]) - 1):
            generated_data.append((sensor[len(sensor) - 1][i + 1]) - (sensor[len(sensor) - 1][i]))
            if generated_data[i] == 0:
                zero_num += 1
        sensor.append(generated_data)
        if (zero_num == len(generated_data)):
            break

    #fill dataset
    sensor[len(sensor) - 1].append(0)

    for i in range(1, len(sensor)):
        new_placeholders = sensor[len(sensor) - 1 - i][-1] + sensor[len(sensor) - i][-1]
        sensor[len(sensor) - 1 - i].append(new_placeholders)
    result += sensor[len(sensor) - 1 - i][-1]

print(result)