# C++ Applications with Auto-Containerization

This repository contains multiple C++ applications that can be automatically containerized using a Python script. The project demonstrates how to create a Docker container for C++ applications with minimal effort.

## Project Structure

- `auto_containerize_cpp.py` - Python script that automates the containerization process
- `app-1-calendar/` - A calendar application with task management features
- `app-2-calculator/` - A simple calculator application

## Auto-Containerization Script

The `auto_containerize_cpp.py` script automates the process of:
1. Identifying C++ source files in a specified directory
2. Generating a Makefile to compile the code
3. Creating a Dockerfile for containerizing the app
4. Building a Docker image that compiles and runs the C++ project

### Usage

```bash
# Make sure the script is set to use the desired application directory
python3 auto_containerize_cpp.py
```

To use a different application directory, edit the following line in `auto_containerize_cpp.py`:

```python
def identify_cpp_files(base_dir="app-1-calendar"):
    # Change to "app-2-calculator" or any other directory containing C++ files
```

### Docker Container

After running the script, a Docker image will be created. You can run the containerized application with:

```bash
docker run -it cpp-calendar-app
```

## Available Applications

### 1. Calendar Application with Task Manager

A calendar application that displays a monthly calendar and allows users to add tasks for specific days.

**Features:**
- Display calendar for any month and year (from 1900 onwards)
- Add tasks for specific days
- Visual indication of days with tasks

[See Calendar App Details](app-1-calendar/README.md)

### 2. Calculator Application

A simple calculator application that demonstrates basic arithmetic operations.

**Features:**
- Basic arithmetic operations (add, subtract, multiply, divide)
- User input handling
- Division by zero handling

[See Calculator App Details](app-2-calculator/README.md)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


