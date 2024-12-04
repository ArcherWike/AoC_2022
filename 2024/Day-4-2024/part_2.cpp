//--- Day 4: Ceres Search ---
//Part 2 / 04.12.2024 / Advent of Code
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <chrono>
#include <sstream>

bool check_word(char word[])
{
    std::stringstream ss;
    ss << word[0] << word[1] << word[2];
    std::string sentence = ss.str();

    if (sentence == "MAS" || sentence == "SAM") return true;
    return false;
}

int main() {
    auto start = std::chrono::high_resolution_clock::now();
    int solution{};

    //Read input from file
    std::ifstream file;
    file.open("./source.txt");
    if (!file) {
        std::cerr << "Cannot open the file!" << std::endl;
        return 1;
    }

    std::vector<std::string> lines;
    std::string text;

    while (std::getline(file, text)) {

        lines.push_back(text);
    }
    file.close();

    char word[3];

    for (int i = 0; i < lines.size(); i++)
    {
        std::string l = lines[i];
        for (int sign_index = 0; sign_index < l.size(); sign_index++)
        {
            char sign = l[sign_index];

            if (sign == 'A')
            {
                int xmas_counter = 0;

                if ((sign_index > 0 and sign_index + 1 < l.size()) and (i > 0 and i + 1 < lines.size()))
                {
                    word[0] = lines[i - 1][sign_index - 1];
                    word[1] = sign;
                    word[2] = lines[i + 1][sign_index + 1];

                    if (check_word(word)) xmas_counter++;

                    word[0] = lines[i - 1][sign_index + 1];
                    word[1] = sign;
                    word[2] = lines[i + 1][sign_index - 1];

                    if (check_word(word)) xmas_counter++;
                }
                if (xmas_counter > 1) solution++;

            }
        }
    }

    auto stop = std::chrono::high_resolution_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(stop - start);

    std::cout << "The solution is: " << solution << std::endl;
    std::cout << "Time: " << duration.count() << " milliseconds" << std::endl;

    return 0;
}
