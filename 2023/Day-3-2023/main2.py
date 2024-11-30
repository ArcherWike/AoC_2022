ReadFile = open('input3.txt', 'r')

input_lines = ReadFile.readlines()


def IsSymbol(char):
    if (char.isdigit()):
        return True
    return False


def find_number(line, gear_index):
    number = ''
    start_ix = gear_index
    end_ix = gear_index

    current_index = gear_index - 1
    while (current_index >= 0):
        if (IsSymbol(line[current_index])):
            current_index -= 1
        else:
            break
    current_index += 1
    start_ix = current_index

    current_index = gear_index
    while (current_index <= len(line)):
        if (IsSymbol(line[current_index])):
            current_index += 1
        else:
            break
    current_index -= 1
    end_ix = current_index

    current_index = start_ix
    while (current_index <= end_ix):
        number += line[current_index]
        current_index += 1
    return number


part_engine = []

number = ''
index_start = 0
index_end = 0
check_num = False

sum_result = 0

for index in range(len(input_lines)):
    line = input_lines[index]
    gear_number = 0
    for symbol_index in range(len((input_lines[index]))):
        index_start = symbol_index
        index_end = symbol_index
        # Find first index number
        if (input_lines[index][symbol_index] == '*'):
            up_num = []
            row_num = []
            down_num = []
            # in the row
            if (index_start > 0):
                index_start -= 1
                if (IsSymbol(input_lines[index][index_start])):
                    new_num = find_number(input_lines[index], index_start)
                    if new_num not in row_num:
                        row_num.append(new_num)
                    gear_number += 1
            if (index_end < len(line)):
                index_end += 1
                if (IsSymbol(input_lines[index][index_end])):
                    new_num = find_number(input_lines[index], index_end)
                    if new_num not in row_num:
                        row_num.append(new_num)
                    gear_number += 1

            for number_index in range(index_start, index_end + 1):
                # previous line
                if (index > 0):
                    if (IsSymbol(input_lines[index - 1][number_index])):
                        gear_number += 1
                        new_num = find_number(input_lines[index - 1], number_index)
                        if new_num not in up_num:
                            up_num.append(new_num)

                # next line
                if index + 1 < len(input_lines):
                    if (IsSymbol(input_lines[index + 1][number_index])):
                        gear_number += 1
                        new_num = find_number(input_lines[index + 1], number_index)
                        if new_num not in down_num:
                            down_num.append(new_num)

            gear_numbers_list = down_num[:] + up_num[:] + row_num[:]
            if (gear_number > 1 and len(row_num) + len(down_num) + len(up_num) > 1):
                sum = 0
                for i in gear_numbers_list:
                    if sum == 0:
                        sum = int(i)
                    else:
                        sum *= int(i)

                sum_result += sum
            number = ''
            check_num = False
print(sum_result)
