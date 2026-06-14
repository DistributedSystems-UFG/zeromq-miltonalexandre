import zmq
import constPipe

context = zmq.Context()

socket_input = context.socket(zmq.PULL)
socket_input.connect(f"tcp://{constPipe.SRC1}:{constPipe.PORT1}")

socket_workA = context.socket(zmq.PUSH)
socket_workA.bind(f"tcp://*:{constPipe.PORT2}")

socket_workB = context.socket(zmq.PUSH)
socket_workB.bind(f"tcp://*:{constPipe.PORT3}")

print("Load balancer started")

while True:
    work = socket_input.recv()
    number = int(work.decode())
    if number % 2 == 0:
        socket_workA.send(work)
    else:
        socket_workB.send(work)
