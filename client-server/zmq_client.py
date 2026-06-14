import zmq

EC2_INSTANCE = "100.28.187.116"


def client():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)  # create request socket

    socket.connect(f"tcp://{EC2_INSTANCE}:12345")  # block until connected
    socket.send(b"TIME")  # send message
    message = socket.recv()  # block until response
    print(message.decode())  # print result
    socket.send(b"FAT 5")  # send message
    message = socket.recv()  # block until response
    print(message.decode())  # print result
    socket.send(b"STOP")  # tell server to stop


if __name__ == "__main__":  # -
    client()
