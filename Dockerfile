FROM ubuntu:22.04

RUN apt-get update && apt-get install -y g++ build-essential

WORKDIR /app

COPY main.cpp .

RUN g++ -std=c++11 -o calendar main.cpp

CMD ["./calendar"]