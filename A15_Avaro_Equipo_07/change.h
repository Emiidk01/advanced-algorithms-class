#ifndef CHANGE_H
#define CHANGE_H

#include <iostream>
#include <vector>
#include <algorithm>

class Change
{
private:
    std::vector<int> denominations;
    int numberOfCoins;

public:
    // Constructor
    Change(int num_denominations, std::vector<int> denoms) : numberOfCoins(num_denominations), denominations(denoms)
    {
        std::sort(denominations.begin(), denominations.end(), std::greater<int>());
    }

    // calculate the change
    std::vector<int> calculateChange(int prize, int bill)
    {
        int change = bill - prize;
        std::vector<int> coinsUsed(numberOfCoins, 0);

        for (int i = 0; i < numberOfCoins; i++)
        {
            while (change >= denominations[i])
            {
                change -= denominations[i];
                coinsUsed[i]++;
            }
        }

        return coinsUsed;
    }

    // print the result
    void printChange(const std::vector<int> &coinsUsed)
    {
        for (int i = 0; i < numberOfCoins; i++)
        {
            std::cout << coinsUsed[i] << std::endl;
        }
    }
};

#endif // CHANGE_H