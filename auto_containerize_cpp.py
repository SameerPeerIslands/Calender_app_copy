import os
import subprocess

# ----- CONFIG -----
source_file = "main.cpp"
binary_name = "calendar"
docker_image_name = "cpp-calendar-app"
dockerfile_name = "Dockerfile"

# ----- STEP 1: Validate source file -----
if not os.path.exists(source_file):
    raise FileNotFoundError(f"{source_file} not found in the current directory.")

# ----- STEP 2: Generate Dockerfile -----
dockerfile_contents = f"""
FROM ubuntu:22.04

RUN apt-get update && apt-get install -y g++ build-essential

WORKDIR /app

COPY {source_file} .

RUN g++ -std=c++11 -o {binary_name} {source_file}

CMD ["./{binary_name}"]
"""

with open(dockerfile_name, "w") as f:
    f.write(dockerfile_contents.strip())

print(f"✅ Dockerfile generated as '{dockerfile_name}'")

# ----- STEP 3: Build Docker image -----
print(f"🔧 Building Docker image '{docker_image_name}'...")
subprocess.run(["docker", "build", "-t", docker_image_name, "."], check=True)
print(f"✅ Docker image '{docker_image_name}' built successfully.")

# Optional: Uncomment to run the container interactively
# subprocess.run(["docker", "run", "-it", docker_image_name])
