#ifndef CHANGE_H
#define CHANGE_H

#include <iostream>
#include <vector>
#include <algorithm>

class Change
{
private:
    // Vector que contiene las denominaciones de monedas disponibles
    std::vector<int> denominations;
    int numberOfCoins;

public:
    // Constructor de la clase Change
    // num_denominations: número de tipos de monedas
    // denoms: vector con las denominaciones de las monedas
    Change(int num_denominations, std::vector<int> denoms) : numberOfCoins(num_denominations), denominations(denoms)
    {
        std::sort(denominations.begin(), denominations.end(), std::greater<int>());
    }

    // Metodo para calcular el cambio
    // prize: cantidad que se debe pagar
    // bill: cantidad entregada por el cliente
    // Devuelve un vector con la cantidad de monedas de cada denominacion utilizadas para el cambio
    std::vector<int> calculateChange(int prize, int bill)
    {
        int change = bill - prize; // Calcula la cantidad de cambio
        std::vector<int> coinsUsed(numberOfCoins, 0);

        // Recorre las denominaciones y calcula cuántas monedas se necesitan de cada una
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

    // Metodo para imprimir el resultado
    // coinsUsed: vector con la cantidad de monedas usadas de cada denominación
    void printChange(const std::vector<int> &coinsUsed)
    {
        for (int i = 0; i < numberOfCoins; i++)
        {
            std::cout << coinsUsed[i] << std::endl;
        }
    }
};

#endif // CHANGE_H