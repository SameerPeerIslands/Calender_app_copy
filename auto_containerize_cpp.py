# This script automates the process of:
# 1. Identifying C++ source files (even in subdirectories)
# 2. Generating a Makefile to compile the code
# 3. Creating a Dockerfile for containerizing the app
# 4. Building a Docker image that compiles and runs the C++ project inside the container

import os           # For file system operations
import platform     # To detect the current operating system (for logs)
import subprocess   # To run shell commands like `docker build`

# Docker image name to be created
DOCKER_IMAGE_NAME = "cpp-calendar-app"

# The name of the final executable that will be built
EXECUTABLE_NAME = "calendar"

# 🔍 Function to recursively identify all C++ source files in the project
def identify_cpp_files(base_dir="."):
    # Supported C++ source file extensions
    cpp_extensions = (".cpp", ".cc", ".cxx", ".C")
    cpp_files = []

    # Walk through the directory tree
    for root, _, files in os.walk(base_dir):
        for file in files:
            if file.endswith(cpp_extensions):
                # Store the path relative to the base directory (required for Makefile)
                relative_path = os.path.relpath(os.path.join(root, file), base_dir)
                cpp_files.append(relative_path)

    return cpp_files

# 🛠️ Function to generate a Makefile for compiling the C++ project
def generate_makefile(source_files, target=EXECUTABLE_NAME):
    # Use g++ as the compiler
    cxx = "g++"
    # Compiler flags: show warnings and use C++17 standard
    flags = "-Wall -Wextra -std=c++17"

    # Makefile template content
    makefile_content = f"""\
# Auto-generated Makefile

CXX = {cxx}
CXXFLAGS = {flags}
TARGET = {target}
SRC = {' '.join(source_files)}

all: $(TARGET)

$(TARGET): $(SRC)
\t$(CXX) $(CXXFLAGS) -o $(TARGET) $(SRC)

clean:
\trm -f $(TARGET)
"""

    # Write the Makefile to disk
    with open("Makefile", "w") as f:
        f.write(makefile_content)

    print("✅ Makefile generated.")

# ⚙️ This function is intentionally left empty since we are compiling inside Docker
def build_cpp_project():
    print("⏩ Skipping local build (done inside Docker)")

# 📦 Function to generate a Dockerfile that builds and runs the C++ app
def generate_dockerfile():
    # Dockerfile contents
    dockerfile_content = f"""\
FROM gcc:latest
# Use official GCC compiler image
WORKDIR /app
# Set working directory in container
COPY . ./
# Copy all local files into the container
RUN make
# Build the C++ project using the Makefile
CMD ["./{EXECUTABLE_NAME}"]
# Command to run the app when container starts
"""
    # Write the Dockerfile to disk
    with open("Dockerfile", "w") as f:
        f.write(dockerfile_content)

    print("📦 Dockerfile generated.")

# 🐳 Function to build the Docker image using the Dockerfile
def build_docker_image():
    print(f"🐳 Building Docker image '{DOCKER_IMAGE_NAME}'...")
    subprocess.run(["docker", "build", "-t", DOCKER_IMAGE_NAME, "."], check=True)
    print(f"✅ Docker image '{DOCKER_IMAGE_NAME}' built successfully.")

# 🚀 Main script execution starts here
if __name__ == "__main__":
    # Step 1: Find all C++ source files
    cpp_files = identify_cpp_files()
    if not cpp_files:
        raise Exception("❌ No C++ source files found in the directory.")

    # Step 2: Display detected platform and C++ files
    print(f"🖥️ Detected platform: {platform.system()}")
    print(f"📄 Found C++ files: {cpp_files}")

    # Step 3: Remove previously compiled binary if it exists (to avoid OS format mismatch)
    if os.path.exists(EXECUTABLE_NAME):
        os.remove(EXECUTABLE_NAME)
        print(f"🧹 Removed stale local binary '{EXECUTABLE_NAME}'")

    # Step 4: Generate Makefile
    generate_makefile(cpp_files)

    # Step 5: Skip local build (Docker will handle it)
    build_cpp_project()

    # Step 6: Create Dockerfile
    generate_dockerfile()

    # Step 7: Build Docker image
    build_docker_image()
