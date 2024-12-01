//--- Day 1: Historian Hysteria ---
//Part 2 / 01.12.2024 / Advent of Code

#include <iostream>
#include <fstream>
#include <string>
#include <vector>

int main() {
    std::string text;
    std::ifstream file("./source.txt");
    if (!file) {
        std::cerr << "Cannot open the file!" << std::endl;
        return 1;
    }
    bool is_first = true;

    std::vector<int> left;
    std::vector<int> right;

    while (std::getline(file, text)) {
        left.push_back(stoi(text.substr(0, 6)));
        right.push_back(stoi(text.substr(8, 6)));
    }

    file.close();

    int total{};
    for (int i = 0; i < left.size(); i++)
    {
        int amount = std::count(right.begin(), right.end(), left[i]);
        total += left[i] * amount;
    }

    std::cout << total;

    return 0;
}