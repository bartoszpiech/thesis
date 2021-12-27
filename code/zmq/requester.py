import zmq
import sys 
import time

context = zmq.Context()

print("Connecting to server...")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

device_id = sys.argv[1] if len(sys.argv) > 1 else "1"

bytes_read = 0
for request in range(1000):
    print(f"Sending request {request}")
    socket.send_string(f"{device_id}")
    message = socket.recv()
    bytes_read += len(message)
    print(f"Received reply {request} [ {message} ]")

# for benchmark purpose
print(f'Total bytes read: {bytes_read}')

##for request in range(100):
#while True:
#    #print("Sending request %s ..." % request)
#    socket.send_string(f"{device_id}")
#    message = socket.recv()
#    print(f"Received reply {message}")
#    #print("Received reply %s [ %s ]" % (request, message))
#    #time.sleep(1)
