FROM gcc:latest
# Use official GCC compiler image
WORKDIR /app
# Set working directory in container
COPY . ./
# Copy all local files into the container
RUN make
# Build the C++ project using the Makefile
CMD ["./calendar"]
# Command to run the app when container starts
