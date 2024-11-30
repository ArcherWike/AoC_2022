ReadFile = open('input3.txt', 'r')

input_lines = ReadFile.readlines()
def IsSymbol(char):
    if (char == '.' or char == '\n'):
        return False
    return True

part_engine = []

number = ''
index_start = 0
index_end = 0
check_num = False

sum_result = 0

for index in range(len(input_lines)):
    line = input_lines[index]
    for symbol_index in range(len((input_lines[index]))):
        #Find first index number
        if (input_lines[index][symbol_index].isdigit()):
            if not check_num:
                check_num = True
                index_start = symbol_index
                number += str(input_lines[index][symbol_index])
            else:
                number += str(input_lines[index][symbol_index])
        else:
            if check_num:
                check_num = False
                index_end = symbol_index - 1
                num_engine_part = False

                #in the row
                if (index_start > 0):
                    index_start -= 1
                    if (IsSymbol(input_lines[index][index_start])):
                        num_engine_part = True
                if (index_end < len(line)):
                    index_end += 1
                    if (IsSymbol(input_lines[index][index_end])):
                        num_engine_part = True

                if not num_engine_part:
                    for number_index in range(index_start, index_end + 1):
                        #previous line
                        if index > 0:
                            if (IsSymbol(input_lines[index - 1][number_index])):
                                num_engine_part = True
                                continue
                        #next line
                        if index + 1 < len(input_lines):
                            if (IsSymbol(input_lines[index + 1][number_index])):
                                num_engine_part = True
                                continue
                if (num_engine_part):
                    part_engine.append(number)
                    sum_result += int(number)
                number = ''
                check_num = False
print(sum_result)

