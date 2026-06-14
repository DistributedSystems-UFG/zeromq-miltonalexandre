import zmq
import time


def fat(n):
    if n == 0:
        return 1
    else:
        return n * fat(n - 1)


def get_date():
    return time.asctime()


def server():
    context = zmq.Context()
    socket = context.socket(zmq.REP)  # create reply socket
    socket.bind("tcp://*:12345")  # bind socket to address

    while True:
        message = socket.recv().decode()  # wait for incoming message
        print("Received message")
        if "STOP" not in message:  # if not to stop...
            if message == "TIME":
                socket.send(get_date().encode())
            elif message.startswith("FAT"):
                i = int(message.split()[1])
                socket.send(str(fat(i)).encode())
            print("Replying")
        else:
            break  # break out of loop and end


if __name__ == "__main__":  # -
    server()
