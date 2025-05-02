# Simple Calculator App

A basic C++ calculator application that demonstrates:
- Basic arithmetic operations (add, subtract, multiply, divide)
- User input handling
- Division by zero error handling
- Multiple files project structure

## Files
- `main.cpp` - Contains the main function and UI logic
- `calculator.h` - Header file with function declarations
- `calculator.cpp` - Implementation of calculator functions

## How to Build Manually
```bash
g++ -o calculator main.cpp calculator.cpp -std=c++17
```

## How to Run Manually
```bash
./calculator
```

## Using with auto_containerize_cpp.py
This application can be containerized using the auto_containerize_cpp.py script at the root level.
Ensure you are in the root directory (not the cpp directory) when running the script. 