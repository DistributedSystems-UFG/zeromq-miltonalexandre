import zmq
import random
import constPipe


def producer(port):
    context = zmq.Context()
    socket = context.socket(zmq.PUSH)  # create a push socket
    socket.bind("tcp://*:" + port)  # bind socket to address

    for i in range(10):  # generate 10 workloads
        workload = random.randint(6, 10)  # compute workload
        print(f"Workload of {workload} seconds")
        socket.send(str(workload).encode())  # send workload to worker


producer(constPipe.PORT1)
