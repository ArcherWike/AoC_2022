//Part 1 / 15.12.2023 / Advent of Code
#include <iostream>
#include <fstream>
#include <string>
#include <vector>

int currentValue = 0;
int totalSum{};

void hashValue(char sign)
{
    currentValue += (int)sign;
    currentValue *= 17;
    currentValue %= 256;
}

int main() {
    char ch;
    std::fstream file("source.txt", std::fstream::in);
    if (!file) {
        std::cerr << "Cannot open the file!" << std::endl;
        return 1;
    }

    while (file >> std::noskipws >> ch) {
        if (ch != ',')
        {
            hashValue(ch);
            
        }
        else if (ch == ' ')
        {
            continue;
        }
        else
        {
            totalSum += currentValue;
            currentValue = 0;

        }
    }
    totalSum += currentValue;
    file.close();
    std::cout << totalSum;

    return 0;
}
