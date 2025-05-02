#include "calculator.h"

// Addition function
int add(int a, int b) {
    return a + b;
}

// Subtraction function
int subtract(int a, int b) {
    return a - b;
}

// Multiplication function
int multiply(int a, int b) {
    return a * b;
}

// Division function
double divide(int a, int b) {
    // Handle division by zero by returning 0
    if (b == 0) {
        return 0;
    }
    return static_cast<double>(a) / b;
} 