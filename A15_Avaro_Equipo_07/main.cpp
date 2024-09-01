// -----------------------------------------------------

// Title: Implementation of the "Greedy Algorithms" programming technique

// Created On: 28/08/2024
// Updated On: 28/08/2024

// Authors:
//     Angel Mauricio Ramirez Herrera - A01710158
//     Cristian Chavez Guia - A0171680
//     Emiliano Gomez Gonzalez - A01710711

// Code Description:
//
//
//
//
//

// -----------------------------------------------------

/*
Utilizando las técnicas de programación de "algoritmos avaros", escribe en C++ un programa
que resuelva el problema del cambio de monedas.
*/

/*
El programa recibe un numero entero N, seguido de N valores enteros (uno en cada línea, no necesariamente
están ordenados) que representan las diferentes denominations disponibles de las monedas.
*/

#include <iostream>
#include <vector>
#include "change.h"
#include <algorithm>

int main()
{
    // Case 1: No denominations available
    std::vector<int> case1Denominations;
    Change change1(0, case1Denominations);
    std::vector<int> result1 = change1.calculateChange(50, 100); // P=50, Q=100
    std::cout << "Case 1: No denominations available\n";
    change1.printChange(result1);

    // Case 2: Single denomination available
    std::vector<int> case2Denominations = {25};
    Change change2(1, case2Denominations);
    std::vector<int> result2 = change2.calculateChange(75, 100); // P=75, Q=100, Change = 15
    std::cout << "Case 2: Single denomination available\n";
    change2.printChange(result2);

    // Case 3: Dataset 1
    std::vector<int> case3Denominations = {4, 5, 25, 10, 50, 325, 500};
    Change change3(7, case3Denominations);
    std::vector<int> result3 = change3.calculateChange(83, 100); // P=83, Q=100, Change = 17
    std::cout << "Case 3: Data entry 1\n";
    change3.printChange(result3);

    // Case 4: Dataset 2
    std::vector<int> case4Denominations = {4, 20, 25, 10, 5, 160, 200};
    Change change4(7, case4Denominations);
    std::vector<int> result4 = change4.calculateChange(134, 200); // P=134, Q=200, Change = 66
    std::cout << "Case 4: Data entry 2\n";
    change4.printChange(result4);

    // Case 4: Dataset 3
    std::vector<int> case4Denominations = {3, 1, 10, 7, 85, 100};
    Change change5(6, case4Denominations);
    std::vector<int> result4 = change4.calculateChange(134, 200); // P=134, Q=200, Change = 66
    std::cout << "Case 4: Data entry 3\n";
    change4.printChange(result4);

    // Case 4: Dataset 4
    std::vector<int> case4Denominations = {5, 100, 25, 10, 5, 1, 711, 1000};
    Change change6(8, case4Denominations);
    std::vector<int> result4 = change4.calculateChange(134, 200); // P=134, Q=200, Change = 66
    std::cout << "Case 4: Data entry 4\n";
    change4.printChange(result4);

    // Case 5: Large bill with small denominations
    std::vector<int> case5Denominations = {1, 5, 10, 25, 50, 100};
    Change change7(6, case5Denominations);
    std::vector<int> result5 = change5.calculateChange(76, 1000); // P=76, Q=1000, Change = 924
    std::cout << "Case 5: Large bill with small denominations\n";
    change5.printChange(result5);

    return 0;
}
