// -----------------------------------------------------

// Implementation of the "Dynamic Programming" and "Greedy Algorithm" techniques for the Coin Change Problem

// Created On: 31/08/2024
// Updated On: 31/08/2024

// Authors:
//     Angel Mauricio Ramirez Herrera - A01710158
//     Cristian Chavez Guia - A0171680
//     Emiliano Gomez Gonzalez - A01710711

// Code Description:
// This program solves the coin change problem using both dynamic programming and a greedy algorithm.
// The program reads a list of denominations and calculates the change for a given product price and bill value.
// The results are displayed for both methods.

// -----------------------------------------------------

#include <iostream>
#include <vector>
#include "dynamic_change.h"
#include "greedy_change.h"

void runTestCase(int n, std::vector<int> denominations, int p, int q) {
    // Using Dynamic Programming
    DynamicChange dynamicChange(n, denominations);
    std::vector<int> dynamicResult = dynamicChange.calculateChange(p, q);
    std::cout << "Dynamic Programming Result:\n";
    for (int i = 0; i < n; i++)
    {
        std::cout << dynamicResult[i] << "\n";
    }

    // Using Greedy Algorithm
    GreedyChange greedyChange(n, denominations);
    std::vector<int> greedyResult = greedyChange.calculateChange(p, q);
    std::cout << "Greedy Algorithm Result:\n";
    for (int i = 0; i < n; i++)
    {
        std::cout << greedyResult[i] << "\n";
    }
}

int main()
{
    // Test Case 1
    std::cout << "Test Case 1:\n";
    int n1 = 6;
    std::vector<int> denominations1 = {1, 5, 10, 25, 50, 100};
    int p1 = 76;
    int q1 = 1000;
    runTestCase(n1, denominations1, p1, q1);

    // Test Case 2
    std::cout << "Test Case 2:\n";
    int n2 = 4;
    std::vector<int> denominations2 = {1, 3, 4, 5};
    int p2 = 7;
    int q2 = 12;
    runTestCase(n2, denominations2, p2, q2);

    // Test Case 3
    std::cout << "Test Case 3:\n";
    int n3 = 5;
    std::vector<int> denominations3 = {2, 5, 10, 20, 50};
    int p3 = 45;
    int q3 = 100;
    runTestCase(n3, denominations3, p3, q3);

    // Test Case 4
    std::cout << "Test Case 4:\n";
    int n4 = 3;
    std::vector<int> denominations4 = {1, 2, 5};
    int p4 = 11;
    int q4 = 20;
    runTestCase(n4, denominations4, p4, q4);

    // Test Case 5
    std::cout << "Test Case 5:\n";
    int n5 = 7;
    std::vector<int> denominations5 = {1, 2, 5, 10, 20, 50, 100};
    int p5 = 96;
    int q5 = 200;
    runTestCase(n5, denominations5, p5, q5);

    return 0;
}
