//Part 2 / 14.12.2023 / Advent of Code
#include <iostream>
#include <fstream>
#include <string>
#include <vector>

void rotateArrayToRight(std::vector<std::string>& temp_lines)
{
    int lenght = temp_lines[0].size();
    std::vector<std::string> new_temp_lines;
    std::string updated_line = "";

    for (int line_char{}; line_char < lenght; line_char++)
    {
        updated_line = "";
        for (int row_index = temp_lines.size() - 1; row_index >= 0; row_index--)
        {
            updated_line += temp_lines[row_index][line_char];
        }
        new_temp_lines.push_back(updated_line);
    }
    
    temp_lines = new_temp_lines;
}

//rolling rocks up to the edges of the platform
void moveStonesUp(std::vector<std::string>& lines)
{
    int lenght = lines[0].size();

    for (int line_index{}; line_index < lines.size(); line_index++) {
        std::string active_line = lines[line_index];

        for (int line_char{}; line_char < lenght; line_char++)
        {
            if (active_line[line_char] == 'O')
            {
                int temp_index = line_index;

                //move stone as far up as possible
                while (temp_index - 1 >= 0)
                {
                    if (lines[temp_index - 1][line_char] == '.' && temp_index - 1 == 0)
                    {
                        lines[line_index][line_char] = '.';
                        lines[temp_index - 1][line_char] = 'O';
                    }
                    else if (lines[temp_index - 1][line_char] != '.')
                    {
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

        total += level_points;
        level++;
    }
    return total;
}
void SpinCycle(std::vector<std::string>& lines)
{
    for (int i{}; i < 4; i++)
    {
        for (int line_index{}; line_index < lines.size(); line_index++) {
            moveStonesUp(lines);
        }
        rotateArrayToRight(lines);
    }
    
}

int main() {
    //settings
    int numOfCycles = 1000;
    std::string fileName = "source.txt";

    std::ifstream file(fileName);
    if (!file) {
        std::cerr << "Cannot open the file!" << std::endl;
        return 1;
    }

    std::vector<std::string> lines;
    std::string line;
    while (std::getline(file, line)) {

        lines.push_back(line);
    }

    file.close();

    for (int i{}; i < numOfCycles; i++)
    {
        SpinCycle(lines);
    }

    std::cout << getWeightStones(lines);

    return 0;
}
