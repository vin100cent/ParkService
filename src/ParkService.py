# Author: Vince Tran
# Date: 02/25/2024
# Description: Main file with start script for NPS API Microservice

from ZmqSocket import startZmq


def main():
    print("Starting NPS API Microservice...")

    userPort = (
        input(
            "Please provide a preferred port number (or hit enter to keep default 5555): "
        ).strip()
        or "5555"
    )
    port = int(userPort)

    print(f"Continuing on port{port}...")
    # starts on the default port, change if needed
    startZmq(port)


if __name__ == "__main__":
    main()
