# Calendar Application with Task Manager

A simple C++ calendar application that displays a calendar for any month and year, allowing users to add and track tasks for specific days.

## Features

- Display a visual calendar for any month and year (from 1900 onwards)
- Add tasks for specific days in the selected month
- Visual indication of days with tasks (marked with an asterisk *)
- List all tasks after displaying the calendar

## How It Works

1. The user enters a year (must be 1900 or later)
2. The user enters a month (1-12)
3. The program asks if the user wants to add tasks for the selected month
4. If yes, the user can add tasks for specific days
5. The calendar is displayed with days containing tasks marked with an asterisk (*)
6. All tasks are listed below the calendar

## Code Structure

- `main.cpp` - The complete application in a single file
- Main Functions:
  - `PrintMonth` - Prints the entire month calendar
  - `PrintMonthTitle` - Prints the month and year header
  - `PrintMonthBody` - Prints the days of the month
  - `GetStartDay` - Calculates the starting day of the week
  - `GetTotalNumberOfDaysInMonth` - Gets the number of days in the month
  - `IsLeapYear` - Checks if a year is a leap year

## How to Build and Run

### Manual Build

```bash
# Compile with g++
g++ -o calendar app-1-calendar/main.cpp -std=c++11

# Run the compiled program
./calendar
```

### Using Containerization Script

1. Make sure the `auto_containerize_cpp.py` script is pointing to this directory:
   ```python
   def identify_cpp_files(base_dir="app-1-calendar"):
   ```

2. Run the containerization script from the project root:
   ```bash
   python3 auto_containerize_cpp.py
   ```

3. Run the Docker container:
   ```bash
   docker run -it cpp-calendar-app
   ```

## Usage Example

```
Enter Year:
2023
Enter Month (1-12):
5
Do you want to add tasks for this month? (y/n): y
Enter day: 15
Enter task: Meeting with team
Add another task? (y/n): y
Enter day: 20
Enter task: Doctor appointment
Add another task? (y/n): n

May
2023
----------------------------
 Sun Mon Tue Wed Thu Fri Sat
     1   2   3   4   5   6
  7   8   9  10  11  12  13
 14  15* 16  17  18  19  20*
 21  22  23  24  25  26  27
 28  29  30  31

Tasks:
Day 15: Meeting with team
Day 20: Doctor appointment
``` 