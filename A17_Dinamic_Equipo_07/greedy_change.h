// -----------------------------------------------------

// Implementation of the "Greedy Algorithm" technique for the Coin Change Problem

// Created On: 31/08/2024
// Updated On: 31/08/2024

// Authors:
//     Angel Mauricio Ramirez Herrera - A01710158
//     Cristian Chavez Guia - A0171680
//     Emiliano Gomez Gonzalez - A01710711

// -----------------------------------------------------

#ifndef GREEDY_CHANGE_H
#define GREEDY_CHANGE_H

#include <iostream>
#include <vector>
#include <algorithm>

class GreedyChange
{
private:
    std::vector<int> denominations;
    int numberOfCoins;

public:
    // Constructor
    GreedyChange(int num_denominations, std::vector<int> denoms) : numberOfCoins(num_denominations), denominations(denoms)
    {
        std::sort(denominations.begin(), denominations.end(), std::greater<int>());
    }

    // Calculate the change using a greedy algorithm
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
};

#endif // GREEDY_CHANGE_H
