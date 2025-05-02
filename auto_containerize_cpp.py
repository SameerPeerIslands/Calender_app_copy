# auto_containerize_cpp.py

import os
import platform
import subprocess

DOCKER_IMAGE_NAME = "cpp-calendar-app"
EXECUTABLE_NAME = "calendar"

def identify_cpp_files():
    return [f for f in os.listdir() if f.endswith(".cpp")]

def generate_makefile(source_files, target=EXECUTABLE_NAME):
    # Linux-compatible flags only
    cxx = "g++"
    flags = "-Wall -Wextra -std=c++17"

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
    with open("Makefile", "w") as f:
        f.write(makefile_content)

    print("✅ Makefile generated.")

def build_cpp_project():
    print("⏩ Skipping local build (done inside Docker)")

def generate_dockerfile():
    dockerfile_content = f"""\
FROM gcc:latest
WORKDIR /app
COPY . .
RUN make
CMD ["./{EXECUTABLE_NAME}"]
"""
    with open("Dockerfile", "w") as f:
        f.write(dockerfile_content)

    print("📦 Dockerfile generated.")

def build_docker_image():
    print(f"🐳 Building Docker image '{DOCKER_IMAGE_NAME}'...")
    subprocess.run(["docker", "build", "-t", DOCKER_IMAGE_NAME, "."], check=True)
    print(f"✅ Docker image '{DOCKER_IMAGE_NAME}' built successfully.")

if __name__ == "__main__":
    cpp_files = identify_cpp_files()
    if not cpp_files:
        raise Exception("❌ No C++ source files found in the directory.")

    print(f"🖥️ Detected platform: {platform.system()}")
    print(f"📄 Found C++ files: {cpp_files}")

    # Clean up stale binary
    if os.path.exists(EXECUTABLE_NAME):
        os.remove(EXECUTABLE_NAME)
        print(f"🧹 Removed stale local binary '{EXECUTABLE_NAME}'")

    generate_makefile(cpp_files)
    build_cpp_project()
    generate_dockerfile()
    build_docker_image()
