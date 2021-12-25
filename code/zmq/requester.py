import zmq
import sys 
import time

context = zmq.Context()

print("Connecting to server...")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

device_id = sys.argv[1] if len(sys.argv) > 1 else "1"


for request in range(100):
    print(f"Sending request {request}")
    socket.send_string(f"{device_id}")
    message = socket.recv()
    print(f"Received reply {request} [ {message} ]")
    #time.sleep(1)





##for request in range(100):
#while True:
#    #print("Sending request %s ..." % request)
#    socket.send_string(f"{device_id}")
#    message = socket.recv()
#    print(f"Received reply {message}")
#    #print("Received reply %s [ %s ]" % (request, message))
#    #time.sleep(1)
