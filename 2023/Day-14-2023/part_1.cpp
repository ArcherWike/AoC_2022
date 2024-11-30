//Part 1 / 14.12.2023 / Advent of Code

#include <iostream>
#include <fstream>
#include <string>
#include <vector>

void moveStones(std::vector<std::string> &lines)
{
    int lenght = lines[0].size();

    for (int line_index{}; line_index < lines.size(); line_index++) {

        std::string active_line = lines[line_index];

        for (int line_char{}; line_char < lenght; line_char++)
        {
            if (active_line[line_char] == 'O')
            {
                int temp_index = line_index;
                while (temp_index - 1 >= 0)
                {
                    if (lines[temp_index - 1][line_char] == '.' && temp_index - 1 == 0)
                    {
                        lines[line_index][line_char] = '.';
                        lines[temp_index - 1][line_char] = 'O';
                    }
                    else if (lines[temp_index - 1][line_char] != '.')
                    {
                        //move stone to another line
                        if (temp_index != line_index)
                        {
                            std::string lineOne = lines[line_index];
                            std::string lineTwo = lines[temp_index];

                            lines[line_index][line_char] = '.';
                            lines[temp_index][line_char] = 'O';
                        }
                        break;
                    }
                    temp_index--;
                }
            }
        }
    }
}

int getWeightStones(std::vector<std::string>& lines)
{
    int lenght = lines[0].size();
    int total{};
    int level = 1;

    for (int line_index = lines.size() - 1; line_index >= 0; line_index--) {
        int level_points{};
        std::string active_line = lines[line_index];

        for (int line_char{}; line_char < lenght; line_char++)
        {
            if (active_line[line_char] == 'O')
            {
                level_points += level;
            }
        }
        std::cout << std::endl << level << "new line :" << level_points << std::endl;

        total += level_points;
        level++;
    }
    return total;
}

int main() {
    std::ifstream file("source.txt");
    if (!file) {
        std::cerr << "Cannot open the file!" << std::endl;
        return 1;
    }

    std::vector<std::string> lines;
    std::string line;
    while (std::getline(file, line)) {
        
        lines.push_back(line);
        moveStones(lines);
    }

    file.close();

    moveStones(lines);

    for (int line_index{}; line_index < lines.size(); line_index++) {
        std::cout << lines[line_index] << std::endl;
    }
    std::cout << getWeightStones(lines);

    return 0;
}
