ReadFile = open('input8.txt', 'r')

step_info = ReadFile.readline().split()[0]
line = ReadFile.readline() #empty line

map = {}
started_loc = 'AAA'
end_loc = 'ZZZ'
for line in ReadFile:
    line = line.strip().split()
    l = line[2][1:len(line[2])-1]
    r = line[3][:len(line[3])-1]
    map[line[0]] = [l,r]
    if started_loc == '':
        started_loc = line[0]

location = started_loc

result_step = 0
index_step = 0
while location != end_loc:
    result_step += 1
    if step_info[index_step] == 'R':
        location = map[location][1]
    else:
        location = map[location][0]
    index_step += 1
    if index_step >= len(step_info):
        index_step = 0
    if location == end_loc:
        break

print(result_step)





