// -----------------------------------------------------

// Implementation of the "Dynamic Programming" technique for the Coin Change Problem

// Created On: 31/08/2024
// Updated On: 31/08/2024

// Authors:
//     Angel Mauricio Ramirez Herrera - A01710158
//     Cristian Chavez Guia - A0171680
//     Emiliano Gomez Gonzalez - A01710711

// -----------------------------------------------------

#ifndef DYNAMIC_CHANGE_H
#define DYNAMIC_CHANGE_H

#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

class DynamicChange
{
private:
    std::vector<int> denominations;
    int numberOfCoins;

public:
    // Constructor
    DynamicChange(int num_denominations, std::vector<int> denoms) : numberOfCoins(num_denominations), denominations(denoms)
    {
        std::sort(denominations.begin(), denominations.end(), std::greater<int>());
    }

    // Calculate the change using dynamic programming
    std::vector<int> calculateChange(int prize, int bill)
    {
        int change = bill - prize;
        std::vector<int> dp(change + 1, INT_MAX);
        std::vector<int> coinUsed(change + 1, -1);
        dp[0] = 0;

        for (int i = 0; i < numberOfCoins; i++)
        {
            for (int j = denominations[i]; j <= change; j++)
            {
                if (dp[j - denominations[i]] != INT_MAX && dp[j - denominations[i]] + 1 < dp[j])
                {
                    dp[j] = dp[j - denominations[i]] + 1;
                    coinUsed[j] = i;
                }
            }
        }

        std::vector<int> result(numberOfCoins, 0);
        int tempChange = change;
        while (tempChange > 0 && coinUsed[tempChange] != -1)
        {
            result[coinUsed[tempChange]]++;
            tempChange -= denominations[coinUsed[tempChange]];
        }

        return result;
    }
};

#endif // DYNAMIC_CHANGE_H
