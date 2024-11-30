//Part 2 / 15.12.2023 / Advent of Code
#include <iostream>
#include <fstream>
#include <string>
#include <vector>

int totalSum{};

void hashValue(char sign, int &currentValue)
{
    currentValue += (int)sign;
    currentValue *= 17;
    currentValue %= 256;
}

int getBoxIndex(std::string label)
{
    int currentValue = 0;
    for (int i = 0; i < label.size(); i++)
    {
        hashValue(label[i], currentValue);
    }
    return currentValue;
}

struct Lens
{
    Lens(std::string label, int focalLength)
        :m_label(label),
        m_focalLength(focalLength)
    {}
    std::string m_label;
    int m_focalLength; //from 1..9
};

std::ostream& operator<<(std::ostream& out, const Lens& lens)
{
    return out << " [ " << lens.m_label << " " << lens.m_focalLength << " ]";
}

class Box
{
public:
    void performOperation(char operation_sign, std::string label, int newFocalLength)
    {
        if (operation_sign == '-') dashOperation(label);
        else if (operation_sign == '=') equalOperation(label, newFocalLength);
    }

    void equalOperation(std::string label, int newFocalLength)
    {
        int l_index = getLabelIndex(label);

        //label was founded so replace lens
        if (l_index >= 0)
        {
            m_slots[l_index].m_focalLength = newFocalLength;
        }
        //add new lens
        else
        {
            Lens new_lens = Lens(label, newFocalLength);
            m_slots.push_back(new_lens);
        }
    }

    void dashOperation(std::string label)
    {
        int l_index = getLabelIndex(label);

        //pull out this lens
        if (l_index >= 0)
        {
            removeLens(l_index);
        }
        return;
    }

    void ShowBox()
    {
        
        for (int i = 0; i < m_slots.size(); i++)
        {
            std::cout << m_slots[i];
        }
        std::cout << "\n";
    }

    int focusingPower(int box_index)
    {
        int totalPower{};
        for (int i = 0; i < m_slots.size(); i++)
        {
            //sum of (slot number) * (focal length)
            totalPower += (box_index + 1) * (i + 1) * m_slots[i].m_focalLength;
        }
        return totalPower;
    }

private:
    std::vector<Lens> m_slots;

    int getLabelIndex(std::string& label_to_find)
    {
        for (int i = 0; i < m_slots.size(); i++)
        {
            if (m_slots[i].m_label == label_to_find) return i;
        }
        return -1;
    }
    void removeLens(int &index)
    {
        m_slots.erase(m_slots.begin() + index);
    }
};

int main() {
    char ch;
    std::fstream file("source.txt", std::fstream::in);
    if (!file) {
        std::cerr << "Cannot open the file!" << std::endl;
        return 1;
    }
    Box* boxes = new Box[256];
    
    std::string lens_label = "";
    char last_sign = '/';
    int focalLength{};

    while (file >> std::noskipws >> ch) {
        if (ch == ' ') {}
        else if (ch != ',')
        {
            if (ch == '-' || ch == '=')
            {
                last_sign = ch;
            }
            else if (isdigit(ch))
            {
                focalLength = (int)ch - 48;
            }
            else
            {
                lens_label += ch;
            }
        }
        else if (ch == ',')
        {
            boxes[getBoxIndex(lens_label)].performOperation(last_sign, lens_label,focalLength);

            //clear settings after action (be ready for next one)
            lens_label = "";
            last_sign = '/';
            focalLength = 0;
        }
    }
    file.close();
    boxes[getBoxIndex(lens_label)].performOperation(last_sign, lens_label, focalLength);

    for (int i = 0; i < 256; i++)
    {
        std::cout << "\n" << "___Box " << i << ": ";
        boxes[i].ShowBox();

        totalSum += boxes[i].focusingPower(i);
    }
    std::cout << "sum is: " << totalSum;

    return 0;
}