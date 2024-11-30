ReadFile = open('input1.txt', 'r')

calibrations_list = []
result = 0

def find_first_digit(arg_list):
    for i in range(len(arg_list)):
        if (arg_list[i].isdigit()):
            return str(arg_list[i])
    return None

for line in ReadFile:
    line = "".join(line.strip('\n'))
    calibrations_list.append(line)
    first_num = find_first_digit(line)
    reserved_line = ''
    for char in reversed(line):
        reserved_line += char
    last_num = find_first_digit(reserved_line)
    current_calibration = first_num + last_num
    result += int(current_calibration)
print(result)