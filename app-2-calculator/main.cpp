#include <iostream>
#include "calculator.h"

int main() {
    std::cout << "Simple Calculator App" << std::endl;
    std::cout << "====================" << std::endl;
    
    int a = 10;
    int b = 5;
    
    std::cout << a << " + " << b << " = " << add(a, b) << std::endl;
    std::cout << a << " - " << b << " = " << subtract(a, b) << std::endl;
    std::cout << a << " * " << b << " = " << multiply(a, b) << std::endl;
    std::cout << a << " / " << b << " = " << divide(a, b) << std::endl;
    
    // Get user input
    int x, y;
    char operation;
    
    std::cout << "\nEnter calculation in format 'number operation number' (e.g., 5 + 3): ";
    std::cin >> x >> operation >> y;
    
    switch (operation) {
        case '+':
            std::cout << "Result: " << add(x, y) << std::endl;
            break;
        case '-':
            std::cout << "Result: " << subtract(x, y) << std::endl;
            break;
        case '*':
            std::cout << "Result: " << multiply(x, y) << std::endl;
            break;
        case '/':
            if (y != 0) {
                std::cout << "Result: " << divide(x, y) << std::endl;
            } else {
                std::cout << "Error: Division by zero!" << std::endl;
            }
            break;
        default:
            std::cout << "Unsupported operation!" << std::endl;
    }
    
    return 0;
} 