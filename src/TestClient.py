import zmq


def main():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    # prompt user for input
    parkCode = input("Enter a park code or return for a random park: ")

    # send the park or random
    print(f"Sending request for: {parkCode}")
    socket.send_string(parkCode)

    # wait on response
    message = socket.recv_string()
    print("Received reply", "[", message, "]")


if __name__ == "__main__":
    main()
