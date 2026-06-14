import zmq

EC2_INSTANCE = "100.28.187.116"


def client():
    context = zmq.Context()
    socket = context.socket(zmq.SUB)  # create a subscriber socket
    socket.connect(f"tcp://{EC2_INSTANCE}:12345")  # connect to the server
    socket.setsockopt(zmq.SUBSCRIBE, b"TIME")  # subscribe to TIME messages
    socket.setsockopt(zmq.SUBSCRIBE, b"LOTERIA")  # subscribe to TIME messages
    socket.setsockopt(zmq.SUBSCRIBE, b"NEWS")  # subscribe to TIME messages

    for i in range(12):  # Five iterations
        msg_time = socket.recv()  # receive a message related to subscription
        print(msg_time.decode())  # print the result


# -
if __name__ == "__main__":  # -
    client()

