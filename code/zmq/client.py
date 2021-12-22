import zmq

context = zmq.Context()

print("Connecting to server...")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

for request in range(10):
    print("Sending reuest %s ..." % request)
    socket.send(b"elo bartek")

    message = socket.recv()
    print("Received reply %s [ %s ]" % (request, message))
