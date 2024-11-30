ReadFile = open('input2.txt', 'r')

Id_sum = 0

max_colors = {'red' : 12,
              'green' : 13,
              'blue' : 14}

def count_colors(array):
    colors = {'red' : 0,
              'green' : 0,
              'blue' : 0}

    for bags in array:
        cubes_in_bag = bags.split(', ')
        for cube in cubes_in_bag:
            cube_info = cube.split(" ")
            #colors[cube_info[1]] += int(cube_info[0])

            if int(cube_info[0]) > max_colors[cube_info[1]]:
                return False

    return True


for line in ReadFile:
    line = line.strip('\n').split(": ")
    current_Id = line[0].split(" ")
    current_Id = current_Id[1]
    bag = line[1].split("; ")

    if (current_Id == '99'):
        print(count_colors(bag))
        break

    if (count_colors(bag)):
        print(current_Id, line)

        Id_sum += int(current_Id)
    #else:
        #print(current_Id, line)
print(Id_sum)

#265 #5050

#2617