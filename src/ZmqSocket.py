# Author: Vince Tran
# Date: 02/25/2024
# Description: this file facilitates communication between server and client
# using ZeroMQ sockets.

import zmq
import json
from NpsApiHandler import getParkName


def startZmq(port):
    # socket setup
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind(f"tcp://*:{port}")

    print(f"ZMQ socket is listening on port {port}...")

    while True:
        # wait for request from client
        message = socket.recv_string()
        print(f"Received request: {message}")

        try:
            # parse request
            parkName = getParkName(message)
            response = json.dumps({"parkName": parkName})
        except Exception as e:
            response = json.dumps({"error": str(e)})

        socket.send_string(response)


if __name__ == "__main__":
    startZmq(5555)
