import zmq
import time
import constPipe
import threading


def worker(sock, name):
    while True:
        work = int(sock.recv())
        print(f"{name}: work for {work} seconds...")
        time.sleep(work)


context = zmq.Context()
sockA = context.socket(zmq.PULL)  # create a pull socket
sockB = context.socket(zmq.PULL)  # create a pull socket
p1 = f"tcp://{constPipe.SRC2}:{constPipe.PORT2}"  # address first task source
p2 = f"tcp://{constPipe.SRC3}:{constPipe.PORT3}"  # address second task source
sockA.connect(p1)  # connect to task source 1
sockB.connect(p2)  # connect to task source 2

t1 = threading.Thread(
    target=worker,
    args=(
        sockA,
        "Pares",
    ),
)
t2 = threading.Thread(
    target=worker,
    args=(
        sockB,
        "Impares",
    ),
)
t1.start()
t2.start()
t1.join()
t2.join()
