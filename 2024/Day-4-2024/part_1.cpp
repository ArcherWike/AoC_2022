//--- Day 4: Ceres Search ---
//Part 4 / 04.12.2024 / Advent of Code
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <chrono>
#include <sstream>

bool check_word(char word[])
{
    std::stringstream ss;
    ss << word[0] << word[1] << word[2] << word[3];
    std::string sentence = ss.str();

    if (sentence == "XMAS") return true;
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

    char word[4];

    for (int i = 0; i < lines.size(); i++)
    {
        std::string l = lines[i];
        for (int sign_index = 0; sign_index < l.size(); sign_index++)
        {
            char sign = l[sign_index];

            if (sign == 'M')
            {
                //right or left
                if (sign_index > 0 and sign_index + 2 < l.size())
                {
                    word[0] = l[sign_index - 1];
                    word[1] = sign;
                    word[2] = l[sign_index + 1];
                    word[3] = l[sign_index + 2];

                    if (check_word(word)) solution++;

                }
                if (sign_index > 1 and sign_index + 1 < l.size())
                {
                    word[0] = l[sign_index + 1];
                    word[1] = sign;
                    word[2] = l[sign_index - 1];
                    word[3] = l[sign_index - 2];

                    if (check_word(word)) solution++;
                }

                //horizontal - top or bacward
                if (i > 0 and i + 2 < lines.size())
                {
                    word[0] = lines[i - 1][sign_index];
                    word[1] = sign;
                    word[2] = lines[i + 1][sign_index];
                    word[3] = lines[i + 2][sign_index];
                    if (check_word(word)) solution++;
                }
                if (i > 1 and i + 1 < lines.size())
                {
                    word[0] = lines[i + 1][sign_index];
                    word[1] = sign;
                    word[2] = lines[i - 1][sign_index];
                    word[3] = lines[i - 2][sign_index];

                    if (check_word(word)) solution++;
                }
                //diagonal \ 
                if ((sign_index > 0 and sign_index + 2 < l.size()) and (i > 0 and i + 2 < lines.size()))
                {
                    word[0] = lines[i - 1][sign_index - 1];
                    word[1] = sign;
                    word[2] = lines[i + 1][sign_index + 1];
                    word[3] = lines[i + 2][sign_index + 2];

                    if (check_word(word)) solution++;
                }
                if ((sign_index > 1 and sign_index + 1 < l.size()) and (i > 1 and i + 1 < lines.size()))
                {
                    word[3] = lines[i - 2][sign_index - 2];
                    word[2] = lines[i - 1][sign_index - 1];
                    word[0] = lines[i + 1][sign_index + 1];
                    word[1] = sign;

                    if (check_word(word)) solution++;
                }
                //diagonal /
                if (sign_index > 0 and sign_index + 2 < l.size() and i > 1 and i + 1 < lines.size())
                {
                    word[3] = lines[i - 2][sign_index + 2];
                    word[2] = lines[i - 1][sign_index + 1];
                    word[0] = lines[i + 1][sign_index - 1];
                    word[1] = sign;

                    if (check_word(word)) solution++;
                }
                if (sign_index > 1 and sign_index + 1 < l.size() and (i > 0 and i + 2 < lines.size()))
                {
                    word[0] = lines[i - 1][sign_index + 1];
                    word[1] = sign;
                    word[2] = lines[i + 1][sign_index - 1];
                    word[3] = lines[i + 2][sign_index - 2];

                    if (check_word(word)) solution++;
                }
            }
        }
    }

    auto stop = std::chrono::high_resolution_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(stop - start);

    std::cout << "The solution is: " << solution << std::endl;
    std::cout << "Time: " << duration.count() << " milliseconds" << std::endl;

    return 0;
}
