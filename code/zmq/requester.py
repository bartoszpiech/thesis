import zmq
import time

context = zmq.Context()

print("Connecting to server...")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

for request in range(100):
    print("Sending request %s ..." % request)
    socket.send(b"123")
    message = socket.recv()
    print("Received reply %s [ %s ]" % (request, message))
